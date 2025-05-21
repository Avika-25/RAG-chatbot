---
title: MCP (Model Context Protocol) Simplified
date: March 18, 2025
url: https://www.buildfastwithai.com/blogs/what-is-mcp-model-context-protocol
---

# MCP (Model Context Protocol) Simplified

## What Is MCP?

## Can’t We Do It Without MCP?

## MCP Architecture Overview

## How MCP Works?

## Conclusion

## Resources and Community

### Overview

### Reference

Are you waiting for the future to happen or ready to make it happen?

Don’t miss your chance to join Gen AI Launch Pad 2025 and shape what’s next.

In 2024 November, Anthropic introduced a new protocol named MCP (Model Context Protocol) which provides a standard method to connect external data sources and tools with LLMs. Let’s breakdown what this protocol is and why we need that. For now, MCP is compatible with Claude. But it can be used with other LLMs.

Before the USB ports came, there were different ports for connecting devices to the computer. PS/2 port is for keyboard and mouse. The VGA port is for monitors, etc. But after the USB port comes, it gives a standard interface to connect the device to the computer. Every device can connect with a computer using a USB port. It eliminates the need for a custom interface for each device and introduces a universal method to connect. MCP is also like this. It is like a USB port for LLMs. Tools, external data sources can connect to LLMs using MCP through a standard mechanism. So, no need to write custom integration for every single tool and data source anymore. MCP provides one standard way to connect all of this.

Absolutely we can connect tools and data sources to LLMs without MCP. Also, currently most of us do it without MCP. But the thing is when we do it without using MCP, we have to write custom integration for every single tool and data source. We have to put additional effort into that. With MCP we can make it easy. We don’t have to write custom integration for tools and data sources.

MCP uses client-server architecture. There are few main things we should know.

For local communication, MCP uses stdio while using HTTP with Server-Sent events for remote communication. It uses JSON for message exchange.

Let’s take a simple example. Assume you are using Claude Desktop, which serves as an MCP host application with an MCP client, and it connected to a MCP server. You ask for the weather forecast for tomorrow. Here is what happens:

In this blog, I am not going to talk about how to create our own MCP servers or MCP clients. If you are interested, you can refer these GitHub repos. There repos contain code for creating MCP server and MCP client.

GitHub Links

Model Context Protocol (MCP) standardizes tool and data integration for LLMs, much like how USB simplified device connectivity. By eliminating the need for custom integrations, MCP enhances interoperability and streamlines development. It also allows users to create their own MCP servers, enabling centralized management of multiple tools in one place.

---------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI Implementation. Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

---------------------------

Join our community of 12,000+ AI enthusiasts and learn to build powerful AI applications! Whether you're a beginner or an experienced developer, our resources will help you understand and implement Generative AI in your projects.

* MCP Host: LLM Application like Claude Desktop, Cursor, Windsurf like IDE or our own custom LLM Application. One host can connect to multiple servers using multiple MCP clients.
* MCP Client: MCP client maintain the connection between MCP server and the host application. This is a one-to-one connection. MCP host creates and manage MCP clients. Maintain security boundaries between servers.
* MCP Server: A program that follow MCP standards. MCP server contain set of tools, resources and pre-written prompts which can extent LLM abilities. External databases can be connected into these servers. We can build our own servers, or we can use existing MCP servers.

* MCP Server
* MCP Client

* Website: www.buildfastwithai.com
* LinkedIn: linkedin.com/company/build-fast-with-ai/
* Instagram: instagram.com/buildfastwithai/
* Twitter: x.com/satvikps
* Telegram: t.me/BuildFastWithAI

1. The MCP client gets the list of available tools from the MCP server.
2. Your query is sent to Claude along with tool descriptions.
3. Claude analyzes the available tools and decides which one(s) to use. In this case some tool related to getting weather forecast. Send the decision to MCP client.
4. The client executes the chosen tool(s) through the MCP server, since tools is in the server.
5. Results (Weather forecast) are sent back to Claude.
6. Claude formulates a natural language response.
7. The response is displayed to you.

1. Anthropic's Official Announcement on MCP
2. Anthropic's MCP Documentation
3. InfoQ's Coverage on MCP
4. Forbes Article on MCP's Impact
5. The Verge's Report on MCP Launch

