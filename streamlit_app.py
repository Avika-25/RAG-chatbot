"""
Streamlit-based RAG Chatbot Interface

This script creates a web interface for the RAG Chatbot using Streamlit.
It allows users to interact with the chatbot through a web browser.

Author: Your Name
Date: Current Date
"""

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load environment variables
load_dotenv()

# Constants
CHROMA_PATH = "chroma"

# Page config
st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="centered",
)

def initialize_session_state():
    """Initialize session state variables."""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    
    if "qa_chain" not in st.session_state:
        st.session_state.qa_chain = None

@st.cache_resource
def initialize_rag_chatbot():
    """
    Initialize the RAG chatbot with vector store and LLM.
    
    Returns:
        A ConversationalRetrievalChain ready to answer questions
    """
    # Check if vector store exists
    if not os.path.exists(CHROMA_PATH):
        st.error("Vector database not found. Please run create_database.py first.")
        st.stop()
    
    # Set up the vector store
    embedding_function = OpenAIEmbeddings()
    vector_store = Chroma(
        persist_directory=CHROMA_PATH, 
        embedding_function=embedding_function
    )
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
    
    # Set up the language model
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    
    # Create memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"  # This matches the output key in ConversationalRetrievalChain
    )
    
    # Create the conversational chain
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True
    )
    
    return qa_chain

def main():
    # Initialize session state
    initialize_session_state()
    
    # Initialize RAG chatbot if not already done
    if st.session_state.qa_chain is None:
        with st.spinner("Initializing chatbot..."):
            st.session_state.qa_chain = initialize_rag_chatbot()
    
    # App title
    st.title("RAG Chatbot")
    st.markdown("""
    This chatbot uses Retrieval-Augmented Generation (RAG) to answer questions based on a custom knowledge base.
    Ask questions related to BuildFastWithAI!
    """)
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "sources" in message and message["sources"]:
                with st.expander("Sources"):
                    sources_list = message["sources"]
                    for source in sources_list:
                        st.markdown(f"- {source}")
    
    # Chat input
    if prompt := st.chat_input("Ask a question..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate and display assistant response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response_container = st.empty()
                sources_container = st.container()
                
                # Get response from the chain
                result = st.session_state.qa_chain.invoke({"question": prompt})
                answer = result.get("answer", "I couldn't find an answer to that.")
                
                # Extract sources if available
                sources = []
                source_documents = result.get("source_documents", [])
                if source_documents:
                    sources = [doc.metadata.get("source", "Unknown") for doc in source_documents]
                    sources = list(set(sources))  # Remove duplicates
                
                # Display the response
                response_container.markdown(answer)
                
                # Display sources if available
                if sources:
                    with sources_container.expander("Sources"):
                        for source in sources:
                            st.markdown(f"- {source}")
                
                # Add assistant message to chat history
                st.session_state.messages.append({
                    "role": "assistant", 
                    "content": answer,
                    "sources": sources
                })

if __name__ == "__main__":
    main()