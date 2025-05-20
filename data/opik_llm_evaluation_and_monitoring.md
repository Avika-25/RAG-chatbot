---
title: Opik: LLM Evaluation and Monitoring
date: January 13, 2025
url: https://www.buildfastwithai.com/blogs/opik-llm-evaluation-and-monitoring
---

# Opik: LLM Evaluation and Monitoring

### Introduction

### Key Features of Opik

### 1. Setup and Installation

### 2. Preparing the Environment

### 3. Logging Traces

### 4. Enhancing Functionality with Decorators

### 5. Evaluating LLM Outputs

### Conclusion

### Resources

#### Code:

#### Explanation:

#### Application:

#### Code:

#### Explanation:

#### Application:

#### Code:

#### Expected Output:

#### Explanation:

#### Application:

#### Code:

#### Expected Output:

#### Explanation:

#### Application:

#### Example Metric: Hallucination

#### Expected Output:

#### Explanation:

#### Application:

#### Additional Metrics:

The best time to start with AI was yesterday. The second best time? Right after reading this post. The fastest way? Gen AI Launch Pad’s 6-week transformation.

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

In the era of AI-driven innovation, Large Language Models (LLMs) have become essential tools for diverse applications, ranging from content generation to complex decision-making. However, ensuring the reliability, performance, and accuracy of LLMs in production environments remains a challenge. Enter Opik: an open-source platform developed by Comet to evaluate, test, and monitor LLM applications effectively.

In this blog post, we will explore how to use Opik for tracing, evaluation, and production monitoring of LLMs. By the end, you’ll have a thorough understanding of its features, setup, and practical applications. Additionally, we will dive deep into its key metrics and how they can provide actionable insights to improve your LLM workflows.

Getting started with Opik is straightforward. With just a few commands, you can have the platform ready to enhance your LLM workflows.

Use this setup in any Python environment, such as Jupyter Notebook or Google Colab, to get started with Opik.

To ensure smooth interaction with LLMs, Opik requires an OpenAI API key. The following script securely configures your environment.

This setup is crucial for environments where OpenAI’s API is used, ensuring secure and consistent access.

Opik’s tracing functionality records all interactions with the LLM, making it easier to analyze and debug outputs. Let’s explore how to enable and utilize this feature.

Use this feature to debug, track, and analyze how your LLM responds to various inputs. Developers can use trace logs to understand input-output relationships and fine-tune their models.

The @track decorator simplifies logging for functions interacting with LLMs, automating trace capture for function calls and outputs.

Ideal for modular applications where multiple functions interact with LLMs. Use this to maintain clean, traceable code that is easy to debug and extend.

Opik provides robust metrics to assess the quality of LLM responses. Here are some examples:

Use this metric to ensure the factual correctness of LLM-generated content, especially in high-stakes domains like healthcare or legal advice.

Opik is a powerful tool that bridges the gap between development and production for LLM applications. Its capabilities—ranging from trace logging to evaluation—empower developers to build reliable, efficient, and high-performing AI systems. By leveraging Opik’s metrics, developers can gain deeper insights into their models and optimize them for real-world applications.

To deepen your understanding, explore the following resources:

--------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI implementation.Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

* The first line ensures the latest versions of opik and openai libraries are installed.
* opik.configure(use_local=False) sets up Opik to operate without relying on local configurations, enabling cloud-based integration.

* userdata.get("OPENAI_API_KEY") retrieves the API key stored in your Google Colab environment.
* If the API key is unavailable, getpass prompts the user to enter it manually.
* os.environ stores the API key as an environment variable for secure access.

* track_openai(client) integrates Opik’s tracing capabilities with the OpenAI client.
* The prompt and completion objects simulate a typical interaction with an LLM.
* All traces are logged under the project name "openai-integration-demo" for further analysis.

* The @track decorator simplifies trace logging by automatically capturing function inputs, outputs, and execution details.
* Functions like generate_story and generate_topic showcase how modularization can enhance reusability and clarity.

* The hallucination metric evaluates if the LLM output introduces inaccuracies or fabrications.
* In this case, the output "Paris" aligns with general knowledge and context, resulting in a low hallucination score.

* Answer Relevance: Assesses how well the LLM’s response aligns with the input query.
* Context Precision: Evaluates the relevance and conciseness of the output concerning the provided context.

* Opik Documentation
* OpenAI API Documentation
* GitHub Repo for Opik
* Further Reading on LLM Monitoring
* OpenAI Tutorials

1. Tracing: Tracks all LLM calls during development and production, enabling better debugging and analysis.
2. Evaluation: Automates the evaluation process using datasets and experiments, providing insights into model performance.
3. Production Monitoring: Logs production traces and tracks key metrics like feedback scores, trace counts, and token usage over time.

```
opik
```

```
openai
```

```
opik.configure(use_local=False)
```

```
userdata.get("OPENAI_API_KEY")
```

```
getpass
```

```
os.environ
```

```
track_openai(client)
```

```
prompt
```

```
completion
```

```
@track
```

```
@track
```

```
generate_story
```

```
generate_topic
```

