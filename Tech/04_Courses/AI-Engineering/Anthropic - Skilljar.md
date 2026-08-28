---
aliases:
  - Anthropic
  - Claude
  - skilljar
tags:
  - ai-engineering
  - course
status: in-progress
area: AI Engineering
course: Anthropic Skilljar
module: Overview
source: https://training.skilljar.com/claude-with-the-anthropic-api
instructor: 
created: 2026-08-25
last_updated: 2026-08-26
progress: 40%
certificates:
---

# 🤖 Anthropic Skilljar

## 📑 Daftar Isi

- [Introduction](#introduction)
  - [Welcome to the course](#welcome-to-the-course)
- [Anthropic overview](#Anthropic overview)
  - [Overview of Claude models](#overview-of-claude-models)
- [Accessing Claude with the API](#accessing-claude-with-the-api)
  - [Making a request](#making-a-request)
  - [Multi-Turn conversations](#multi-turn-conversations)
  - [System prompts](#system-prompts)
  - [Temperature](#temperature)
  - [Response streaming](#response-streaming)
  - [Structured data](#structured-data)
- [Prompt evaluation](#prompt-evaluation)
  - [Prompt evaluation](#prompt-evaluation-1)
  - [A typical eval workflow](#a-typical-eval-workflow)
  - [Generating test datasets](#generating-test-datasets)
  - [Running the eval](#running-the-eval)
  - [Model based grading](#model-based-grading)
  - [Code based grading](#code-based-grading)
- [Prompt engineering techniques](#prompt-engineering-techniques)
  - [Prompt engineering](#prompt-engineering)
  - [Being clear and direct](#being-clear-and-direct)
  - [Being specific](#being-specific)
  - [Structure with XML tags](#structure-with-xml-tags)
  - [Providing examples](#providing-examples)
- [Tool use with Claude](#tool-use-with-claude)
  - [Introducing tool use](#introducing-tool-use)
  - [Project overview](#project-overview)
  - [Tool functions](#tool-functions)
  - [Tool schemas](#tool-schemas)
  - [Handling message blocks](#handling-message-blocks)
  - [Sending tool results](#sending-tool-results)
  - [Multi-turn conversations with tools](#multi-turn-conversations-with-tools)
  - [Implementing multiple turns](#implementing-multiple-turns)
  - [Using multiple tools](#using-multiple-tools)
  - [Fine grained tool calling](#fine-grained-tool-calling)
  - [The text edit tool](#the-text-edit-tool)
  - [The web search tool](#the-web-search-tool)
- [RAG and Agentic Search](#rag-and-agentic-search)
  - [Introducing Retrieval Augmented Generation](#introducing-retrieval-augmented-generation)
  - [Text chunking strategies](#text-chunking-strategies)
  - [Text embeddings](#text-embeddings)
  - [The full RAG flow](#the-full-rag-flow)
  - [Implementing the RAG flow](#implementing-the-rag-flow)
  - [BM25 lexical search](#bm25-lexical-search)
  - [A Multi-Index RAG pipeline](#a-multi-index-rag-pipeline)
- [Features of Claude](#features-of-claude)
  - [Extended thinking](#extended-thinking)
  - [Image support](#image-support)
  - [PDF support](#pdf-support)
  - [Citations](#citations)
  - [Prompt caching](#prompt-caching)
  - [Rules of prompt caching](#rules-of-prompt-caching)
  - [Prompt caching in action](#prompt-caching-in-action)
  - [Code execution and the Files API](#code-execution-and-the-files-api)
- [Model Context Protocol](#model-context-protocol)
  - [Introducing MCP](#introducing-mcp)
  - [MCP clients](#mcp-clients)
  - [Project setup](#project-setup)
  - [Defining tools with MCP](#defining-tools-with-mcp)
  - [The server inspector](#the-server-inspector)
  - [Implementing a client](#implementing-a-client)
  - [Defining resources](#defining-resources)
  - [Accessing resources](#accessing-resources)
  - [Defining prompts](#defining-prompts)
  - [Prompts in the client](#prompts-in-the-client)
  - [MCP review](#mcp-review)
- [Anthropic apps - Claude Code and computer use](#anthropic-apps---claude-code-and-computer-use)
  - [Anthropic apps](#anthropic-apps)
  - [Claude Code setup](#claude-code-setup)
  - [Claude Code in action](#claude-code-in-action)
  - [Enhancements with MCP servers](#enhancements-with-mcp-servers)
- [Agents and workflows](#agents-and-workflows)
  - [Agents and workflows](#agents-and-workflows-1)
  - [Parallelization workflows](#parallelization-workflows)
  - [Chaining workflows](#chaining-workflows)
  - [Routing workflows](#routing-workflows)
  - [Agents and tools](#agents-and-tools)
  - [Environment inspection](#environment-inspection)
  - [Workflows vs agents](#workflows-vs-agents)

---

## Introduction

### Welcome to the course
_Belum dicatat._

---

## Anthropic overview

### Overview of Claude models
![[Pasted image 20260825150058.png]]
![[Pasted image 20260825150132.png]]

---

## Accessing Claude with the API

> When building applications with Claude, understanding the complete request lifecycle helps you make better architectural decisions and debug issues more effectively. Let's walk through what happens from the moment a user clicks "send" in your chat interface to when Claude's response appears on screen.

### Making a request

#### The Five-Step Request Flow

Every interaction with Claude follows a predictable pattern with five distinct phases: request to server, request to Anthropic API, model processing, response to server, and response to client.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623275%2F03_-_001_-_Accessing_the_API_03.1748623275310.png)

#### Why You Need a Server

You should never make requests to the Anthropic API directly from client-side code. Here's why:

*   API requests require a secret API key for authentication
*   Exposing this key in client code creates a serious security vulnerability
*   Anyone could extract the key and make unauthorized requests

Instead, your web or mobile app sends requests to your own server, which then communicates with the Anthropic API using the securely stored key.

#### Making API Requests

When your server contacts the Anthropic API, you can use either an official SDK or make plain HTTP requests. Anthropic provides SDKs for Python, TypeScript, JavaScript, Go, and Ruby.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623276%2F03_-_001_-_Accessing_the_API_05.1748623276722.png)

Every request must include these essential fields:

*   **API Key** - Identifies your request to Anthropic
*   **Model** - Name of the model to use (like "claude-3-sonnet")
*   **Messages** - List containing the user's input text
*   **Max Tokens** - Limit for how many tokens Claude can generate

#### Inside Claude's Processing

Once Anthropic receives your request, Claude processes it through four main stages: tokenization, embedding, contextualization, and generation.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623277%2F03_-_001_-_Accessing_the_API_08.1748623277503.png)

#### Tokenization

Claude first breaks your input text into smaller chunks called tokens. These can be whole words, parts of words, spaces, or symbols. For simplicity, think of each word as one token.

#### Embedding

Each token gets converted into an embedding - a long list of numbers that represents all possible meanings of that word. Think of embeddings as numerical definitions that capture semantic relationships.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623278%2F03_-_001_-_Accessing_the_API_10.1748623278148.png)

Words often have multiple meanings. For example, "quantum" could refer to:

*   A discrete unit of physical quantity (physics)
*   Quantum mechanics or quantum physics concepts
*   Something extremely small or subatomic
*   Quantum computing applications

#### Contextualization

Claude refines each embedding based on surrounding words to determine the most likely meaning in context. This process adjusts the numerical representations to highlight the appropriate definition.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623278%2F03_-_001_-_Accessing_the_API_11.1748623278717.png)

#### Generation

The contextualized embeddings pass through an output layer that calculates probabilities for each possible next word. Claude doesn't always pick the highest probability word - it uses a mix of probability and controlled randomness to create natural, varied responses.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623279%2F03_-_001_-_Accessing_the_API_13.1748623279317.png)

After selecting each word, Claude adds it to the sequence and repeats the entire process for the next word.

#### When Claude Stops Generating

After each token, Claude checks several conditions to decide whether to continue:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623280%2F03_-_001_-_Accessing_the_API_15.1748623279963.png)

*   **Max tokens reached** - Has it hit the limit you specified?
*   **Natural ending** - Did it generate an end-of-sequence token?
*   **Stop sequence** - Did it encounter a predefined stop phrase?

#### The API Response

When generation completes, the API sends back a structured response containing:

*   **Message** - The generated text
*   **Usage** - Count of input and output tokens
*   **Stop Reason** - Why generation ended

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623281%2F03_-_001_-_Accessing_the_API_17.1748623281653.png)

Your server receives this response and forwards the generated text back to your client application, where it appears in the user interface.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623282%2F03_-_001_-_Accessing_the_API_19.1748623282180.png)

#### Key Takeaways

Understanding this flow helps you:

*   Design secure architectures that protect your API keys
*   Set appropriate token limits for your use case
*   Handle different stop reasons in your application logic
*   Debug issues by understanding where they might occur in the pipeline

Don't worry about memorizing every detail - the goal is familiarizing yourself with the terminology and overall process you'll encounter when working with Claude's API.

---

Making your first request to the Anthropic API is straightforward once you understand the basic setup and structure. This guide walks through the essential steps to get Claude responding to your prompts using Python.

#### Setting Up Your Environment

Before making any API calls, you need to install the required packages and configure your API key securely.

First, install the necessary dependencies in your Jupyter notebook:

```
%pip install anthropic python-dotenv
```

Next, create a `.env` file in the same directory as your notebook to store your API key securely:

```
ANTHROPIC_API_KEY="your-api-key-here"
```

This approach keeps your API key out of your code and prevents accidentally committing it to version control. Always add `.env` to your `.gitignore` file.

Load the environment variables and create your API client:

```
from dotenv import load_dotenv
load_dotenv()

from anthropic import Anthropic

client = Anthropic()
model = "claude-sonnet-4-0"
```

#### The Create Function

The core of making API requests is the `client.messages.create()` function. This function requires three key parameters:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623269%2F03_-_003_-_Making_a_Request_09.1748623269461.png)

*   **model** - The name of the Claude model you want to use
*   **max\_tokens** - A safety limit on response length (not a target)
*   **messages** - The conversation history you're sending to Claude

The `max_tokens` parameter acts as a safety mechanism. If you set it to 1000, Claude will stop generating after 1000 tokens even if it has more to say. Claude doesn't try to reach this limit - it just writes what it thinks is appropriate and stops if it hits the maximum.

#### Understanding Messages

Messages represent the conversation between you and Claude, similar to a chat application. There are two types of messages:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623270%2F03_-_003_-_Making_a_Request_13.1748623270369.png)

*   **User messages** - Content you want to send to Claude (written by humans)
*   **Assistant messages** - Responses that Claude has generated

Each message is a dictionary with a `role` (either "user" or "assistant") and `content` (the actual text).

#### Making Your First Request

Here's a complete example of making a request to Claude:

```
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence"
        }
    ]
)
```

When you run this code, Claude will process your request and return a response object containing the generated text along with metadata about the request.

#### Extracting the Response

The response object contains a lot of information, but you usually just want the generated text. Access it using:

```
message.content[0].text
```

This gives you clean, readable output like: "Quantum computing is a type of computation that leverages quantum mechanics principles like superposition and entanglement to process information using quantum bits (qubits), potentially solving certain complex problems exponentially faster than classical computers."

With these basics in place, you can start experimenting with different prompts and building more complex interactions with Claude.

### Multi-Turn conversations

When working with the Anthropic API and Claude, there's a crucial concept you need to understand: **Claude doesn't store any of your conversation history**. Each request you make is completely independent, with no memory of previous exchanges.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623270%2F03_-_004_-_Multi-Turn_Conversations_01.1748623269971.png)

This means if you want to have a multi-turn conversation where Claude remembers context from earlier messages, you need to handle the conversation state yourself.

#### The Problem with Stateless Conversations

Let's say you ask Claude "What is quantum computing?" and get a good response. Then you follow up with "Write another sentence" - Claude has no idea what you're referring to. It will write a sentence about something completely random because it has no memory of the quantum computing discussion.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623270%2F03_-_004_-_Multi-Turn_Conversations_02.1748623270625.png)

#### How Multi-Turn Conversations Work

To maintain conversation context, you need to do two things:

*   Manually maintain a list of all messages in your code
*   Send the complete message history with every request

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623271%2F03_-_004_-_Multi-Turn_Conversations_05.1748623271251.png)

Here's the flow that actually works:

1.  Send your initial user message to Claude
2.  Take Claude's response and add it to your message list as an assistant message
3.  Add your follow-up question as another user message
4.  Send the entire conversation history to Claude

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623271%2F03_-_004_-_Multi-Turn_Conversations_08.1748623271832.png)

#### Building Helper Functions

To make conversation management easier, you can create three helper functions:

```
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages):
    message = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
    )
    return message.content[0].text
```

#### Putting It All Together

Here's how you use these functions to maintain a conversation:

```
# Start with an empty message list
messages = []

# Add the initial user question
add_user_message(messages, "Define quantum computing in one sentence")

# Get Claude's response
answer = chat(messages)

# Add Claude's response to the conversation history
add_assistant_message(messages, answer)

# Add a follow-up question
add_user_message(messages, "Write another sentence")

# Get the follow-up response with full context
final_answer = chat(messages)
```

Now Claude will understand that "Write another sentence" refers to expanding on the quantum computing definition, because you've provided the complete conversation context.

These helper functions will be useful throughout your work with Claude, making it much easier to build applications that can maintain meaningful conversations over multiple exchanges.

### System prompts

#Systemprompts are a powerful way to customize how Claude responds to user input. Instead of getting generic answers, you can shape Claude's tone, style, and approach to match your specific use case.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623273%2F03_-_006_-_System_Prompts_00.1748623272065.png)

#### Why System Prompts Matter

Consider building a math tutor chatbot. When a student asks "How do I solve 5x + 2 = 3 for x?", you want Claude to act like a real tutor, not just spit out the answer. A good math tutor should:

*   Initially give hints rather than complete solutions
*   Patiently walk students through problems step by step
*   Show solutions for similar problems as examples

You definitely don't want Claude to:

*   Immediately give direct answers
*   Tell students to just use a calculator

#### How System Prompts Work

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623273%2F03_-_006_-_System_Prompts_05.1748623273817.png)

System prompts provide Claude with guidance on how to respond. You define them as plain strings and pass them into the create function call. The key benefits are:

*   System prompts provide Claude guidance on how to respond
*   Claude will try to respond in the same way someone in the specified role would respond
*   Helps keep Claude on task

Here's the basic structure:

```
system_prompt = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""

client.messages.create(
    model=model,
    messages=messages,
    max_tokens=1000,
    system=system_prompt
)
```

#### Seeing the Difference

Without a system prompt, Claude gives a complete step-by-step solution immediately. This might be helpful, but it doesn't encourage the student to think through the problem themselves.

With the math tutor system prompt, Claude's response changes dramatically. Instead of providing the full solution, Claude asks guiding questions like "What do you think would be a good first step to isolate x? Consider what operation we might need to perform on both sides to start moving terms around."

#### Building a Flexible Chat Function

Rather than hard-coding system prompts, you can make your chat function more reusable by accepting system prompts as parameters:

```
def chat(messages, system=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text
```

This approach handles an important detail: Claude's API doesn't accept `system=None`, so you need to conditionally include the system parameter only when it's provided.

Now you can call your chat function with or without a system prompt:

```
# Without system prompt
answer = chat(messages)

# With system prompt
system = """
You are a patient math tutor.
Do not directly answer a student's questions.
Guide them to a solution step by step.
"""
answer = chat(messages, system=system)
```

System prompts are essential for creating AI applications that behave consistently and appropriately for their intended purpose. They transform generic AI responses into specialized, role-appropriate interactions.

### Temperature

#Temperature is a powerful parameter that controls how predictable or creative Claude's responses will be. Understanding how to use it effectively can dramatically improve your AI applications.

#### How Claude Generates Text

Before diving into temperature, it helps to understand Claude's text generation process. When you send Claude a prompt like "What do you think?", it goes through three key steps:

*   **Tokenization** - Breaking your input into smaller chunks
*   **Prediction** - Calculating probabilities for possible next words
*   **Sampling** - Choosing a token based on those probabilities

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623338%2F03_-_008_-_Temperature_00.1748623338635.png)

In this example, Claude might assign a 30% probability to "about", 20% to "would", 10% to "of", and so on. The model then selects one token and repeats this entire process to build complete sentences.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623339%2F03_-_008_-_Temperature_05.1748623339740.png)

#### What Temperature Does

Temperature is a decimal value between 0 and 1 that directly influences these selection probabilities. It's like adjusting the "creativity dial" on Claude's responses.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623340%2F03_-_008_-_Temperature_06.1748623340446.png)

At low temperatures (near 0), Claude becomes very deterministic - it almost always picks the highest probability token. At high temperatures (near 1), Claude distributes probability more evenly across options, leading to more varied and creative outputs.

#### Interactive Temperature Demo

You can see temperature in action with Claude's interactive demo. Watch how the probability distribution changes as you adjust the temperature slider:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623341%2F03_-_008_-_Temperature_07.1748623341049.png)

At temperature 0.0, "about" gets 100% probability - completely deterministic. At temperature 1.0, probabilities spread more evenly across all possible tokens, introducing randomness and creativity.

#### Choosing the Right Temperature

Different tasks call for different temperature ranges:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623341%2F03_-_008_-_Temperature_10.1748623341732.png)

#### Low Temperature (0.0 - 0.3)

*   Factual responses
*   Coding assistance
*   Data extraction
*   Content moderation

#### Medium Temperature (0.4 - 0.7)

*   Summarization
*   Educational content
*   Problem-solving
*   Creative writing with constraints

#### High Temperature (0.8 - 1.0)

*   Brainstorming
*   Creative writing
*   Marketing content
*   Joke generation

#### Implementing Temperature in Code

Adding temperature support to your chat function is straightforward. Here's how to modify your existing function:

```
def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    
    if system:
        params["system"] = system
    
    message = client.messages.create(**params)
    return message.content[0].text
```

The key changes are adding `temperature=1.0` as a parameter and including `"temperature": temperature` in the params dictionary.

#### Testing Temperature Effects

To see temperature in action, try generating movie ideas with different settings:

```
# Low temperature - more predictable
answer = chat(messages, temperature=0.0)

# High temperature - more creative  
answer = chat(messages, temperature=1.0)
```

At temperature 0.0, you might consistently get responses like "A time-traveling archaeologist must prevent ancient artifacts from being stolen." At temperature 1.0, you'll see much more variety in themes, characters, and plot elements.

#### Key Takeaways

Remember that temperature doesn't guarantee different outputs - it just changes the probability of getting them. Even at high temperatures, Claude might occasionally produce similar responses. The key is matching your temperature choice to your specific use case:

*   Need consistent, factual responses? Use low temperature
*   Want creative brainstorming? Dial up the temperature
*   Somewhere in between? Medium temperatures work well for most general tasks

Temperature is one of the most practical parameters you can adjust to fine-tune Claude's behavior for your specific needs.

### Response streaming

When building chat applications with Claude, there's a significant user experience challenge: responses can take 10-30 seconds to generate, leaving users staring at a loading spinner. The solution is response streaming, which lets users see text appear chunk by chunk as Claude generates it, creating a much more responsive feel.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623337%2F03_-_009_-_Response_Streaming_00.1748623336822.png)

#### The Problem with Standard Responses

In a typical chat setup, your server sends a user message to Claude and waits for the complete response before sending anything back to the client. This creates an awkward delay where users have no feedback that anything is happening.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623338%2F03_-_009_-_Response_Streaming_02.1748623337803.png)

#### How Streaming Works

With streaming enabled, Claude immediately sends back an initial response indicating it has received your request and is starting to generate text. Then you receive a series of events, each containing a small piece of the overall response.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623338%2F03_-_009_-_Response_Streaming_03.1748623338384.png)

Your server can forward these text chunks to your client application as they arrive, allowing users to see the response building up word by word. All of these events are part of a single request to Claude.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623339%2F03_-_009_-_Response_Streaming_04.1748623338949.png)

#### Understanding Stream Events

When you enable streaming, Claude sends back several types of events:

*   **MessageStart** - A new message is being sent
*   **ContentBlockStart** - Start of a new block containing text, tool use, or other content
*   **ContentBlockDelta** - Chunks of the actual generated text
*   **ContentBlockStop** - The current content block has been completed
*   **MessageDelta** - The current message is complete
*   **MessageStop** - End of information about the current message

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623339%2F03_-_009_-_Response_Streaming_11.1748623339633.png)

The `ContentBlockDelta` events contain the actual generated text that you'll want to display to users.

#### Basic Streaming Implementation

To enable streaming, add `stream=True` to your messages.create call:

```
messages = []
add_user_message(messages, "Write a 1 sentence description of a fake database")

stream = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=messages,
    stream=True
)

for event in stream:
    print(event)
```

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623340%2F03_-_009_-_Response_Streaming_12.1748623340577.png)

#### Simplified Text Streaming

Rather than manually parsing events, you can use the SDK's simplified streaming interface that extracts just the text content:

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        print(text, end="")
```

This approach automatically filters out everything except the actual text content, which is usually what you need for displaying responses to users.

#### Getting the Complete Message

While streaming individual chunks is great for user experience, you often need the complete message for storage or further processing. After streaming completes, you can get the assembled final message:

```
with client.messages.stream(
    model=model,
    max_tokens=1000,
    messages=messages
) as stream:
    for text in stream.text_stream:
        # Send each chunk to your client
        pass
    
    # Get the complete message for database storage
    final_message = stream.get_final_message()
```

This gives you the best of both worlds: real-time streaming for users and a complete message object for your application logic.

### Structured data

When you need Claude to generate structured data like JSON, Python code, or bulleted lists, you'll often run into a common problem: Claude wants to be helpful and add explanatory text around your content. While this is usually great, sometimes you need just the raw data with nothing else.
Consider building a web app that generates AWS EventBridge rules. Users enter a description, click generate, and expect to see clean JSON they can immediately copy and use. If Claude returns the JSON wrapped in markdown code blocks with explanatory text, users can't simply copy the entire response - they have to manually select just the JSON portion.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623326%2F03_-_011_-_Structured_Data_02.1748623325858.png)

#### The Problem with Default Responses

By default, when you ask Claude to generate JSON, you might get something like this:

````
```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
```

This rule captures EC2 instance state changes when instances start running.
````

The JSON is correct, but it's wrapped in markdown formatting and includes explanatory text. For a web app where users need to copy the raw JSON, this creates friction in the user experience.

#### The Solution: Assistant Message Prefilling + Stop Sequences

You can combine assistant message prefilling with stop sequences to get exactly the content you want. Here's how it works:

```
messages = []

add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")

text = chat(messages, stop_sequences=["```"])
```

This technique works by:

1.  The user message tells Claude what to generate
2.  The prefilled assistant message makes Claude think it already started a markdown code block
3.  Claude continues by writing just the JSON content
4.  When Claude tries to close the code block with ` ``` `, the stop sequence immediately ends generation

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623327%2F03_-_011_-_Structured_Data_15.1748623326804.png)

The result is clean JSON with no extra formatting:

```
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
```

#### Processing the Response

You might notice some extra newline characters in the response. These are easy to handle:

```
import json

# Clean up and parse the JSON
clean_json = json.loads(text.strip())
```

#### Beyond JSON

This technique isn't limited to JSON generation. Use it anytime you need structured data without commentary:

*   Python code snippets
*   Bulleted lists
*   CSV data
*   Any formatted content where you want just the content, not explanations

The key is identifying what Claude naturally wants to wrap your content in, then using that as your prefill and stop sequence. For code, it's usually markdown code blocks. For lists, it might be different formatting markers.

This approach gives you precise control over Claude's output format, making it much easier to integrate AI-generated content into applications where clean, structured data is essential.

---
## Prompt evaluation

#### Prompt evaluation
When working with Claude, writing a good prompt is just the beginning. To build reliable AI applications, you need to understand two critical concepts: prompt engineering and prompt evaluation. Prompt engineering gives you techniques for writing better prompts, while prompt evaluation helps you measure how well those prompts actually work.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623381%2F04_-_001_-_Prompt_Evaluation_00.1748623381094.png)

#### Prompt Engineering vs Prompt Evaluation

Prompt engineering is your toolkit for crafting effective prompts. It includes techniques like:

*   Multishot prompting
*   Structuring with XML tags
*   Many other best practices

These techniques help Claude understand exactly what you're asking for and how you want it to respond.

Prompt evaluation takes a different approach. Instead of focusing on how to write prompts, it's about measuring their effectiveness through automated testing. You can:

*   Test against expected answers
*   Compare different versions of the same prompt
*   Review outputs for errors

#### Three Paths After Writing a Prompt

Once you've drafted a prompt, you typically face three options for what to do next:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623382%2F04_-_001_-_Prompt_Evaluation_10.1748623382207.png)

**Option 1:** Test the prompt once and decide it's good enough. This carries a significant risk of breaking in production when users provide unexpected inputs.

**Option 2:** Test the prompt a few times and tweak it to handle a corner case or two. While better than option 1, users will often provide very unexpected outputs that you haven't considered.

**Option 3:** Run the prompt through an evaluation pipeline to score it, then iterate on the prompt based on objective metrics. This approach requires more work and cost, but gives you much more confidence in your prompt's reliability.

#### Why Most Engineers Fall Into Testing Traps

Options 1 and 2 are common traps that all engineers fall into, myself included. It's natural to write a prompt for a serious application and not test it thoroughly enough. We tend to underestimate how many edge cases real users will encounter.

The reality is that when you deploy a prompt to production, users will interact with it in ways you never anticipated. What seemed like a solid prompt during your limited testing can quickly break down when faced with the full variety of real-world inputs.

#### The Evaluation-First Approach

Option 3 represents a more systematic approach to prompt development. By running your prompt through an evaluation pipeline, you get objective metrics about its performance across a broader range of test cases. This data-driven approach lets you:

*   Identify weaknesses before they become production issues
*   Compare different prompt versions objectively
*   Iterate with confidence based on measurable improvements
*   Build more reliable AI applications

While this approach requires more upfront investment in time and testing infrastructure, it pays dividends in the reliability and robustness of your final application. The goal is to catch problems during development rather than after your users encounter them.

## A typical eval workflow
A typical prompt evaluation workflow follows five key steps that help you systematically improve your prompts through objective measurement. While there are many different ways to assemble these workflows and various open source and paid tools available, understanding the core process helps you start small and scale up as needed.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623388%2F04_-_002_-_A_Typical_Eval_Workflow_00.1748623388621.png)

### Step 1: Draft a Prompt

Start by writing an initial prompt that you want to improve. For this example, we'll use a simple prompt:

```
prompt = f"""
Please answer the user's question:

{question}
"""
```

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623390%2F04_-_002_-_A_Typical_Eval_Workflow_04.1748623389909.png)

This basic prompt will serve as our baseline for testing and improvement.

### Step 2: Create an Eval Dataset

Your evaluation dataset contains sample inputs that represent the types of questions or requests your prompt will handle in production. The dataset should include questions that will be interpolated into your prompt template.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623391%2F04_-_002_-_A_Typical_Eval_Workflow_06.1748623390933.png)

For this example, our dataset includes three questions:

*   "What's 2+2?"
*   "How do I make oatmeal?"
*   "How far away is the Moon?"

In real-world evaluations, you might have tens, hundreds, or even thousands of records. You can assemble these datasets by hand or use Claude to generate them for you.

### Step 3: Feed Through Claude

Take each question from your dataset and merge it with your prompt template to create complete prompts. Then send each one to Claude to get responses.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623391%2F04_-_002_-_A_Typical_Eval_Workflow_08.1748623391715.png)

For example, the first question becomes:

```
Please answer the user's question:
What's 2+2?
```

Claude might respond with "2 + 2 = 4" for the math question, provide oatmeal cooking instructions for the second question, and give the distance to the Moon for the third.

### Step 4: Feed Through a Grader

The grader evaluates the quality of Claude's responses by examining both the original question and Claude's answer. This step provides objective scoring, typically on a scale from 1 to 10, where 10 represents a perfect answer and lower scores indicate room for improvement.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623392%2F04_-_002_-_A_Typical_Eval_Workflow_11.1748623392294.png)

In our example, the grader might assign:

*   Math question: 10 (perfect answer)
*   Oatmeal question: 4 (needs improvement)
*   Moon question: 9 (very good answer)

The average score across all questions gives you an objective measurement: (10 + 4 + 9) ÷ 3 = 7.66

### Step 5: Change Prompt and Repeat

Now that you have a baseline score, you can modify your prompt and run the entire process again to see if your changes improve performance.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623393%2F04_-_002_-_A_Typical_Eval_Workflow_15.1748623393094.png)

For example, you might add more guidance to your prompt:

```
prompt = f"""
Please answer the user's question:

{question}

Answer the question with ample detail
"""
```

After running this improved prompt through the same evaluation process, you might get a higher average score of 8.7, indicating that the additional instruction helped Claude provide better responses.

#### Prompt Scoring

The key benefit of this workflow is getting objective measurements of prompt performance. You can:

*   Compare different prompt versions numerically
*   Use the version with the best score
*   Continue iterating to find even better approaches

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623393%2F04_-_002_-_A_Typical_Eval_Workflow_17.1748623393804.png)

This systematic approach removes guesswork from prompt engineering and gives you confidence that your changes are actually improvements rather than just different variations.

## Generating test datasets
Building a custom prompt evaluation workflow starts with creating a solid prompt and then generating test data to see how well it performs. Let's walk through setting up an evaluation system for a prompt that helps users write AWS-specific code.

#### Setting Up the Goal

Our prompt needs to assist users in writing three specific types of output for AWS use cases:

*   Python code
*   JSON configuration files
*   Regular expressions

The key requirement is that when a user requests help with a task, we return clean output in one of these formats without any extra explanations, headers, or footers.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623393%2F04_-_003_-_Generating_Test_Datasets_01.1748623392676.png)

Here's our starting prompt (version 1):

```
prompt = f"""
Please provide a solution to the following task:
{task}
"""
```

#### Creating an Evaluation Dataset

An evaluation dataset contains inputs that we'll feed into our prompt. For each combination of prompt and input, we'll run the prompt and analyze the results.

Our dataset will be an array of JSON objects, where each object contains a "task" property describing what we want Claude to accomplish. We can either create this dataset by hand or generate it automatically using Claude.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623393%2F04_-_003_-_Generating_Test_Datasets_05.1748623393811.png)

Since we're generating test data, this is a perfect opportunity to use a faster model like Haiku instead of the full Claude model.

#### Generating Test Data with Code

Let's create a function that automatically generates our test dataset. First, we'll need our helper functions for working with Claude:

```
def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)

def add_assistant_message(messages, text):
    assistant_message = {"role": "assistant", "content": text}
    messages.append(assistant_message)

def chat(messages, system=None, temperature=1.0, stop_sequences=[]):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    
    response = client.messages.create(**params)
    return response.content[0].text
```

Now we'll create our dataset generation function:

````
def generate_dataset():
    prompt = """
Generate an evaluation dataset for a prompt evaluation. The dataset will be used to evaluate prompts that generate Python, JSON, or Regex specifically for AWS-related tasks. Generate an array of JSON objects, each representing task that requires Python, JSON, or a Regex to complete.

Example output:
```json
[
  {
    "task": "Description of task",
  },
  ...additional
]
```

* Focus on tasks that can be solved by writing a single Python function, a single JSON object, or a single regex
* Focus on tasks that do not require writing much code

Please generate 3 objects.
"""
````

To properly parse the JSON response, we'll use prefilling and stop sequences:

```
    messages = []
    add_user_message(messages, prompt)
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    return json.loads(text)
```

#### Testing the Dataset Generation

Let's run our function and see what kind of test cases we get:

```
dataset = generate_dataset()
print(dataset)
```

This should return three different test cases covering our target outputs - Python functions, JSON configurations, and regular expressions for AWS-specific tasks.

#### Saving the Dataset

Once we have our dataset, we'll save it to a file so we can easily load it later during evaluation:

```
with open('dataset.json', 'w') as f:
    json.dump(dataset, f, indent=2)
```

This creates a `dataset.json` file in the same directory as your notebook, containing your list of tasks ready for prompt evaluation.

With this foundation in place, you now have a systematic way to generate test data for evaluating how well your prompts perform across different types of AWS-related coding tasks.

#### Downloads

*   [001\_prompt\_evals.ipynb (opens in new tab)](https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1762977284/001_prompt_evals.ipynb?response-content-disposition=attachment&Expires=1787746106&Signature=V1nZ34HFSUNPYVaH3-DjO54oPqkrQrJaEw49r5Bg-Vm5kwrPxTG75tFf7qD6-3q2oDYQgcuG4-yShasUHpXs-GDmTimCJ~k-RQp~suYkkC6MkhHaQF-yKch95eg1VIPWgXQaYckak9NJTRspJf4U7xlZ5eeLION7rYhRlf95~2snD5vL3PfnuWQzrBCHsx32-43FU9SsvhrryFlgvmwxQ2WQkls4dJzpvtEMrGXdkyV42F9rn5ThFi0W2cjkV7-7GkPLamLlOw-qK7rtnP17Y73ollUybk6fgTAO2CfBIcnoN0GdMFnd85cCHnYWmAZYRhxtWb5uXYNGSypJoO5pJQ__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)

## Running the eval
Now that we have our evaluation dataset ready, it's time to build the core evaluation pipeline. This involves taking each test case, merging it with our prompt, feeding it to Claude, and then grading the results.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623396%2F04_-_004_-_Running_the_Eval_00.1748623396420.png)

The evaluation process follows a clear workflow: we take our dataset of test cases, combine each one with our prompt template, send it to Claude for processing, and then evaluate the output using a grader system.

#### Building the Core Functions

The evaluation pipeline consists of three main functions, each with a specific responsibility. Let's start with the simplest one - the function that handles individual prompts.

#### The run\_prompt Function

This function takes a test case and merges it with our prompt template:

```
def run_prompt(test_case):
    """Merges the prompt and test case input, then returns the result"""
    prompt = f"""
Please solve the following task:

{test_case["task"]}
"""
    
    messages = []
    add_user_message(messages, prompt)
    output = chat(messages)
    return output
```

Right now, we're keeping the prompt extremely simple. We're not including any formatting instructions, so Claude will likely return more verbose output than we need. We'll refine this later as we iterate on our prompt design.

#### The run\_test\_case Function

This function orchestrates running a single test case and grading the result:

```
def run_test_case(test_case):
    """Calls run_prompt, then grades the result"""
    output = run_prompt(test_case)
    
    # TODO - Grading
    score = 10
    
    return {
        "output": output,
        "test_case": test_case,
        "score": score
    }
```

For now, we're using a hardcoded score of 10. The grading logic is where we'll spend significant time in upcoming sections, but this placeholder lets us test the overall pipeline.

#### The run\_eval Function

This function coordinates the entire evaluation process:

```
def run_eval(dataset):
    """Loads the dataset and calls run_test_case with each case"""
    results = []
    
    for test_case in dataset:
        result = run_test_case(test_case)
        results.append(result)
    
    return results
```

This function processes every test case in our dataset and collects all the results into a single list.

#### Running the Evaluation

To execute our evaluation pipeline, we load our dataset and run it through our functions:

```
with open("dataset.json", "r") as f:
    dataset = json.load(f)

results = run_eval(dataset)
```

The first time you run this, expect it to take some time - even with Claude Haiku, it can take around 30 seconds to process a full dataset. We'll cover optimization techniques later.

#### Examining the Results

The evaluation returns a structured JSON array where each object represents one test case result:

```
print(json.dumps(results, indent=2))
```

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623397%2F04_-_004_-_Running_the_Eval_18.1748623397308.png)

Each result contains three key pieces of information:

*   **output**: The complete response from Claude
*   **test\_case**: The original test case that was processed
*   **score**: The evaluation score (currently hardcoded)

As you can see in the output, Claude generates quite verbose responses since we haven't provided specific formatting instructions yet. This is exactly the kind of issue we'll address as we refine our prompts.

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623397%2F04_-_004_-_Running_the_Eval_01.1748623397839.png)

#### What We've Accomplished

At this point, we've successfully built the core evaluation pipeline. We can take our dataset, process it through Claude, and collect structured results. The major missing piece is the grading system - that hardcoded score of 10 needs to be replaced with actual evaluation logic.

This pipeline represents the foundation of most AI evaluation systems. While it may seem simple, you've just built the majority of what an eval pipeline actually does. The complexity comes in the details - better prompts, sophisticated grading, and performance optimizations.

Next, we'll dive into the critical topic of graders, which will transform our hardcoded scores into meaningful evaluations of Claude's performance.

## Model based grading
When building prompt evaluation workflows, grading systems provide objective signals about output quality. A grader takes model output and returns some kind of measurable feedback - typically a number between 1 and 10, where 10 represents high quality and 1 represents poor quality.

#### Types of Graders

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623451%2F04_-_005_-_Model_Based_Grading_03.1748623451557.png)

There are three main approaches to grading model outputs:

*   **Code graders** - Programmatically evaluate outputs using custom logic
*   **Model graders** - Use another AI model to assess the quality
*   **Human graders** - Have people manually review and score outputs

#### Code Graders

Code graders let you implement any programmatic check you can imagine. Common uses include:

*   Checking output length
*   Verifying output does/doesn't have certain words
*   Syntax validation for JSON, Python, or regex
*   Readability scores

The only requirement is that your code returns some usable signal - usually a number between 1 and 10.

#### Model Graders

Model graders feed your original output into another API call for evaluation. This approach offers tremendous flexibility for assessing:

*   Response quality
*   Quality of instruction following
*   Completeness
*   Helpfulness
*   Safety

#### Human Graders

Human graders provide the most flexibility but are time-consuming and tedious. They're useful for evaluating:

*   General response quality
*   Comprehensiveness
*   Depth
*   Conciseness
*   Relevance

#### Defining Evaluation Criteria

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623452%2F04_-_005_-_Model_Based_Grading_06.1748623452682.png)

Before implementing any grader, you need clear evaluation criteria. For a code generation prompt, you might focus on:

*   **Format** - Should return only Python, JSON, or Regex without explanation
*   **Valid Syntax** - Produced code should have valid syntax
*   **Task Following** - Response should directly address the user's task with accurate code

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623453%2F04_-_005_-_Model_Based_Grading_07.1748623453532.png)

The first two criteria work well with code graders, while task following is better suited for model graders due to their flexibility.

#### Implementing a Model Grader

Here's how to build a model grader function:

```
def grade_by_model(test_case, output):
    # Create evaluation prompt
    eval_prompt = """
    You are an expert code reviewer. Evaluate this AI-generated solution.
    
    Task: {task}
    Solution: {solution}
    
    Provide your evaluation as a structured JSON object with:
    - "strengths": An array of 1-3 key strengths
    - "weaknesses": An array of 1-3 key areas for improvement  
    - "reasoning": A concise explanation of your assessment
    - "score": A number between 1-10
    """
    
    messages = []
    add_user_message(messages, eval_prompt)
    add_assistant_message(messages, "```json")
    
    eval_text = chat(messages, stop_sequences=["```"])
    return json.loads(eval_text)
```

The key insight is asking for strengths, weaknesses, and reasoning alongside the score. Without this context, models tend to default to middling scores around 6.  
#### Integrating Grading into Your Workflow 
Update your test case runner to call the grader: 

``` python
def run_test_case(test_case):
    output = run_prompt(test_case)
    
    # Grade the output
    model_grade = grade_by_model(test_case, output)
    score = model_grade["score"]
    reasoning = model_grade["reasoning"]
    
    return {
        "output": output, 
        "test_case": test_case, 
        "score": score,
        "reasoning": reasoning
    }

```    

[Downloads 001_prompt_evals_grader.ipynb (opens in new tab)](https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1762977624/001_prompt_evals_grader.ipynb?response-content-disposition=attachment&Expires=1787746312&Signature=VFFYf1gQFwb~Ipf3SVxDScM~NZFgTutpRSnlkohEmTAeFbZwpxNAft52X42rxTLWnUG2dw7aQDq2~lkNxvwqQRHGO6wFhn68RYlEvMhjKuwV7gt9aSp5XvR6UrtSjzWxy4a65qWflrBfFosPXIHzsAdXbW9O058bhO~wOo3JB86BzYcUGYnW1nVsEL1RC9tPG2OCIIdmMZxA1jkEbaZRFv~fmpvc4Nkhl5gtJeJRxu0FaDXoH4WIwd5SdJo1X5asuL9SeIPezC6YiD3M4jmPW8r-mxsJo4j44MNj-St~9649SBYWG8xgIKB-Jv~Y6k916HskzFKOb8OI8hlO0GEi2A__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)

### Code based grading
When evaluating AI models that generate code, you need more than just checking if the response makes sense. You also need to verify that the generated code actually has valid syntax and follows the correct format. This is where code-based grading comes in.

#### How Code Grading Works

Code grading validates two key aspects of AI-generated responses:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623444%2F04_-_006_-_Code_Based_Grading_00.1748623444116.png)

*   **Format** - The response should return only the requested code type (Python, JSON, or Regex) without explanations
*   **Valid Syntax** - The generated code should actually parse correctly as the intended language
*   **Task Following** - The response should directly address what was asked and be accurate

The first two criteria are handled by the code grader, while task following is evaluated by the model grader. Together, they provide a comprehensive evaluation.

#### Syntax Validation Functions

To check if generated code has valid syntax, you can create three helper functions that attempt to parse the output:

![](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2Fa46l9irobhg0f5webscixp0bs%2Fpublic%2F1748623445%2F04_-_006_-_Code_Based_Grading_02.1748623445106.png)

```
def validate_json(text):
    try:
        json.loads(text.strip())
        return 10
    except json.JSONDecodeError:
        return 0

def validate_python(text):
    try:
        ast.parse(text.strip())
        return 10
    except SyntaxError:
        return 0

def validate_regex(text):
    try:
        re.compile(text.strip())
        return 10
    except re.error:
        return 0
```

Each function tries to parse the text as its respective format. If parsing succeeds, it returns a perfect score of 10. If it fails with an error, the syntax is invalid and returns 0.

#### Dataset Format Requirements

For the code grader to know which validator to use, your test cases need to specify the expected output format:

```
{
    "task": "Create a Python function to validate an AWS IAM username",
    "format": "python"
}
```

You can update your dataset generation prompt to automatically include this format field by adding it to the example output structure.

#### Improving Prompt Clarity

To get better results from your AI model, make your prompt instructions more specific about the expected output format:

```
* Respond only with Python, JSON, or a plain Regex
* Do not add any comments or commentary or explanation
```

You can also use a pre-filled assistant message with code blocks to encourage the model to return just the raw code:

```
add_assistant_message(messages, "```code")
```

This tells Claude to start generating code content without having to specify whether it's Python, JSON, or Regex ahead of time.

#### Combining Scores

The final step is merging the model grader score with the code grader score. A simple approach is to take the average:

```
model_grade = grade_by_model(test_case, output)
model_score = model_grade["score"]
syntax_score = grade_syntax(output, test_case)

score = (model_score + syntax_score) / 2
```

This gives equal weight to both content quality and technical correctness. You might adjust these weights based on what matters more for your specific use case.

#### Testing Your Implementation

Once you've implemented code grading, run your evaluation to get a baseline score. The score itself isn't inherently good or bad - what matters is whether you can improve it by refining your prompts. This gives you a quantitative way to measure prompt engineering progress rather than relying on subjective assessment.

#### Downloads

*   [001\_prompt\_evals\_fns.ipynb (opens in new tab)](https://cc.sj-cdn.net/instructor/4hdejjwplbrm-anthropic/assets/1762977673/001_prompt_evals_fns.ipynb?response-content-disposition=attachment&Expires=1787746687&Signature=bwAWaPAw7AzEIC-idGXVWC26R42vhPW5TxYNTCtpkw2CEHYQQ12llHL5yg1Xev5qbL4Cux1sJpENs-Wi1aZtUJ3ng6j8D9gbjV8cJ4Rd272zyYtzmZlLReBnSqBzq7~ZXohebeCplatPrExARzg91zUZ54TTAtUjnUkoO7SDxsQ2vLqjizKihdiwihs8JvsbGG8Poe9Vv3n~q36SwPoRSKKX3L~EmkxZd8Egak1bmoF-5tsNoXnx8AHMNGX~xgxMFBdTQKVnqVaFqkjtU~NssAPFRkhNhl7w5H6EVNykwMW4RjzFP2Xls3HZ-XSrMCKK4X4WAJyID0wAffhQ2QlXZQ__&Key-Pair-Id=APKAI3B7HFD2VYJQK4MQ)

---

## Prompt engineering techniques
_Belum dicatat._
### Prompt engineering
_Belum dicatat._

### Being clear and direct
_Belum dicatat._

### Being specific
_Belum dicatat._

### Structure with XML tags
_Belum dicatat._

### Providing examples
_Belum dicatat._

---

## Tool use with Claude

### Introducing tool use
_Belum dicatat._

### Project overview
_Belum dicatat._

### Tool functions
_Belum dicatat._

### Tool schemas
_Belum dicatat._

### Handling message blocks
_Belum dicatat._

### Sending tool results
_Belum dicatat._

### Multi-turn conversations with tools
_Belum dicatat._

### Implementing multiple turns
_Belum dicatat._

### Using multiple tools
_Belum dicatat._

### Fine grained tool calling
_Belum dicatat._

### The text edit tool
_Belum dicatat._

### The web search tool
_Belum dicatat._

---

## RAG and Agentic Search

### Introducing Retrieval Augmented Generation
_Belum dicatat._

### Text chunking strategies
_Belum dicatat._

### Text embeddings
_Belum dicatat._

### The full RAG flow
_Belum dicatat._

### Implementing the RAG flow
_Belum dicatat._

### BM25 lexical search
_Belum dicatat._

### A Multi-Index RAG pipeline
_Belum dicatat._

---

## Features of Claude

### Extended thinking
_Belum dicatat._

### Image support
_Belum dicatat._

### PDF support
_Belum dicatat._

### Citations
_Belum dicatat._

### Prompt caching
_Belum dicatat._

### Rules of prompt caching
_Belum dicatat._

### Prompt caching in action
_Belum dicatat._

### Code execution and the Files API
_Belum dicatat._

---

## Model Context Protocol

### Introducing MCP
_Belum dicatat._

### MCP clients
_Belum dicatat._

### Project setup
_Belum dicatat._

### Defining tools with MCP
_Belum dicatat._

### The server inspector
_Belum dicatat._

### Implementing a client
_Belum dicatat._

### Defining resources
_Belum dicatat._

### Accessing resources
_Belum dicatat._

### Defining prompts
_Belum dicatat._

### Prompts in the client
_Belum dicatat._

### MCP review
_Belum dicatat._

---

## Anthropic apps - Claude Code and computer use

### Anthropic apps
_Belum dicatat._

### Claude Code setup
_Belum dicatat._

### Claude Code in action
_Belum dicatat._

### Enhancements with MCP servers
_Belum dicatat._

---

## Agents and workflows

### Agents and workflows
_Belum dicatat._

### Parallelization workflows
_Belum dicatat._

### Chaining workflows
_Belum dicatat._

### Routing workflows
_Belum dicatat._

### Agents and tools
_Belum dicatat._

### Environment inspection
_Belum dicatat._

### Workflows vs agents
_Belum dicatat._

---

## 🗺️ Part of
[[MOC - AI Engineering]] · [[MOC - HOME]]
