---
title: Giskard Evaluation & Testing Framework for AI Systems
date: January 9, 2025
url: https://www.buildfastwithai.com/blogs/giskard-evaluation-testing-framework-for-ai-systems
---

# Giskard Evaluation & Testing Framework for AI Systems

## Introduction

## Setting Up Giskard: The First Steps

## Building an AI Model with LangChain

## Evaluating the Model with Giskard

## Conclusion

## Resources

### Installation

### Setting Up the OpenAI API Key

### Step 1: Preparing the Vector Store

### Step 2: Defining the Prompt Template

### Step 3: Creating the QA Chain

### Wrapping the Model

### Testing with Example Data

### Scanning for Vulnerabilities

### Generating Automated Test Suites

### Summary

### Next Steps

#### Why These Libraries?

#### Code Breakdown

#### Expected Output

#### Real-World Applications

#### Why Use a Prompt Template?

#### Explanation

#### Example Query

#### Key Features

#### Expected Output

#### Use Case

#### Saving the Report

The best time to start with AI was yesterday. The second best time? Right after reading this post. The fastest way? Gen AI Launch Pad’s 6-week transformation.

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

Artificial intelligence (AI) systems are becoming indispensable in industries ranging from healthcare to finance. However, the rapid adoption of AI models raises critical questions about their reliability, fairness, and security. Addressing these concerns is essential to prevent unintended consequences and build trust in AI systems. Giskard, an open-source Python library, provides a comprehensive framework for evaluating and testing AI models. This guide explores Giskard’s powerful capabilities, from setup and integration to model evaluation, showcasing a practical example of building a climate-focused question-answering (QA) system using LangChain and OpenAI models.

By the end of this blog, you will understand:

Before we delve into model creation and evaluation, it is crucial to install Giskard and its dependencies. Use the following command to set up your environment:

This installation includes:

Giskard acts as the foundation for testing, while LangChain and FAISS simplify the creation of AI models that require advanced document retrieval and processing capabilities. These libraries are especially useful for building QA models based on extensive textual data.

To access OpenAI’s language models, you need to securely set up your API key. The following snippet ensures this is done correctly:

This snippet retrieves your OpenAI API key securely from Colab’s user data. Replace this with your preferred method of securely handling API keys if you’re not using Google Colab.

Now that we’ve set up the environment, let’s build an AI model to answer climate-related questions using data from the IPCC Climate Change Synthesis Report (2023).

The first step in creating a QA model is to preprocess the document and store it in a retrievable format. We use LangChain’s text processing and FAISS for this purpose:

This step doesn’t produce a direct output but prepares a vector database (db) that can be queried for retrieving relevant text chunks.

This preprocessing pipeline is essential for tasks like:

A well-designed prompt ensures the language model generates accurate and contextually relevant answers. Here is the prompt template:

Prompt templates standardize the input to the language model, ensuring consistent responses across different queries. This is particularly important for domain-specific tasks where precision and clarity are paramount.

Combine the vector store and prompt template to build a retrieval-based QA system:

Test the QA chain with a query:

Expected Output:

To enable Giskard’s evaluation and testing functionalities, wrap the QA chain:

Create a dataset of example queries for testing:

The model generates context-aware answers to each query based on the IPCC report.

Run Giskard’s scan to detect issues:

This scan identifies vulnerabilities such as:

Save the report for further analysis or sharing.

Giskard can generate test suites from the scan:

Automated test suites enable continuous validation of model quality during development.

This guide demonstrated how to:

---------------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI implementation.Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

* Giskard: For AI evaluation and testing.
* LangChain: For building composable language model pipelines.
* FAISS: For efficient similarity search and clustering.
* PyPDFLoader: For processing PDF documents.

* PyPDFLoader: Downloads and processes the IPCC PDF report into text format.
* RecursiveCharacterTextSplitter: Splits the document into smaller chunks (1000 characters) with overlaps to preserve context.
* FAISS: Converts these chunks into a searchable vector database using OpenAI embeddings.

* Document search engines.
* Legal document analysis.
* Summarization of extensive reports.

* RetrievalQA: Retrieves relevant chunks from the vector database (db) and passes them to the language model (llm) for generating an answer.
* OpenAI’s gpt-4o: The underlying language model for generating responses.

* "Sea level rise is largely unavoidable due to current warming levels. It will continue for centuries, though mitigation efforts can slow the rate."

* model_predict: Converts the QA chain into a callable function.
* Giskard wrapper: Adds metadata like model type and description for effective testing.

* Hallucinations (unsupported claims).
* Bias in responses.
* Security weaknesses.

* Experiment with different datasets and document types.
* Customize test suites to align with specific domain requirements.
* Explore Giskard’s advanced features for large-scale model validation.

* Giskard Documentation
* LangChain Documentation
* FAISS Documentation
* OpenAI API Documentation
* Giskard Build Fast With AI NoteBook

1. How to set up and configure Giskard for your AI workflows.
2. The process of building a domain-specific AI model integrated with LangChain.
3. Techniques to detect vulnerabilities, including bias and hallucinations, in AI systems.
4. The steps to automate testing and ensure compliance and quality.

1. Set up Giskard and related libraries for AI evaluation.
2. Build a robust QA system using LangChain and OpenAI models.
3. Evaluate and enhance the system’s reliability using Giskard’s scanning and testing tools.

```
db
```

```
db
```

```
llm
```

```
gpt-4o
```

```
model_predict
```

