---
title: Streamlit in Google Colab
date: January 23, 2025
url: https://www.buildfastwithai.com/blogs/streamlit-in-google-colab
---

# Streamlit in Google Colab

## What You’ll Learn:

## 1. Getting Started: Setting Up Streamlit in Google Colab

## 2. Building an OpenAI-Powered Chatbot

## 3. Fetching Public IP Address

## 4. Deploying Apps with LocalTunnel

## 5. LangChain-Powered Text Summarization App

## Conclusion:

## Resources:

## Resources and Community

### Installation Steps:

### Explanation of Installed Libraries:

### Overview:

### Code for the Chatbot App:

### Key Features Explained:

### Expected Output:

### Real-World Applications:

### Command:

### Explanation:

### Expected Output:

### Command:

### Detailed Steps:

### Expected Output:

### Overview:

### Code for Summarization App:

### Key Features:

Are you stuck waiting for the right time, or will you make now the right time?

Gen AI Launch Pad 2025 is your answer.

In this blog, we will cover:

By the end of this guide, you’ll be able to build and deploy interactive web apps directly from Colab, leveraging the power of Python, Streamlit, and various advanced libraries.

Streamlit’s intuitive design allows developers to focus on functionality without worrying about front-end development. To get started, you first need to prepare your Colab environment by installing the necessary libraries.

Run the following command in your Colab notebook to install Streamlit and other essential packages:

Once these packages are installed, you’re ready to start coding your apps.

One of the most exciting applications of Streamlit is building chatbots. By integrating OpenAI’s GPT models, you can create conversational apps that answer questions, provide recommendations, or even assist with creative tasks.

Here’s the complete code to build a chatbot using Streamlit and OpenAI:

After running the app, users will see:

Before deploying your app, it’s essential to know your Colab environment’s public IP address. This helps with debugging and access configuration.

This command fetches your public IP address from the icanhazip.com service.

A single line displaying your public IP address, e.g., 35.234.33.244.

To make your Streamlit apps accessible on the web, use LocalTunnel. This tool creates a secure tunnel from your Colab environment to the internet.

LocalTunnel will generate a unique public URL that redirects to your app, e.g., https://example.loca.lt.

This app allows users to input large blocks of text and receive concise summaries, leveraging LangChain’s advanced text processing capabilities.

Streamlit in Colab enables developers to quickly prototype and deploy interactive web applications. Whether building a chatbot, summarization tool, or search-enabled app, the possibilities are endless. By combining the power of Streamlit, LangChain, and OpenAI, you can create scalable, impactful solutions in record time.

---------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI implementation.Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

---------------------------

Join our community of 12,000+ AI enthusiasts and learn to build powerful AI applications! Whether you're a beginner or an experienced developer, this tutorial will help you understand and implement AI agents in your projects.

* How to set up Streamlit in Google Colab
* Building interactive web applications using Streamlit
* Creating an OpenAI-powered chatbot
* Developing a text summarization tool with LangChain
* Incorporating web search functionality into your applications
* Deploying your Streamlit apps using LocalTunnel

* Streamlit: The backbone of our web application, enabling us to create interactive UIs.
* LangChain-Community: A library designed to simplify the integration of large language models and AI workflows.
* Tiktoken: Optimized tokenizer for handling input text for OpenAI models.
* DuckDuckGo Search: Facilitates web search functionality directly from the app.

* A sidebar to enter their OpenAI API key.
* A chat interface where they can input queries and receive AI-generated responses.

* Customer support bots
* Interactive teaching assistants
* Personal productivity tools

* Input Area: Users can paste text for summarization.
* LangChain Integration: Uses LangChain’s efficient summarization chains.
* Dynamic Results: Displays summaries in real time.

* Streamlit Documentation
* OpenAI API Reference
* LangChain Documentation
* LocalTunnel
* Colab Documentation
* Streamlit + Collab Experiment Notebook

* Website: www.buildfastwithai.com
* LinkedIn: linkedin.com/company/build-fast-with-ai/
* Instagram: instagram.com/buildfastwithai/
* Twitter: x.com/satvikps
* Telegram: t.me/BuildFastWithAI

1. Sidebar Input: Users can securely input their OpenAI API key.
2. Session State: Maintains a conversation history for dynamic interactions.
3. Chat Interface: Displays user queries and AI responses in a structured format.

1. Run the Streamlit Server: Starts the app locally on port 8501.
2. LocalTunnel Command: Exposes the local server to a public URL.

```
icanhazip.com
```

```
35.234.33.244
```

```
8501
```

```
https://example.loca.lt
```

