---
title: Building with LLMs: A Practical Guide to API Integration
date: January 4, 2025
url: https://www.buildfastwithai.com/blogs/building-with-llms-a-practical-guide-to-api-integration
---

# Building with LLMs: A Practical Guide to API Integration

## OpenAI

## Parameters and context window

## Access

## Fine-tuning options

## Pricing

## Gemini by Google DeepMind

## Parameters and context window

## Access

## Fine-tuning options

## Pricing

## Llama by Meta

## Parameters and context window

## Access and deployment

## Fine-tuning

## Pricing

## Claude by Anthropic

## Parameters and context window

## Access and deployment

## Fine-tuning options

## Pricing

## Grok by xAI

## Parameters and context window

## Access and deployment

## Fine-tuning options

## Pricing

## Mistral by Mistral AI

## Parameters and context window

## Access and deployment

## Fine-tuning options

## Pricing

### Stay Updated:

Did you know you can build your SaaS using only an LLM API?

At Gen AI Launch Pad 2024, we teach you how and help bring your idea to life!

Top 8 Large Language Models Comparison

OpenAI released its first GPT model in 2018, and since then, it has set the industry standard for performance in complex language tasks. The LLM remains unrivaled in performance, reasoning skills, and fine-tuning ease. The flagship model so far is the GPT-4o, which has a smaller, faster, and cheaper version called the GPT-4o mini.

OpenAI recently launched the o1 and o1-mini models in beta, focusing on deeper reasoning and complex tasks in science, coding, and math. However, GPT-4o remains more capable for common use cases, as the o1 models lack features like Internet browsing.

Besides LLMs, Open AI represents image models DALL-E and audio models Whisper and TTS. To know more about how they work, read our article on AI image generators and another one explaining sound, music and voice generation.

GPT-4o is estimated to have hundreds of billions of parameters; some sources claim 1.8 trillion, although exact details are proprietary. In both versions, the context window can hold up to 128,000 tokens, which is the equivalent of 300 pages of text.

GPT models are only available as a service in the cloud; you can’t deploy them on-premises. They are accessible via Open AI APIs, using Python, Node.js, and .Net. or through Azure OpenAI Service, which also supports C#, Go, and Java. You can call API with other languages as well, thanks to community libraries.

Below, we’ll list API products offered directly by Open AI.

Chat completions API allows you to quickly embed text generation capabilities into your app, chatbot, or other conversational interface.

Generating prose using Python with the chat completions endpoint. Source: OpenAI Platform

To customize GPT-4o/GPT-4o mini models, you have to prepare a dataset that contains at least 10 conversational patterns, though the OpenAI recommendation is to start with 50 training examples. The dataset for fine-tuning must be in JSON format and up to 1GB in size (though you don’t need a set that large to see improvements.) It can also contain images. To upload the dataset, use Files API or Uploads API for files larger than 512 MB.

Fine-tuning can be performed via OpenAI UI or programmatically, using OpenAI SDK. Azure OpenAI currently supports only text-to-text fine-tuning.

GPT-4o API usage for business costs $2.5 /1M input tokens and $10/1M output tokens, while GPT-4o mini is much cheaper: $0.15/1M input tokens and $0.6/1M output tokens.

O1-preview costs $15.00/1M input tokens and $60.00/1M output tokens.

You can find the detailed pricing information here.

The Gemini (former Bard) model family is optimized for high-level reasoning and understanding not only texts but also image, video, and audio data.

The model's name was inspired by NASA's early moonshot program, breakthrough Project Gemini. It was also associated with the Gemini astrology sign since people born under it are highly adaptable, effortlessly connect with diverse individuals, and naturally view situations from multiple perspectives.

The flagship products are Gemini 1.5 Pro and Gemini 1.5 Flash. Flash is a mid-size multimodal model optimized for a wide range of reasoning tasks. Pro can handle large amounts of data. Both models support over 100 languages.

Estimates suggest Gemini models operates with 1.56 trillion parameters. Gemini 1.5 Pro has an unprecedented context window of two million tokens, which allows it to fit 10 Harry Potter novels (well, existing seven plus fan-dreamed three) in one prompt. Or one Harry Potter movie (2 hours of video) or 19 hours of audio. The Gemini 1.5 Flash’s context window is one million tokens.

Gemini models are cloud-based only. Google provides two ways to access its LLMs — Google AI and Vertex AI (Google’s end-to-end AI development platform). Both APIs support function calling.

Google AI Gemini API ****provides a fast way to explore the LLM capabilities and get started with prototyping and creating simple chatbots. It supports mobile devices and natively connects with Firebase, a Google platform for the development of AI-powered web, iOS, and Android apps. The API can be consumed with Python, Node.js, and Go. SDKs for Flutter, Android, Swift, and JavaScript are recommended for prototyping only. If you want to launch your app written in those languages to production, migrate to Vertex AI.

Vertex AI Gemini API ****allows for building complex, enterprise-grade applications. With Vertex AI, you can leverage a range of additional services, such as MLOps tools for model validation, versioning, and monitoring, an Agent Building console for creating virtual assistants, and security features, critical for the production environment.

