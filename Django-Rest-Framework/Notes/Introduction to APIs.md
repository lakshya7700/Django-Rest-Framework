# What is an API?

It stands of Application Programming Interface.

## For example: 

Imagine you are a user who wants something from the web, like information or a service.
You connect to web services and send a request to a web server.

Will the web server give you a response to that request? Is it capable of providing the exact response you need?
The answer is NO.

For this purpose, we build APIs. APIs are programs designed to give you the correct response for your request.
They determine what service is being asked for and ensure the correct response is sent back to the user.

## lets take a more simplified example

Suppose you go to a restaurant. There are many types of cuisines to choose from. You call the waiter and tell them that you want Chinese food. The waiter goes to the chef and communicates your order.

Later, you decide you want a dessert. Again, you call the waiter, who informs the chef, and you receive your order.

You don’t directly go to the chef to ask for the food you want.
In this analogy:

- The waiter is the API.
- The chef is the database/server where all the information or services are stored.

I hope this gives you a much clearer idea of what an API is and why it’s used.

# Types of API

- REST API
- SOAP API
- RPC API
- GraphQL

# REST API

REST API stands for Representational State Transfer API. It follows specific constraints or rules to ensure proper functionality. By adhering to these rules, we create RESTful APIs.

## Rules

1. CSA (Client Server Architecture): 
- The client and server should be independent of each other.
- Any data or information exchanged between the client and server should not depend on the server's state or time.

2. Stateless:
- The server should not store any information about previous requests.
- Each request from the client should be treated as independent and new.

3. Layered System:
- In a multi-layered architecture, changes made in one layer (e.g., the first layer) should not impact other layers or vice versa.
- Each layer operates independently.

4. Uniformed interface:
- Changes made on the client side should not affect the API or server.
- Similarly, changes in the server should not impact the client or API.
- The interface between the client and server remains consistent.

5. Cashebility:
- If the same request is sent repeatedly, the server can cache the response and send the cached response for identical requests.
- This reduces processing time and improves efficiency.

If an API follows all these rules, it is considered a RESTful API.

# GRAPHQL

It stands for graph querry language.

# SOAP API

It stands for simple object access protocol

# RPC API

It stands for remote procedure call
