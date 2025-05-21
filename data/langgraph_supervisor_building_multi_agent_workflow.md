---
title: LangGraph-Supervisor: Building Multi-Agent Workflows
date: March 10, 2025
url: https://www.buildfastwithai.com/blogs/langgraph-supervisor-building-multi-agent-workflows
---

# LangGraph-Supervisor: Building Multi-Agent Workflows

## Introduction

## Step 1: Install Dependencies

## Step 2: Import Required Libraries

## Step 3: Initialize the AI Model

## Step 4: Define AI Agent Functions

## Step 5: Create AI Agents

## Step 6: Create the Supervisor Workflow

## Step 7: Running the Workflow

## Step 8: Adding Memory to Supervisor

## Conclusion

## References

## Resources and Community

### Key Takeaways:

Do you want to be remembered as someone who waited or someone who created?

Gen AI Launch Pad 2025 is your platform to innovate.

Artificial intelligence (AI) workflows often require multiple agents to collaborate on different tasks, such as research, calculations, or creative content generation. LangGraph-Supervisor simplifies the creation of hierarchical multi-agent systems, allowing a central supervisor agent to manage task delegation and communication between specialized agents efficiently.

In this tutorial, we will:

By the end, you'll have a functional system where AI agents collaborate effectively, improving automation in your applications.

Before we start coding, ensure you have LangGraph-Supervisor and LangChain installed. You can install them using pip:

Also, set up your OpenAI API key:

This ensures your AI models can interact with OpenAI’s services.

Now, import the necessary libraries:

We will use ChatOpenAI as the underlying AI model and create specialized AI agents with LangGraph-Supervisor.

Define the AI model that our agents will use:

This model will power the agents responsible for different tasks in our system.

Our multi-agent system will include a math expert and a research expert. First, define the functions these agents will use:

Now, create the specialized agents:

These agents are designed to focus on their respective tasks without overlapping responsibilities.

The supervisor agent will manage communication between the specialized agents:

The supervisor dynamically delegates tasks based on user input.

Compile and execute the workflow:

This process:

To make the workflow remember previous interactions, we introduce memory:

This allows agents to recall past queries and maintain context over multiple interactions.

By following this tutorial, you’ve built a multi-agent system where a supervisor agent effectively delegates tasks between a math expert and a research expert. With LangGraph-Supervisor, complex AI workflows become more structured and efficient.

---------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI Implementation. Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

---------------------------

Join our community of 12,000+ AI enthusiasts and learn to build powerful AI applications! Whether you're a beginner or an experienced developer, our resources will help you understand and implement Generative AI in your projects.

* Set up LangGraph-Supervisor and its dependencies.
* Create AI agents for different tasks.
* Implement a supervisor agent to orchestrate them.
* Run and test the multi-agent workflow.

* LangGraph-Supervisor simplifies multi-agent coordination.
* AI agents specialize in specific tasks, improving efficiency.
* The supervisor agent dynamically routes tasks based on user input.
* Adding memory enhances AI interaction capabilities.

* Website: www.buildfastwithai.com
* LinkedIn: linkedin.com/company/build-fast-with-ai/
* Instagram: instagram.com/buildfastwithai/
* Twitter: x.com/satvikps
* Telegram: t.me/BuildFastWithAI

1. The supervisor agent receives the user request.
2. It delegates the request to the math expert.
3. The math expert processes the request and returns the result.
4. The supervisor presents the final response.

1. LangGraph Documentation
2. LangChain Supervisor GitHub
3. LangChain Official Website
4. LangGraph-Supervisor Experiment Notebook

