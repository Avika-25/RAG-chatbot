---
title: Instructor: The Most Popular Library for Simple Structured Outputs
date: December 19, 2024
url: https://www.buildfastwithai.com/blogs/instructor-the-most-popular-library-for-simple-structured-outputs
---

# Instructor: The Most Popular Library for Simple Structured Outputs

## Introduction

## Why Use Instructor?

## Installation

## Setting Up API Keys

## Importing Libraries

## Creating a Structured Data Model

## Error Handling

## Conclusion

## Resources

### Troubleshooting Installation Issues

### How to Obtain API Keys

### Security Tips

### What is Pydantic?

### Key Features of Pydantic

### Example of Pydantic Model

### Output:

### Why Use Pydantic with Instructor?

### Why Use Structured Models?

### Example of Error Handling

### Output:

### Key Takeaways:

You’re not just reading about AI today — you’re about to build it."

"Don’t just watch the future happen — create it. Join Gen AI Launch Pad 2024 and turn your curiosity into capability before the AI wave leaves you behind. 🚀"

As AI models like GPT become more powerful and flexible, developers are often faced with a challenge: how do we get structured outputs from large language models (LLMs)? Enter Instructor, a library designed to simplify structured data extraction from LLMs. In this blog post, we'll explore what makes Instructor so effective, break down the code, and understand how you can integrate it with models like OpenAI's GPT and Cohere's models.

Instructor makes it easy to prompt LLMs for structured outputs, such as JSON data. Instead of receiving unstructured text, you can request LLMs to provide responses in the format you need. This is especially useful for:

Instructor abstracts away complexity, enabling you to build robust applications faster. By specifying a schema for the output, you ensure your AI delivers exactly what you need.

First, let's install the necessary libraries. The notebook starts with a simple installation step:

Output:

This installs all necessary packages quietly (without verbose output).

Next, you need API keys for OpenAI and Cohere. The code fetches these from Google Colab's userdata storage:

1.OpenAI API Key:

2.Cohere API Key:

Now, let's import the required libraries:

Pydantic is a powerful data validation and parsing library in Python. It allows you to define schemas (structured models) for your data using Python classes. These schemas ensure that data conforms to the expected format and type, providing a reliable way to validate incoming data and prevent errors. Pydantic is particularly useful when you need to ensure consistency and correctness of data in applications.

Here's an example of a simple pydantic model:

If you provide incorrect data types, Pydantic will raise a validation error:

Output:

When combined with Instructor, Pydantic helps define the structure of the data you expect from an LLM. This means you can:

Instructor uses Pydantic models to guide the LLM in generating consistent, structured outputs, making your applications more reliable and easier to maintain.

Here's an example of how to define a structured output using pydantic and Instructor:

In this example:

This model tells the LLM to output responses matching this structure.

Instructor can gracefully handle errors when the model output doesn't match the expected structure. If the LLM returns an output that doesn't align with the defined pydantic model, Instructor raises a validation error.

This helps ensure your application can handle unexpected outputs gracefully.

The Instructor library is a powerful tool for extracting structured data from large language models like OpenAI's GPT and Cohere's models. By combining the flexibility of LLMs with the precision of pydantic schemas, Instructor allows you to build applications that require consistent, structured outputs with ease.

Whether you're building chatbots, automating data pipelines, or working on enterprise AI solutions, Instructor can help streamline your development process.

---------------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI implementation.Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

* Form Data Extraction: Automating extraction of specific fields from documents.
* APIs & Automation: Structuring data for APIs or downstream processing.
* Enterprise Use-Cases: Tasks that require predictable and structured results.
* Data Pipelines: When you need clean, structured data for analytics or reporting.
* Chatbots and Assistants: Ensuring responses from AI assistants follow a predictable format.

* Instructor: The main library for structured outputs.
* OpenAI: For accessing OpenAI models like GPT-3.5 and GPT-4.
* Cohere: An alternative to OpenAI, providing different LLM capabilities.

* Network Issues: If the installation is slow or fails, check your internet connection.
* Version Conflicts: If you have older versions of libraries installed, update them using pip install --upgrade.
* Environment Issues: Ensure you're working in a clean virtual environment or Colab instance to avoid conflicts.

* Sign up at OpenAI.
* Go to your account settings and generate a new API key.

* Sign up at Cohere.
* Navigate to the API section and generate a new API key.

* Never share your API keys publicly or commit them to repositories.
* Use environment variables or secure storage options to manage keys.

* Instructor: The core library for handling structured outputs.
* OpenAI: For interfacing with OpenAI's models.
* Pydantic: For defining structured data models.

* Enforce Data Integrity: Ensure the LLM’s response conforms to your schema.
* Reduce Errors: Identify and handle invalid outputs gracefully.
* Streamline Processing: Easily integrate structured outputs into your workflows, APIs, and data pipelines.

* WeatherResponse: A pydantic model specifying the desired fields:
* location: Name of the location (string).
* temperature: The temperature in degrees (float).
* condition: The weather condition (string).

* Consistency: Ensures the LLM output follows a predictable structure.
* Error Reduction: Reduces the chances of unexpected or unusable data.
* Easier Parsing: Simplifies downstream processing and integration with APIs or databases.

* Instructor GitHub Repository: Instructor on GitHub
* OpenAI API Documentation: OpenAI Docs
* Cohere API Documentation: Cohere Docs
* Pydantic Documentation: Pydantic Docs
* Instructor Build Fast with AI: NoteBook

1. Type Enforcement: Ensures that data matches specified types, such as str, float, int, or custom types.
2. Validation: Automatically validates data against the defined schema and raises clear error messages if the data is incorrect.
3. Serialization/Deserialization: Converts data between different formats (e.g., JSON to Python objects and vice versa).
4. Nested Models: Supports defining complex schemas with nested data structures.
5. Error Handling: Provides detailed error messages when validation fails, making debugging easier.
6. Automatic Data Parsing: Automatically parses input data, transforming it to the correct types.

1. Ease of Use: Instructor simplifies prompting for structured outputs.
2. Consistency: Ensure predictable results by defining pydantic schemas.
3. Flexibility: Works with both OpenAI and Cohere models.
4. Robustness: Built-in error handling for invalid outputs.

```
pip install --upgrade
```

```
userdata
```

```
str
```

```
float
```

```
int
```

```
pydantic
```

```
pydantic
```

```
WeatherResponse
```

```
pydantic
```

```
location
```

```
temperature
```

```
condition
```

```
pydantic
```

```
pydantic
```

```
pydantic
```

