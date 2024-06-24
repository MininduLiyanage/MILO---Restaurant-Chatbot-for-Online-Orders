# MILO - Restaurant Chatbot for online orders using Dialogflow-MySQL-FastAPI

Welcome to the repository for **MILO**, a sophisticated chatbot designed to streamline the process of placing, tracking, and managing online orders for a restaurant. Built using **Dialogflow**, **FastAPI**, and **MySQL**, MILO leverages Natural Language Processing (**NLP**) techniques to understand and interact with users in a natural, conversational manner.

## Project Overview
MILO is more than just a chatbot; it's a complete solution for managing online orders in a restaurant setting. By integrating advanced technologies and platforms, MILO offers a seamless experience for customers to place orders, track their status, and manage them effectively.

## Key Features
**Dialogflow Integration**: MILO is trained using Dialogflow to handle various intents related to online orders, including placing new orders, tracking existing ones, completing orders, or removing items from an order. Dialogflow's robust NLP capabilities allow MILO to understand and process natural language queries effectively.

**NLP Techniques**: The chatbot employs Named Entity Recognition (NER) to identify food items, quantities, and user commands within the conversation. This ensures that MILO can accurately understand and execute user requests.

**FastAPI Backend**: The project uses FastAPI to build a high-performance backend for MILO. FastAPI provides a flexible and scalable framework to manage API requests and interactions seamlessly.

**MySQL Database**: MySQL is used to store and manage all the data related to food items, their IDs, prices, and the orders placed by users. This includes storing information on order contents, total order prices, order status, and more. Custom SQL functions are implemented to retrieve item prices and calculate the total cost of orders dynamically.

## Project Structure
**main.py**: The core of the application, running the FastAPI server and managing the interaction between the chatbot and the database.

**db_func.py**: Contains functions for interacting with the MySQL database, such as fetching food item details, tracking order statuses, and calculating prices.

**helper_func.py**: Includes auxiliary functions that support various operations within the application, enhancing its functionality and efficiency.
