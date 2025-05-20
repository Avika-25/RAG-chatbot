---
title: Guidance: Structured LLM Generation
date: January 10, 2025
url: https://www.buildfastwithai.com/blogs/guidance-structured-llm-generation
---

# Guidance: Structured LLM Generation

### Introduction

### Detailed Explanation

### Conclusion

### Resources

#### Join Build Fast with AI’s Gen AI Launch Pad 2025—a 6-week transformation program designed to accelerate your AI mastery and empower you to build revolutionary applications.

#### Setting Up Guidance

#### Simple Generation

#### Making Decisions with select

#### Interleaved Generation and Control

#### Regex-Guided Output

#### Multistep Interaction

The best time to start with AI was yesterday. The second best time? Right after reading this post.

Large Language Models (LLMs), such as OpenAI's GPT series, have significantly advanced natural language processing, enabling sophisticated applications across industries. Yet, conventional methods like fine-tuning and prompt engineering can pose challenges, including increased costs, latency, and a lack of precise control over output structure.

Guidance emerges as a game-changer, offering a programming paradigm designed to enhance interaction with LLMs. With features like structured generation, output constraints, and dynamic control logic, Guidance allows developers to optimize performance while reducing operational complexities.

This blog delves into the capabilities of Guidance, providing a step-by-step walkthrough of its features, practical applications, and advanced techniques. By the end, you'll have the tools and knowledge to:

To begin, ensure your environment is configured correctly. Install the necessary libraries and set up your API key.

What this does:

Why it matters: Setting up this environment ensures seamless integration with GPT models, laying the foundation for advanced use cases.

Where to apply: This setup is essential for projects requiring structured LLM interactions, such as chatbots, decision-making systems, or custom workflows.

A straightforward way to generate responses is by appending a query to a model instance.

Explanation:

Expected Output:

Use Case: Ideal for single-turn Q&A systems, basic chatbot applications, or quick information retrieval.

Pro Tip: Experiment with varying query structures to understand how phrasing impacts the model’s responses.

Guidance introduces the ability to choose between predefined alternatives, enabling dynamic responses based on user input.

Explanation:

Expected Output:

Applications: This is particularly useful for scenarios like:

Guidance excels in blending logic with text generation, enabling sophisticated control over outputs. Here’s an example:

Explanation:

Expected Output:

Applications: Build chatbots or assistants that adaptively handle queries based on their complexity or the availability of information.

Regex constraints ensure outputs adhere to specific formats, which is invaluable for structured data generation.

Explanation:

Expected Output: A rephrased proverb, properly formatted with new chapter and verse references.

Applications:

Pro Tip: Experiment with more complex regex patterns to enforce advanced constraints.

Here’s how Guidance can handle multistep processes with conditional branching:

Explanation:

Expected Output:

Applications: Use this approach for research, consulting, or expert-driven content creation.

Guidance transforms the way developers interact with LLMs, offering unparalleled control and flexibility. By mastering its tools—from regex constraints to dynamic workflows—you can unlock new possibilities in text generation while optimizing for efficiency and cost.

---------------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI implementation.Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

* Efficiently interact with LLMs.
* Control and constrain model outputs.
* Implement multistep workflows for complex tasks.
* Apply Guidance in real-world scenarios with confidence.

* guidance: The main library enabling structured LLM interactions.
* gpustat: Tracks GPU usage, useful for monitoring resource consumption in high-performance tasks.
* llama-cpp-python: Provides integration with LLaMA models for additional flexibility.
* OPENAI_API_KEY: Authenticates your session with OpenAI's API.

* The + operator combines the model instance (gpt4) with the query string.
* The model processes the query and generates a response.

* A specific answer detailing the winner of the Kentucky Derby and the margin of victory.

* select: Allows the model to choose between predefined options.
* The variable choice stores the model’s selection, influencing subsequent actions.

* If the model chooses “SEARCH”: It indicates the need for external input.
* If it chooses “RESPOND”: It directly generates an answer.

* Decision trees in interactive chatbots.
* Routing logic in customer support systems.
* Dynamic branching workflows.

* guidance decorator: Marks the function as a Guidance-enabled workflow.
* gen: Dynamically generates text with defined constraints (e.g., stop="Q:").
* Conditional logic determines whether to defer to external resources or generate a direct response.

* For “SEARCH”: A suggestion to consult external sources.
* For “RESPOND”: A complete answer.

* regex: Ensures generated outputs match specific patterns (e.g., numerical values for chapter and verse).
* The gen function dynamically generates text adhering to these constraints.

* Academic citations.
* Template-based text generation.
* Ensuring data consistency in structured datasets.

* Context Blocks:
* system: Provides initial setup or context.
* user: Captures user queries or instructions.
* assistant: Generates responses based on the above inputs.
* gen: Dynamically generates expert recommendations and a collaborative response.

* A list of three world-class experts.
* A nuanced answer reflecting diverse perspectives.

* Guidance Documentation
* OpenAI GPT API
* Regex Cheat Sheet
* Guidance Gpustat Build Fast With AI NoteBook

```
guidance
```

```
gpustat
```

```
llama-cpp-python
```

```
OPENAI_API_KEY
```

```
+
```

```
gpt4
```

```
select
```

```
select
```

```
choice
```

```
guidance
```

```
gen
```

```
stop="Q:"
```

```
regex
```

```
chapter
```

```
verse
```

```
gen
```

```
system
```

```
user
```

```
assistant
```

```
gen
```

