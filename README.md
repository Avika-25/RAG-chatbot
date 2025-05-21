# RAG Chatbot Project Documentation

## Project Overview
This project implements a Retrieval-Augmented Generation (RAG) chatbot that uses a vector database to retrieve relevant information from a knowledge base and generate responses to user queries. The project consists of four main Python scripts:

1. `create_database.py`: Creates a Chroma vector database from Markdown files
2. `query_data.py`: Provides a command-line interface to query the database
3. `rag_chatbot.py`: Implements an interactive console-based RAG chatbot
4. `streamlit_app.py`: Creates a web interface for the RAG chatbot using Streamlit

## Script Documentation

### `create_database.py`

```python
"""
Script to create a Chroma vector database from Markdown files for the RAG chatbot.
This loads documents, splits them into chunks, and stores embeddings.

Author: Your Name
Date: May 2025
"""

# Import necessary libraries for document loading, splitting, and vector storage
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key from environment variables
openai.api_key = os.environ['OPENAI_API_KEY']

# Define paths for data and Chroma database
CHROMA_PATH = "chroma"  # Directory to store the vector database
DATA_PATH = "data"      # Directory containing Markdown files

def main():
    """
    Main function to start the database creation process.
    
    This function serves as the entry point for the script and calls
    the generate_data_store function to begin the process of creating
    the vector database.
    """
    generate_data_store()

def generate_data_store():
    """
    Generate the vector store by loading documents, splitting them, and saving to Chroma.
    
    This is the core function that orchestrates the entire process:
    1. Loads documents from the data directory
    2. Splits the documents into manageable chunks
    3. Creates embeddings and stores them in the Chroma database
    """
    documents = load_documents()  # Load all Markdown files
    chunks = split_text(documents)  # Split documents into smaller chunks
    save_to_chroma(chunks)  # Save chunks as embeddings in Chroma

def load_documents():
    """
    Load Markdown files from the data directory.
    
    This function uses LangChain's DirectoryLoader to find and load
    all .md files from the DATA_PATH directory.
    
    Returns:
        list[Document]: A list of Document objects containing the content and metadata
                        of each Markdown file.
    """
    # Initialize DirectoryLoader to load all .md files from DATA_PATH
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()  # Load the documents
    return documents

def split_text(documents: list[Document]):
    """
    Split documents into smaller chunks for embedding.
    
    This function divides each document into smaller chunks to improve embedding
    quality and retrieval accuracy. It uses RecursiveCharacterTextSplitter
    to create chunks with specified size and overlap.
    
    Args:
        documents (list[Document]): List of Document objects to split.
        
    Returns:
        list[Document]: List of chunked Document objects with updated metadata.
    """
    # Initialize text splitter with chunk size and overlap
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  # Max size of each chunk
        chunk_overlap=200,  # Overlap to maintain context between chunks
        length_function=len,  # Use length function to measure chunk size
        add_start_index=True,  # Include start index in metadata
    )
    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)
    # Print the number of documents and chunks for verification
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

    # If there are chunks, print a sample for debugging
    if chunks:
        document = chunks[min(10, len(chunks)-1)]  # Pick a sample chunk (up to 10th)
        print("Sample chunk content:")
        print(document.page_content)  # Show the content of the sample chunk
        print("Sample chunk metadata:")
        print(document.metadata)  # Show metadata like source file

    return chunks

def save_to_chroma(chunks: list[Document]):
    """
    Save document chunks to a Chroma vector store.
    
    This function creates embeddings for each document chunk and stores them
    in a Chroma vector database. If the database already exists, it is deleted
    and recreated from scratch.
    
    Args:
        chunks (list[Document]): List of Document chunks to embed and store.
    """
    # If Chroma directory exists, delete it to start fresh
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    # Create a new Chroma database with the chunks and OpenAI embeddings
    db = Chroma.from_documents(
        chunks, OpenAIEmbeddings(), persist_directory=CHROMA_PATH
    )
    # Confirm the number of chunks saved
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```

### `query_data.py`

```python
"""
Script to query the Chroma vector database and get answers using a RAG pipeline.
This provides a command-line interface to ask questions.

Author: Your Name
Date: May 2025
"""

# Import libraries for argument parsing, vector store, and LLM
import argparse
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Define path for Chroma database
CHROMA_PATH = "chroma"

# Define the prompt template for the LLM
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

def main():
    """
    Main function to handle command-line query input and output.
    
    This function sets up argument parsing, retrieves relevant documents from
    the vector database based on the query, and sends the context and query
    to the language model for generating a response.
    """
    # Set up command-line argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text  # Get the query from command-line input

    # Prepare the vector database
    embedding_function = OpenAIEmbeddings()  # Initialize OpenAI embeddings
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the database for relevant documents
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    # Check if results are empty or not relevant enough
    if len(results) == 0 or results[0][1] < 0.2:
        print(f"Unable to find matching results.")
        return

    # Combine document content into context for the prompt
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    # Create and format the prompt with context and question
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    # Uncomment the line below to debug the full prompt
    # print(prompt)

    # Initialize the LLM (GPT-3.5-turbo)
    model = ChatOpenAI(model_name="gpt-3.5-turbo")
    # Get the response from the LLM
    response_text = model.invoke(prompt).content

    # Extract sources from document metadata
    sources = [doc.metadata.get("source", None) for doc, _score in results]

    # Print the response and sources neatly
    print("Response:", response_text)
    print("Sources:", sources)

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```

### `rag_chatbot.py`

