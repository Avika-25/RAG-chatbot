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
    Returns:
        A ConversationalRetrievalChain ready to answer questions
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
    Users can type questions and get responses with sources.
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
    """Main function to check for vector store and start the chat loop."""
    # Check if the Chroma database exists
    if not os.path.exists(CHROMA_PATH):
        print("Error: Vector database not found. Please run create_database.py first.")
        return

    # Start the interactive chat loop
    chat_loop()

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()