---
title: Langfuse: Open Source LLM Engineering Platform
date: January 13, 2025
url: https://www.buildfastwithai.com/blogs/langfuse-open-source-llm-engineering-platform
---

# Langfuse: Open Source LLM Engineering Platform

### Introduction

### Getting Started with Langfuse

### Building with Langfuse: Core Features

### Integrating Langfuse with LangChain

### Conclusion

### Resources

#### Setup and Installation

#### Configuring API Keys

#### 1. Managing Prompts with Langfuse

#### 2. Retrieving and Compiling Prompts

#### 3. Functional Summarization with Langfuse

#### Setting Up the Integration

#### Key Takeaways:

##### Explanation:

How do you become an AI innovator? Start with the right guide, and this is your first step.

Join Build Fast with AI’s Gen AI Launch Pad 2025—a 6-week program designed to empower you with the tools and skills to lead in AI innovation.

Large Language Models (LLMs) like OpenAI's GPT have transformed the way we interact with AI, offering tools to create dynamic, intelligent applications. However, the development, debugging, and management of these applications can be challenging. Enter Langfuse: an open-source platform designed to simplify LLM engineering through tools for tracing, prompt management, and evaluation.

Langfuse provides a streamlined approach to managing LLM-driven projects by enabling developers to efficiently version, debug, and analyze prompts and model behavior. This blog will guide you through using Langfuse, explaining its features with practical code examples, real-world applications, and best practices for maximizing its potential.

By the end of this blog, you will:

To get started, you’ll need to install Langfuse and a few related libraries. Langfuse supports integration with OpenAI models and other LLM frameworks. Install the necessary packages as follows:

Langfuse requires API keys for authentication and integration. Here’s how to set up:

Explanation:

Real-world Use Case: Applications requiring API-heavy tasks, such as interactive chatbots or text summarizers, benefit greatly from Langfuse’s credential management.

Langfuse simplifies prompt management by enabling developers to create, modify, and version prompts programmatically.

Define a Prompt

Here’s an example of creating a prompt for summarizing stories:

Expected Output:

Langfuse stores the prompt for reuse and versioning, making it easier to manage changes.

Real-world Use Case:

For applications like automated content generation or knowledge extraction, prompt management ensures consistency across different iterations.

Langfuse allows developers to retrieve and compile the latest version of a prompt dynamically.

Explanation:

Expected Output:

Real-world Use Case:

Dynamic prompt compilation is ideal for chatbots or other interactive systems where input variables change frequently.

Using the managed prompt, let’s build a function to summarize stories programmatically:

Explanation:

Expected Output:

Given a story input, the function generates a structured JSON output:

Output:

Real-world Use Case:

This function is ideal for summarizing user-generated content, news articles, or creative stories in applications requiring structured data.

Langfuse provides seamless integration with LangChain for enhanced tracing and prompt management in AI workflows.

Explanation:

Real-world Use Case:

Combine Langfuse with LangChain for projects involving multi-step LLM interactions, where traceability and debugging are crucial.

Langfuse revolutionizes LLM engineering with its comprehensive tools for prompt management, debugging, and tracing. Whether optimizing chatbot responses or building advanced AI workflows, Langfuse simplifies the process while ensuring consistent, high-quality outputs.

---------------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI implementation.Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

* Understand Langfuse’s core functionalities.
* Learn how to integrate Langfuse into your LLM projects.
* See how to manage prompts, evaluate outputs, and build robust applications with ease.

* The environment variables LANGFUSE_PUBLIC_KEY and LANGFUSE_SECRET_KEY authenticate your Langfuse access.
* OPENAI_API_KEY integrates OpenAI models for prompt execution.

* create_prompt: Defines and stores a prompt in Langfuse.
* config: Specifies model settings and the JSON schema for output.

* get_prompt: Retrieves the current version of the specified prompt.
* compile: Dynamically replaces placeholders (e.g., {{json_schema}}) with provided values.

* summarize_story: Leverages Langfuse’s managed prompts and OpenAI’s API to process and summarize stories.
* langfuse_prompt: Tracks prompt usage for debugging and improvement.

* CallbackHandler: Enables tracing and logging in LangChain workflows.
* auth_check: Confirms proper configuration of Langfuse credentials.

* Langfuse simplifies prompt versioning and debugging.
* Integration with OpenAI and LangChain enables scalable, traceable applications.
* Real-world applications range from content summarization to interactive event planning.

* Langfuse Documentation
* LangChain Official Site
* OpenAI API
* JSON Schema
* Langfuse Build Fast With AI NoteBook

1. Retrieve your keys: Sign up and get your project keys from Langfuse Cloud.
2. Set up keys in your environment:

```
LANGFUSE_PUBLIC_KEY
```

```
LANGFUSE_SECRET_KEY
```

```
OPENAI_API_KEY
```

```
create_prompt
```

```
config
```

```
get_prompt
```

```
compile
```

```
{{json_schema}}
```

```
summarize_story
```

```
langfuse_prompt
```

```
CallbackHandler
```

```
auth_check
```

