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
    """Main function to handle command-line query input and output."""
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