```python
"""
RAG Chatbot using LangChain

This script creates an interactive conversational chatbot that uses Retrieval-Augmented Generation
to answer questions based on a knowledge base. It supports conversation history.

Author: Your Name
Date: May 2025
"""

# Import libraries for vector store, LLM, memory, and environment variables
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Load environment variables from .env file
load_dotenv()

# Define path for Chroma database
CHROMA_PATH = "chroma"

def initialize_rag_chatbot():
    """
    Initialize the RAG chatbot with vector store and LLM.
    
    This function sets up all components needed for the chatbot:
    - Vector store connection
    - Document retriever
    - Language model
    - Conversation memory
    - Conversational chain
    
    Returns:
        ConversationalRetrievalChain: A chain that combines retrieval and conversation
                                     capabilities for answering questions.
    """
    # Set up the vector store for document retrieval
    embedding_function = OpenAIEmbeddings()  # Initialize embeddings
    vector_store = Chroma(
        persist_directory=CHROMA_PATH, 
        embedding_function=embedding_function
    )
    # Configure retriever to get top 3 relevant documents
    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Set up the language model
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")  # Use GPT-3.5-turbo for responses

    # Create memory to store conversation history
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True,
        output_key="answer"  # Matches the output key in ConversationalRetrievalChain
    )

    # Create the conversational chain with LLM, retriever, and memory
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        verbose=True  # Set to False in production
    )

    return qa_chain

def chat_loop():
    """
    Main chat loop for interacting with the RAG chatbot.
    
    This function creates an interactive console-based chat interface where:
    - Users can type questions and get responses
    - The chatbot provides answers based on retrieved documents
    - Sources are displayed for each response
    - The conversation continues until the user exits
    """
    qa_chain = initialize_rag_chatbot()  # Initialize the chatbot

    # Print welcome message
    print("\n===== RAG Chatbot =====")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input("\nYou: ")  # Get user input

        # Check if user wants to exit
        if user_input.lower() in ["exit", "quit"]:
            print("\nThank you for chatting! Goodbye.")
            break

        # Try to get a response from the chatbot
        try:
            result = qa_chain.invoke({"question": user_input})
            answer = result.get("answer", "I couldn't find an answer to that.")

            # Extract sources from retrieved documents
            sources = []
            source_documents = result.get("source_documents", [])
            if source_documents:
                sources = [doc.metadata.get("source", "Unknown") for doc in source_documents]
                sources = list(set(sources))  # Remove duplicate sources

            # Print the chatbot's response
            print("\nChatbot:", answer)

            # Print sources if available
            if sources:
                print("\nSources:", sources)

        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again with a different question or check your setup.")

def main():
    """
    Main function to check for vector store and start the chat loop.
    
    This function verifies that the Chroma database exists before
    starting the interactive chat loop.
    """
    # Check if the Chroma database exists
    if not os.path.exists(CHROMA_PATH):
        print("Error: Vector database not found. Please run create_database.py first.")
        return

    # Start the interactive chat loop
    chat_loop()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
```

### `streamlit_app.py`

```python
"""
Streamlit-based RAG Chatbot Interface

This script creates a web interface for the RAG Chatbot using Streamlit.
It allows users to interact with the chatbot through a web browser.

Author: Your Name
Date: May 2025
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
    """
    Initialize session state variables for Streamlit.
    
    This function sets up the session state to store:
    - Message history
    - Chat history for the LLM
    - The QA chain instance
    
    These variables persist across reruns of the Streamlit app.
    """
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
    
    This function is cached by Streamlit to prevent reinitialization
    on each rerun. It sets up all components needed for the chatbot:
    - Vector store connection
    - Document retriever
    - Language model
    - Conversation memory
    - Conversational chain
    
    Returns:
        ConversationalRetrievalChain: A chain that combines retrieval and conversation
                                     capabilities for answering questions.
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
    """
    Main function to set up and run the Streamlit web application.
    
    This function:
    1. Initializes the session state
    2. Sets up the RAG chatbot
    3. Creates the web interface with title and description
    4. Displays the chat history
    5. Handles user input and generates responses
    6. Updates the chat interface with new messages
    """
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
```

## Project Structure

```
project/
├── .env                      # Environment variables file (API keys)
├── create_database.py        # Script to create the vector database
├── query_data.py             # Script for command-line querying
├── rag_chatbot.py            # Console-based interactive chatbot
├── streamlit_app.py          # Web interface for the chatbot
├── data/                     # Directory containing Markdown files for the knowledge base
│   └── *.md                  # Markdown files with content
└── chroma/                   # Directory for the Chroma vector database (created by scripts)
```

## Setup Instructions

1. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. Install required dependencies:
   ```
   pip install langchain langchain_community langchain_openai langchain_chroma openai python-dotenv streamlit
   ```

3. Create a `data` directory and add your Markdown files.

4. Run `create_database.py` to generate the vector database:
   ```
   python create_database.py
   ```

5. Use one of the following methods to interact with the chatbot:
   - Command-line query: `python query_data.py "Your question here"`
   - Interactive console: `python rag_chatbot.py`
   - Web interface: `streamlit run streamlit_app.py`

## Best Practices Implemented

- **Modularity**: Each script has a specific responsibility
- **Documentation**: All functions and classes have detailed docstrings
- **Error Handling**: Input validation and exception handling
- **Environment Variables**: API keys stored in .env file
- **Caching**: Streamlit caching for improved performance
- **Consistent Style**: PEP 8 compliant code formatting