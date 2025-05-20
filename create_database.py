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
    """Main function to start the database creation process."""
    generate_data_store()

def generate_data_store():
    """
    Generate the vector store by loading documents, splitting them, and saving to Chroma.
    This is the core function that orchestrates the entire process.
    """
    documents = load_documents()  # Load all Markdown files
    chunks = split_text(documents)  # Split documents into smaller chunks
    save_to_chroma(chunks)  # Save chunks as embeddings in Chroma

def load_documents():
    """
    Load Markdown files from the data directory.
    Returns a list of Document objects.
    """
    # Initialize DirectoryLoader to load all .md files from DATA_PATH
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()  # Load the documents
    return documents

def split_text(documents: list[Document]):
    """
    Split documents into smaller chunks for embedding.
    Args:
        documents: List of Document objects to split.
    Returns:
        List of chunked Document objects.
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
    Args:
        chunks: List of Document chunks to embed and store.
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