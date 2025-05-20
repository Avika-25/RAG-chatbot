---
title: They're Building Apps in Seconds — You're Still Writing Loops
date: February 27, 2025
url: https://www.buildfastwithai.com/blogs/claude-3-7-sonnet
---

# They're Building Apps in Seconds — You're Still Writing Loops

## Introduction

## Key Features of Claude 3.7 Sonnet

## Claude 3.7 Sonnet Performance

## 'Claude Code' — The New CLI Coding Assistant

## How to Access Claude 3.7 Sonnet

## Why is this such a big deal?

## Final Thoughts

## Resources and Community

### 1. Extended Thinking Mode

### 2. Larger Output Capacity

### 3. Improved Coding Abilities

### 4. Reduced Unnecessary Refusals

### 5. Claude Code

### Coding Performance

### Reasoning Performance

### Reasoning Performance

### Claude 3.7 Sonnet Pricing

Are you willing to risk being left behind, or will you take action?

Join Gen AI Launch Pad 2025 and be the future.

Anthropic just launched its most intelligent AI model to date and the first hybrid reasoning model on the market—Claude 3.7 Sonnet. The hybrid part means the model works both as a reasoning model and a large language model (LLM).

While OpenAI recently announced that GPT-5 will be a unified model, Anthropic has already introduced Claude 3.7 Sonnet, which is capable of both quick responses and deeper reasoning, getting ahead in this particular approach to AI development.

This new model can "think" about questions for as long as the users ask it to, so depending on how long it considers things, its responses could be very different.

Claude 3.7 Sonnet can also build complex apps with a single prompt, and with the introduction of a new product called Claude Code, developers can now give substantial engineering tasks to Claude directly from their terminal.

Claude 3.7 Sonnet brings several important features that set it apart from previous models and other AI systems on the market:

Perhaps the most notable feature is the extended thinking capability. Unlike most AI models that give instant responses, Claude 3.7 Sonnet can take time to "think" before answering questions. This thinking process is visible to users, making the AI's reasoning more transparent.

When using the API, users can control exactly how much thinking the model does. You can tell Claude to think for a specific number of tokens, up to its output limit of 128K tokens. This allows you to balance speed and cost against the quality of answers.

Here's an example Typescript code for extended thinking:

The API response will include both thinking and text content blocks:

For people who need higher accuracy, especially on complex topics like math, physics, or coding, the extended thinking mode makes a big difference. The model can work through problems step by step, similar to how humans think, which leads to more reliable answers.

Claude 3.7 Sonnet supports up to 128K output tokens (in beta), which is over 15 times longer than before. This is very useful for:

This expanded capacity means the model can handle much more complex tasks without running into token limits.

As a developer, this is what I am most excited about. The model shows major improvements in coding across many areas:

Several tech companies like Cursor, Cognition, Vercel, and Replit have already tested Claude 3.7 Sonnet and found it performs better than other models for real-world coding tasks.

According to Anthropic, Claude 3.7 Sonnet makes more careful distinctions between harmful and harmless requests, reducing unnecessary refusals by 45% compared to earlier models. This helps the AI be more helpful without constantly blocking reasonable requests.

This is huge because one of the reasons that I have used Claude less and less in the past couple of months is the high frequency of refusals. It was an annoying feature to be honest.

Claude Code is a brand new command line tool for what Anthropic calls "agentic coding." Currently available as a limited research preview, it allows developers to give substantial engineering tasks to Claude directly from their terminal.

The tool acts as a coding partner that can:

In early testing, they found Claude Code could complete tasks in a single pass that would normally take 45+ minutes of manual work, cutting down development time.

Claude Code is currently available as a limited research preview. Developers interested in trying it would need to join the preview program.

The performance of Claude 3.7 Sonnet shows significant improvements over previous models in several key areas:

Claude 3.7 Sonnet has shown impressive results on coding benchmarks and real-world tests. It achieves state-of-the-art performance on SWE-bench Verified, which evaluates AI models' ability to solve real-world software issues.

Anthropic also shared how Claude 3.7 Sonnet achieves state-of-the-art performance on TAU-bench, a framework that tests AI agents on complex real-world tasks with user and tool interactions.

The company says their goal with Claude Code is to better understand how developers use Claude for coding, which will help them make future model improvements.

The extended thinking mode makes Claude 3.7 Sonnet much better at tasks that need careful reasoning:

This reasoning capability puts Claude 3.7 Sonnet in a new category of AI models that can think more deeply about problems rather than just generating text based on patterns.

This one had me particularly excited.

Claude Code is a command -line tool Anthropic introduced that basically lets you interact with Claude 3.7 through your terminal for coding tasks​.

In other words, Claude can now act like a developer's assistant who can edit files, run tests, debug code and even commit to GitHub — all via CLI commands you give it.

Imagine saying

"Hey Claude, open my app.js and optimize the search function"

and it just does it.

Or asking Claude to run your test suite and fix any failing tests it finds. It's like having a super-intelligent junior developer who never gets tired.

I tried a simple scenario where, I let Claude Code suggest a refactor in one of my Python scripts and it not only provided the updated code but actually executed it to verify it worked (under my supervision, of course).

