---
title: Serverless PostgreSQL & AI: NeonDB with pgvector
date: February 14, 2025
url: https://www.buildfastwithai.com/blogs/what-is-neondb-serverless-postgresql
---

# Serverless PostgreSQL & AI: NeonDB with pgvector

## Introduction

## Getting Started with Neon PostgreSQL

## Implementing Vector Search with pgvector

## Building an Interactive To-Do List App

## OpenAI Chatbot with NeonDB

## Conclusion

## Resources

## Resources and Community

### Step 1: Connect to Neon PostgreSQL

### Step 2: Test the Database Connection

### Step 3: Install and Set Up pgvector

### Step 4: Create a Table and Insert Vector Data

### Step 5: Perform a Vector Similarity Search

### Step 6: Create the To-Do List Table

### Step 7: Add a New Task

### Step 8: View All Tasks

### Step 9: Delete a Task

### Step 10: Store Chat History in NeonDB

Do you want to be remembered as someone who waited or someone who created?

Gen AI Launch Pad 2025 is your platform to innovate.

In the world of AI-driven applications, database performance and scalability are crucial. Neon is an open-source, serverless PostgreSQL database that introduces cutting-edge features like autoscaling, branching, and vector support (pgvector). This makes it an ideal choice for AI workloads, real-time analytics, and scalable cloud applications.

In this blog, we’ll explore how to leverage Neon’s features to create scalable applications. We’ll walk through:

Before diving into code, let's take a quick look at Neon’s key features:

First, let’s connect to a Neon database using Python and psycopg2.

Explanation:

Before proceeding, let’s ensure our database connection is successful:

Explanation:

Expected Output:

To perform vector similarity searches, we first need to install the pgvector extension in Neon.

Explanation:

Let’s create a table that stores vector embeddings:

Explanation:

Explanation:

Expected Output:

Explanation:

Explanation:

Explanation:

Explanation:

Explanation:

NeonDB provides a powerful, scalable, and serverless PostgreSQL experience, making it perfect for AI applications. Whether you’re implementing vector search, task management, or AI chatbots, Neon simplifies the process.

---------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI Implementation. Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

---------------------------

Join our community of 12,000+ AI enthusiasts and learn to build powerful AI applications! Whether you're a beginner or an experienced developer, this tutorial will help you understand and implement AI agents in your projects.

* Setting up a serverless PostgreSQL database.
* Running vector similarity searches with pgvector.
* Creating an interactive to-do list application.
* Implementing an AI chatbot with OpenAI and NeonDB.

* Open Source: Transparent and free to use.
* Serverless: No infrastructure management required.
* Autoscaling: Automatically adjusts resources based on demand.
* Branching: Clone databases instantly for testing and development.
* Vector Search (pgvector): Optimized for AI and embedding-based searches.
* Fully PostgreSQL-Compatible: Works with all PostgreSQL tools and extensions.

* We retrieve the database URL from Google Colab’s userdata.
* Establish a connection to the database.
* Create a cursor to execute SQL queries.

* Executes a simple SELECT 1; query to test the connection.
* If the query returns (1,), the connection is successful.

* Ensures that the pgvector extension is installed and available in the database.

* Creates a table items with a BIGSERIAL primary key and a 3-dimensional vector column.
* Inserts vector data to be used for similarity searches.

* Uses the <-> operator to compute similarity between vectors.
* Retrieves the top 3 nearest vectors to [3,1,2].

* Creates a tasks table with an id, task description, and a completed status.

* Inserts a new task into the tasks table.
* Commits the transaction to save the task.

* Retrieves all tasks from the tasks table.
* Displays each task along with its completion status.

* Deletes a task by its id from the database.
* Commits the deletion to update the database.

* Creates a chat_history table to store user queries and chatbot responses.

* Neon Official Documentation
* pgvector Extension Guide
* PostgreSQL Official Site
* Neon Experiment Notebook

* Website: www.buildfastwithai.com
* LinkedIn: linkedin.com/company/build-fast-with-ai/
* Instagram: instagram.com/buildfastwithai/
* Twitter: x.com/satvikps
* Telegram: t.me/BuildFastWithAI

```
userdata
```

```
SELECT 1;
```

```
(1,)
```

```
pgvector
```

```
items
```

```
BIGSERIAL
```

```
[3,1,2]
```

```
tasks
```

```
id
```

```
task description
```

```
completed
```

```
tasks
```

```
tasks
```

```
id
```

```
chat_history
```

