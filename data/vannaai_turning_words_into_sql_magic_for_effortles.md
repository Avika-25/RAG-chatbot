---
title: Vanna.AI: Turning Words into SQL Magic for Effortless Data Analysis
date: January 17, 2025
url: https://www.buildfastwithai.com/blogs/vanna-ai-turning-words-into-sql-magic-for-effortless-data-analysis
---

# Vanna.AI: Turning Words into SQL Magic for Effortless Data Analysis

## Resources and Community

### Introduction:

### Detailed Explanation:

### Conclusion:

### Resources Section:

#### 1. Installing Vanna.AI

#### 2. Setting Up API Keys

#### 3. Setting Up Vanna.AI with Flask for Database Interaction

#### 4. Extending Vanna.AI with Google Gemini

#### 5. Training Vanna.AI with SQL Queries, DDL, and Documentation

#### 6. Asking Vanna.AI Questions

The best time to start with AI was yesterday. The second best time? Right after reading this post. The fastest way? Gen AI Launch Pad’s 6-week transformation.

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

In today's data-centric world, businesses and organizations rely heavily on databases to store and analyze vast amounts of information. However, interacting with databases can often be a tedious task, especially when it involves writing complex SQL queries. This is where Vanna.AI, an open-source platform, comes into play.

Vanna.AI simplifies the process of interacting with databases by allowing users to issue queries in natural language, which it then translates into SQL. The platform is built with flexibility and ease of use in mind, allowing seamless integration with databases like SQLite and extending functionality with Google’s Gemini model for advanced query capabilities.

In this blog post, we'll walk through the entire process of setting up and using Vanna.AI, including installation, configuration, training the model, and making natural language queries. You'll also see how to integrate the platform with web apps using Flask, and explore how to take advantage of advanced features such as using Gemini for enhanced NLP capabilities.

By the end of this post, you'll not only understand how to get started with Vanna.AI but also gain insights into how this tool can be applied in real-world scenarios for seamless database interaction.

Before you can start using Vanna.AI, you need to install the package and its dependencies in your Python environment. This step ensures you have everything needed to run the code.

To interact with Vanna.AI and Google's services, you need to provide authentication through API keys. These keys are used to verify your identity and authorize access to the services.

Now that your environment is ready, let’s integrate Vanna.AI with a SQLite database and create a Flask app to interact with it. Flask is a lightweight web framework that enables you to create simple web applications in Python.

Google’s Gemini model powers advanced NLP features, allowing Vanna.AI to understand and process more complex natural language queries. This section shows how to combine Vanna.AI with Gemini.

Vanna.AI can be trained to better understand your database by feeding it SQL queries, DDL statements, and documentation about your data structure.

Now that Vanna.AI has been set up and trained, you can ask it natural language questions and retrieve answers directly.

Vanna.AI offers an elegant solution for simplifying database queries through natural language. It provides powerful tools for integrating databases with AI, making it easier for non-technical users to interact with data, automate reporting, and create intelligent systems.

By setting up Vanna.AI with Flask, connecting it to a database, training it with real data, and utilizing the Gemini model for advanced NLP, you can unlock the full potential of Vanna.AI for your projects.

Next, explore integrating this system with other web apps, experiment with more complex queries, or try it out on your own datasets to see how it can help streamline your data analysis.

---------------------------

Stay Updated:- Follow Build Fast with AI pages for all the latest AI updates and resources.

Experts predict 2025 will be the defining year for Gen AI implementation.Want to be ahead of the curve?

Join Build Fast with AI’s Gen AI Launch Pad 2025 - your accelerated path to mastering AI tools and building revolutionary applications.

---------------------------

Join our community of 12,000+ AI enthusiasts and learn to build powerful AI applications! Whether you're a beginner or an experienced developer, this tutorial will help you understand and implement AI agents in your projects.

* Explanation:
* vanna: This is the core package that provides the main functionality for translating natural language into SQL.
* vanna[gemini]: The gemini extra dependency adds support for Google’s Gemini model, which enhances Vanna.AI’s natural language processing (NLP) capabilities. With Gemini, Vanna.AI can handle more complex queries and provide smarter responses.
* Expected Output:
* After running the command, you’ll see output from pip showing that the packages were installed successfully. It will look something like this:

* Real-World Application:
* Installing these dependencies is the first step toward integrating Vanna.AI into your environment. Once installed, you can start using it in your data workflows, whether it's for data analysis, generating reports, or powering automated data retrieval in apps.

