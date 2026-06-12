# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework. You will define request and response models, create endpoints, and practice validating and handling HTTP requests.

## 📝 Tasks

### 🛠️ Task 1: Set up the FastAPI application

#### Description
Create the basic FastAPI app structure and start the server locally.

#### Requirements
Completed project should:

- Import `FastAPI` and create an `app` instance
- Include at least one route that returns a simple JSON message
- Provide a command example for running the API with `uvicorn`


### 🛠️ Task 2: Define models and endpoints

#### Description
Use Pydantic models to define the data structure of API requests and responses. Create routes to read and modify item data.

#### Requirements
Completed project should:

- Create a Pydantic model for an item with fields such as `id`, `name`, `description`, and `price`
- Add a `GET` endpoint to return item details by ID
- Add a `POST` endpoint to create a new item
- Use an in-memory dictionary or list to store sample items


### 🛠️ Task 3: Validate input and test the API

#### Description
Add request validation and test your API endpoints to ensure they behave correctly.

#### Requirements
Completed project should:

- Validate request data using Pydantic field types and optional fields
- Return a `404` response when an item is not found
- Include at least one example HTTP request for testing the API with `curl` or a browser
