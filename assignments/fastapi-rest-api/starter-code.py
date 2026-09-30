from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


books = [
    {"id": 1, "title": "The Hobbit", "author": "J. R. R. Tolkien", "year": 1937},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "year": 1962},
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books")
def list_books():
    # TODO: Return all books in the collection.
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    # TODO: Find the book by ID, or raise HTTPException with status code 404.
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    # TODO: Assign a unique ID, add the book to the collection, and return it.
    pass
