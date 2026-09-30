# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API for a book collection using FastAPI. Practice defining routes, returning JSON, accepting request data, and choosing appropriate HTTP status codes.

## 📝 Tasks

### 🛠️ Create the FastAPI App and Health Route

#### Description
Complete `starter-code.py` and start the app locally. Install FastAPI and Uvicorn if they are not already available:

```bash
python -m pip install fastapi uvicorn
uvicorn starter-code:app --reload
```

#### Requirements
Completed program should:

- Create a FastAPI application named `app`.
- Respond to `GET /health` with the JSON object `{"status": "ok"}`.
- Make the interactive API documentation available at `/docs`.

### 🛠️ Add Book Read Routes

#### Description
Use the starter collection to add routes for listing all books and looking up one book by its ID.

#### Requirements
Completed program should:

- Respond to `GET /books` with all books as a JSON array.
- Respond to `GET /books/{book_id}` with the matching book, including its `id`, `title`, `author`, and `year` fields.
- Return HTTP 404 when the requested book ID does not exist.

### 🛠️ Add a Route to Create Books

#### Description
Use the provided `BookCreate` request model to accept a new book and add it to the in-memory collection.

#### Requirements
Completed program should:

- Accept a `POST /books` request with `title`, `author`, and `year` fields.
- Assign the new book a unique integer ID and include it in the response.
- Return the created book with HTTP 201 status.

Example request body:

```json
{"title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937}
```