* Explanation:
* The userdata.get function pulls the Google API key and Vanna.AI API key from the environment where the code is being executed. This ensures that the keys are securely stored and retrieved without hardcoding them into the script.
* These keys are required for the system to access Google’s resources (for example, Google Gemini for NLP) and Vanna.AI’s services.
* Expected Output:
* There is no direct output here. However, once these keys are successfully retrieved, you’ll be able to connect to the APIs and use their features.
* Real-World Application:
* API keys are essential for managing access to cloud services and external platforms. This method ensures that only authorized users can interact with the system, securing sensitive data.

* Explanation:
* VannaDefault: This is a default class in the Vanna.AI library that connects to a specified model (in this case, ‘chinook’) and uses the provided API key for authentication.
* connect_to_sqlite: This method connects Vanna.AI to a SQLite database hosted at the specified URL (Chinook.sqlite). The database contains various sales and artist data.
* ask: The ask method takes a natural language query and sends it to Vanna.AI, which translates it into an appropriate SQL query. Here, the query is asking for the top 10 artists by sales.
* VannaFlaskApp: This sets up a Flask application to make your Vanna.AI-powered database accessible via the web. Running VannaFlaskApp(vn).run() will start a local web server.
* Expected Output:
* The response will return the top 10 artists by sales, based on the database.
* The Flask app will start running, and you can access it at http://localhost:5000 (or a similar address).
* Example response to the query might look like:

* Real-World Application:
* Flask is a great tool for creating web-based interfaces for databases. By setting up Vanna.AI with Flask, you can create applications where users can query databases using natural language.
* This is useful for creating dashboards, chatbots, or customer-facing tools that allow users to interact with data without knowing SQL.

* Explanation:
* This code defines a new class, MyVanna, that combines two classes: VannaDB_VectorStore for database interaction and GoogleGeminiChat for advanced natural language understanding.
* The GoogleGeminiChat class is initialized with the Google API key and the Gemini model (gemini-2.0-flash-exp), which allows Vanna.AI to process more sophisticated language queries.
* VannaDB_VectorStore connects Vanna.AI to your SQLite database, so you can retrieve information based on the data stored.
* Expected Output:
* This class is now configured to process advanced queries. While there’s no immediate output from this block, you’ll have a more powerful model ready to handle complex questions.
* Real-World Application:
* Combining Vanna.AI with Google Gemini allows for more nuanced understanding of natural language queries. This is particularly useful when dealing with complex datasets where a basic model might struggle with phrasing or context.

* Explanation:
* train(sql=...): This method allows you to train the model with a specific SQL query. It helps Vanna.AI learn how to execute similar queries in the future.
* train(ddl=...): This is where you train Vanna.AI with Data Definition Language (DDL), which defines the structure of the database (e.g., creating tables).
* train(documentation=...): This method adds documentation to help Vanna.AI understand what each table or field represents. In this case, it explains that the Artist table contains information about music artists.
* Expected Output:
* While no output is immediately shown, the model is now more "intelligent" and can process SQL queries, DDL, and documentation more accurately.
* Real-World Application:
* Training Vanna.AI is crucial when working with custom or complex databases. By providing it with relevant data, it becomes more efficient and accurate in understanding and querying your data.

* Explanation:
* The ask method sends a natural language query to Vanna.AI, which converts it into an SQL query and retrieves the relevant data from the database.
* In this case, the query asks for the top 10 artists by sales, and the result will be printed out.
* Expected Output:
* The response will be a list of tuples representing the top 10 artists by sales, for example:

* Real-World Application:
* The ability to ask questions in natural language and receive database-driven responses is immensely valuable for non-technical users. Whether for customer support, business reporting, or even interactive dashboards, this functionality makes data much more accessible.

* Vanna.AI GitHub Repository
* Google Gemini Documentation
* Flask Documentation
* Vanna.AI Build Fast With AI Detailed Notebook

* Website: www.buildfastwithai.com
* LinkedIn: linkedin.com/company/build-fast-with-ai/
* Instagram: instagram.com/buildfastwithai/
* Twitter: x.com/satvikps
* Telegram: t.me/BuildFastWithAI

```
vanna
```

```
vanna[gemini]
```

```
gemini
```

```
userdata.get
```

```
VannaDefault
```

```
connect_to_sqlite
```

```
Chinook.sqlite
```

```
ask
```

```
ask
```

```
VannaFlaskApp
```

```
VannaFlaskApp(vn).run()
```

```
http://localhost:5000
```

```
MyVanna
```

```
VannaDB_VectorStore
```

```
GoogleGeminiChat
```

```
GoogleGeminiChat
```

```
gemini-2.0-flash-exp
```

```
VannaDB_VectorStore
```

```
train(sql=...)
```

```
train(ddl=...)
```

```
train(documentation=...)
```

```
Artist
```

```
ask
```