Overall, it makes sense to start building your Gemini-based app with Google AI API and, as your project matures, move to Vertex AI API.

With Google AI, fine-tuning is possible for 1.5 Flash and text only. It doesn’t cover chat-style conversations. You can start with a dataset of 20 examples (each no longer than 40,000 characters), but the optimal size is between 100 and 500 examples. Tuned models don’t support JSON inputs and texts longer than 40,000 characters.

Vertex AI supports supervised fine-tuning for 1.5 Flash and Pro using text, image, audio, and document inputs. A dataset of 100 examples (up to 32,000 tokens each) is recommended. Fine-tuning can be done via the Gemini REST API, Google Cloud console, Vertex AI SDK for Python, or Colab Enterprise.

Rates vary based on the model, input type, and prompt size (inputs/outputs over 128k tokens cost twice as much). Text input/output is counted in million tokens or thousand characters (Vertex AI), audio and video inputs—in seconds, and visual inputs—in images.

Google AI Gemini API offers a free tier for testing purposes with limitations of 15 requests/minute, 1500 requests/day, and 1M tokens per minute. Vertex AI provides batch mode with a 50 percent discount.

More details are available on the Google Cloud pricing page.

Llama (short for Large Language Model Meta AI) is a family of open-source, highly customizable language models. The latest release, Llama 3.2, has two collections of models:

All versions work with eight languages: English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai.

