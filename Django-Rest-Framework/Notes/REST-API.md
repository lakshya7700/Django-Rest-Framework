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

6. Code on demand (Optional)

If an API follows all these rules, it is considered a RESTful API.


Your note conveys the concept, but the explanation can be made clearer and grammatically polished. Here's the revised version:

If some of the constraints of REST are not being followed, or if certain constraints contradict others, the API is referred to as a Partial RESTful API.

The term Partial RESTful API is used when not all REST architectural constraints are adhered to in the design of the API.

### Common reasons for this can include:

- Skipping statelessness or uniform interface rules.
- Designing the system to be dependent on client-server coupling, which violates REST's independence principle.
- Such APIs may still function but do not fully qualify as RESTful APIs due to the lack of adherence to the required constraints.

# GRAPHQL

GraphQL stands for Graph Query Language. It is a modern technology developed by Facebook to address some of the limitations of REST APIs.

## Difference between REST API and GRAPH-QL

1. Over-fetching/Under-fetching:

In REST APIs, over-fetching or under-fetching data can be a common issue. Over-fetching occurs when more data than necessary is retrieved, while under-fetching means retrieving insufficient data, requiring additional requests.

GraphQL solves this by allowing clients to specify exactly what data they need in a single query, ensuring optimized data retrieval.

2. API Design

In REST APIs, different endpoints must be created for different operations, such as creating, updating, or deleting resources.

GraphQL eliminates this redundancy by using a single endpoint. It processes queries and mutations to retrieve or modify data as per the client’s requirements.

3. Format:

REST APIs support multiple data formats like JSON, XML, or HTML.
GraphQL strictly uses JSON for communication.

4. Usage:

REST APIs are often used for public APIs and resource-driven architectures.

GraphQL is more suitable for complex systems, mobile APIs, and microservices where flexibility and efficiency in data fetching are critical.

While GraphQL is a powerful alternative to REST APIs, the primary focus of this repository remains on REST API concepts.