I have used the windsurf and they now added this claude 3.7 model for paid user.

It feels a bit like sci-fi to have an AI directly manipulating code on my machine.

Do note, Claude Code is in limited preview right now​ but not everyone has access yet — and it works under human oversight (thankfully!).

So you still have to review and approve its changes (no skynet scenarios… yet).

But as a glimpse of the future of AI-assisted development it's incredibly promising.

Claude 3.7 Sonnet is now available on both the Claude website and through API access. To access it via a chat interface, you can try the following channels:

Simply switch to Claude 3.7 Sonnet from the model dropdown.

All Claude plans can access the model, including Free, Pro, Team, and Enterprise. However, the extended thinking mode is only available for paid plans (Pro, Team, and Enterprise).

Developers can also access Claude 3.7 Sonnet through:

When using the API, developers have full control over the model's thinking budget, allowing them to specify how many tokens the model can use for thinking.

Here's a sample API call using Typescript:

As I mentioned, Claude 3.7 Sonnet is included in the free tier account on claude.ai but without the extended thinking mode. You can also choose to upgrade your account to either the Pro ($20 per month) or Team ($30 per month).

Claude 3.7 Sonnet keeps the same pricing as previous models:

This pricing includes thinking tokens when using the extended thinking mode. For API users, there are options for cost savings:

For me as a developer, having a more powerful AI model means I can have more confidence that it'll have better awareness of my project's code base and is more capable of generating more secure and more complete code.

The ability to understand context across an entire codebase is particularly valuable. Previous models often lost track of how different parts of a project fit together, but Claude 3.7 Sonnet seems to maintain a more cohesive understanding of large projects.

For researchers, the deep thinking capability of this model means there's less chance of hallucinations, and it actually generates more meaningful and factual answers. The visible reasoning process also helps researchers understand how the model reached its conclusions, which is important for trust and verification.

For casual users, the responses from this new model are actually more reliable and less robotic. The longer context window and improved reasoning lead to conversations that feel more natural and helpful.

For AI developers, claude-3.7-sonnet and claude-3.7–sonnet-thinking are now supported in Cursor!

Here's how you can switch to the new models in Cursor.

I plan to do some testing and build sample apps to see how well the new Claude models handle app generation on Cursor. This will give me a better sense of their real-world capabilities beyond the benchmarks.

I was surprised to see Anthropic drop Claude 3.7 Sonnet out of the blue (or maybe I wasn't paying so much attention on the leaks). I was actually expecting Claude 3.5 Opus to be released first but it seems that they have scrapped that model already.

Now, it's clear that big tech companies are racing to release the best AI model with reasoning capabilities. It's only been weeks since DeepSeek released R-1, then xAI launched Grok 3 with reasoning capabilities, and now we got Claude 3.7 Sonnet. It's honestly a bit overwhelming and I don't even know if the benchmarks from these tech companies are actually reliable.

What I am most excited about is the integration of Claude 3.7 Sonnet in coding tools like Cursor. I can't wait to test it out by building more complex applications, and also learn more about the Claude Code which is also very interesting.

For developers especially, the improvements in coding abilities and the introduction of Claude Code could change how we work. Having an AI that can understand large codebases and handle substantial engineering tasks could free us to focus on more creative aspects of development.

While I'm cautious about some of the claims being made, Claude 3.7 Sonnet does point to a future where AI works alongside humans as a true thinking partner rather than just a fancy autocomplete tool. I'll be testing it extensively to see if it lives up to the hype.

---------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI Implementation. Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

---------------------------

Join our community of 12,000+ AI enthusiasts and learn to build powerful AI applications! Whether you're a beginner or an experienced developer, this tutorial will help you understand and implement AI agents in your projects.

* Complex code generation
* Detailed planning documents
* Long-form writing
* Handling large data analysis tasks

* Planning and solving complex coding tasks
* Handling full-stack updates
* Working with complex codebases
* Building sophisticated web apps and dashboards from scratch
* Producing production-ready code with fewer errors

* Search and read code
* Edit files
* Write and run tests
* Commit and push code to GitHub
* Use command-line tools
* Keep you informed at each step

* Math and science problems show notable improvement
* Complex planning tasks benefit from the step-by-step thinking process
* Instruction-following becomes more precise
* The model makes fewer errors on tasks that need several steps of reasoning

* Web browser interface
* iOS app
* Android app

* Anthropic API
* Amazon Bedrock
* Google Cloud's Vertex AI

* Pro tier: Full access, including extended thinking mode
* Team and Enterprise plans: Full access with additional features for organizations

* $3 per million input tokens
* $15 per million output tokens

* Up to 90% cost savings with prompt caching
* 50% cost savings with batch processing

* Website: www.buildfastwithai.com
* LinkedIn: linkedin.com/company/build-fast-with-ai/
* Instagram: instagram.com/buildfastwithai/
* Twitter: x.com/satvikps
* Telegram: t.me/BuildFastWithAI

```
app.js
```

```
claude-3.7-sonnet
```

```
claude-3.7–sonnet-thinking
```