Be aware that the EU’s AI Act, which will go into effect in the summer of 2025, сreates regulatory complexity for open-source AI. Llama 3.2 is currently [restricted from the European market](https://slator.com/meta-rolls-out-multimodal-llama-3-2-but-not-in-europe/#:~:text=Not Available in Europe,to concerns over GDPR compliance.) due to concerns about GDPR compliance.

Llama 3.2 offers 1B, 3B, 11B, and 90B parameter models, all with a 128,000-token context length. The 11B and 90B models include vision capabilities for image analysis, graph interpretation, and geographical queries.

Llama can be deployed on-premises, which gives companies control over data security and privacy. The models are available for download on llama.com and Hugging Face.

In September 2024, Meta presented the Llama Stack, the company’s first framework for efficiently deploying Llama models across various environments: on-premises, in cloud, and on local devices.

It contains a set of APIs, such as

Client SDKs for working Llama Stack include Python, Node, Swift, and Kotlin, among others.

Also, companies can access Llama on multiple partner platforms, such as AWS (via Amazon Bedrock, a service that offers a choice of models via a single API), Databricks, Dell, Google Cloud, Grok, IBM, Intel, Microsoft Azure, NVIDIA, Oracle Cloud, Snowflake, and more.

You can customize your Llama model using different environments. Below are several options.

Learn more about Llama fine-tuning from the official documentation here.

Llama is open-source but still governed by a license that restricts its use in certain cases. Businesses with over 700 million active users monthly must contact Meta for special licensing. Downloading Llama is free. However, to utilize it as a service, you’ll have to pay the chosen cloud provider or API platform, and the price will depend on many factors and additional features offered by the vendor.

For example, Amazon Bedrock’s pricing depends on the region: North America is split into two price zones, Europe into three. In the US East zone, the framework charges for integration Llama 3.2 1B $0.1/M input or output tokens; Llama 3.2 90B—$2/M input or output tokens.

The Llama 3.2 1B price on the Grok platform is four times higher: $0.4/M input or output tokens.

Claude is a family of models that can process text, code, and image input and generate code and text. The last generation includes two state-of-the-art models: the flagship Claude 3.5 Sonnet, specializing in complex tasks, coding, and creative writing, and the smaller and faster Claude 3.5 Haiku. The most powerful model of the previous generation is Claude 3 Opus, good in math and coding. The models support 10+ languages.

Claude emphasizes ethics, guided by a Constitutional AI manifesto rooted in universal human values. Recently, it introduced a beta feature for computer use, enabling the model to interact with software and perform tasks like filling forms using data from your PC and the Internet.

The parameters are undisclosed, though they are rumored to be about 500 billion. The context window is 200k+ tokens (500 pages of text or 100 images) for all Claude 3.5 versions.

The model is cloud-hosted only. There are three first-party Anthropic APIs:

You can call APIs directly or use Python SDK and TypeScript SDK.

Claude 3.5 and Claude 3 families are also available through Amazon Bedrock API and Vertex AI API.

Anthropic’s strict information security requirements were a stumbling block when it came to model customization since the tuning data is user-controlled. So far, fine-tuning is only possible for Claude 3 Haiku in Amazon Bedrock.

Claude 3.5 Sonnet usage costs $3/M input tokens and $15/M output tokens; Claude 3.5 Haiku is $0.25/M input tokens and $1.25/M output tokens. The Batches API provides a 50 percent discount. The detailed pricing info is here.

Grok, an Elon Musk's brainchild, is integrated with X (formerly Twitter) and incorporates information from posts and comments in X into its answers. Grok-1 is open-source; you can download the code from GitHub.

The latest Grok family generation includes the commercial Grok-2. The Grok-2 mini is to be released soon. Currently, only the Beta version is accessible on the xAI console.

The website claims X Grok 2 Beta AI supports many languages, but their number is undisclosed. Obviously, the model can speak English.

Grok, coined by Robert A. Heinlein, means deep understanding. While strong in coding and math, Grok lacks safety measures, making it easier to manipulate into harmful responses. It’s not ideal for customer service applications.

There are 314 billion parameters declared for Grok-1, and it has an 8.000-length context window. Parameters for Grok-2 are unknown so far, but the Grok beta version, which belongs to the Grok-2 family, has a 128-length context window.

Grok-2 is multimodal. The model can generate high-resolution images on the X social network and understand input images, even explaining the meaning of a meme. However, it’s not publicly available yet.

Grok-1 can be downloaded and deployed on-premises.

In the beginning, Grok was used only by the X platform and by premium users of X as a chatbot. However, in October 2024, Grok presented its first REST API service for enterprises, currently in the public beta testing phase. The API is accessible via xAI Console, which provides tools to create API keys, manage teams, handle billing, compare models, track usage, and access API documentation.

Currently, only the Grok-beta model—offering comparable performance to Grok 2 with enhanced efficiency, speed, and capabilities—is accessible via API on the console.

The xAI API integrates fully and is available through both the OpenAI SDK and the Anthropic SDK. Once you update the base URL, you can use the SDKs to call the Grok models with your xAI API key.

Though downloadable, Grok-1 model cannot be fine-tuned.

Grok-beta costs $5/M input tokens and $15/M output tokens. You can download the earlier version, Grok-1, for free.

Founded in 2024, Mistral AI is a French startup co-founded by former Meta employees Timothée Lacroix and Guillaume Lample, together with former DeepMind researcher Arthur Mensch. The company offers a mix of open-source and commercial generative models.

The premium range includes six LLMs, such as Mistral Large 2 for complex tasks, Codestral for AI coding, and fast models like 3B and 8B. Mistral Large 2 is free for non-commercial research.

Seven free models are also available, including Mathstral 7B and multilingual Mistral NeMo. Most Mistral models support five major European languages, while Mistral NeMo supports eleven, and Mistral Large 2 covers dozens of languages and 80+ coding languages.

Mistral Large 2 operates with 123 billion parameters.

Mistral Large 2, Mistral 3B, and 8B have a context window of 128,000 tokens.

First, you can access any model on La Plateforme, a developer platform hosted on Mistral’s infrastructure, and pay-as-you-go for commercial use.

Open-source models can be downloaded from Hugging Face and used on your device or in your private cloud infrastructure, but you’ll have to buy a commercial license (to get the price list, connect with the team at the Mistral AI website). They are also accessible via cloud partners GCP, AWS, Azure, IBM, Snowflake, NVIDIA, and OUTSCALE, with a pay-as-you-go pricing model.

Mistral Large 2 is available on Azure AI Studio, AWS Bedrock, Google Cloud Model Garden, IBM watsonx, and Snowflake.

Mistral AI API includes a list of APIs dedicated to specific tasks: Chat Completion API for generating responses, Embeddings API for vectorizing or representing words as vectors (necessary for text classification, sentiment analysis, and more), Files API for uploading files that can be used in various endpoints, etc.

All models are open to experiments and customization. You can use a dedicated fine-tuning API at La Plateforme to create the fine-tuning pipeline. An open-source codebase on GitHub can be customized, too.

Mistral Large 2 costs $2/1M for input tokens and $6/1M for output tokens. A recent price cut makes it one of the most cost-effective frontier models. Ministral 3B is $0.04/1M for input/output tokens.

Follow Build Fast with AI pages for all the latest AI updates and resources.

Why should 2025 be your year to master LLM APIs?

Because our Generative AI Mastery Program will take you from API calls to production-ready AI apps in just 6 weeks

Don't just call APIs. Master them.

* Lightweight (1B and 3 B)—text-only, 2-3 times faster than their bigger counterparts, and ideal for on-device and edge deployment; and
* Vision (11B and 90B)—support image inputs and excel on image understanding.

* Inference API for generating responses and processing complex inputs;
* Safety API to moderate outputs for avoiding harmful or biased content;
* Memory API that allows models to retain and reference past conversations, which is useful in customer support chatbots;
* Agentic System API for function calling; and more.

* Hugging Face with Axolotl library allows you to fine-tune all Llama 3.2 versions;
* PyTorch native library torchtune supports the end-to-end fine-tuning lifecycle for Llama 3.2 (1,3 and 11B only);
* Azure AI Studio offers fine-tuning for Llama 3.2 1B and 3B; other versions are coming soon; and
* Amazon Bedrock supports customizing Llama 3.1 models but not the later generation.

* Text Completions API is a legacy API, that won't be supported in the future.
* Messages API is the new main API, and transferring from Text Completion to Message API is recommended. It can be used for either single queries or stateless multi-turn conversations.
* Message Batches API (in beta mode) can process multiple Messages API requests simultaneously, costing 50 percent less than streaming API.

