from fastapi import FastAPI, Body

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


Books = [
    Book(1, "To Kill a Mockingbird", "Harper Lee", "A novel about the serious issues of rape and racial inequality.",
         "4.8"),
    Book(2, "Go Set a Watchman", "Harper Lee", "A novel about Scout Finch's return to Maycomb.", "4.2"),
    Book(3, "1984", "George Orwell",
         "A dystopian social science fiction novel and cautionary tale about the dangers of totalitarianism.", "4.7"),
    Book(4, "Animal Farm", "George Orwell", "A satirical allegorical novella about the rise of totalitarianism.",
         "4.5"),
    Book(5, "The Great Gatsby", "F. Scott Fitzgerald", "A novel about the American dream and the roaring twenties.",
         "4.6"),
    Book(6, "Tender Is the Night", "F. Scott Fitzgerald",
         "A novel about the rise and fall of Dick Diver, a promising young psychiatrist.", "4.3"),
    Book(7, "Pride and Prejudice", "Jane Austen",
         "A romantic novel that charts the emotional development of the protagonist Elizabeth Bennet.", "4.7"),
    Book(8, "Emma", "Jane Austen", "A novel about youthful hubris and romantic misunderstandings.", "4.5"),
    Book(9, "Moby-Dick", "Herman Melville", "A novel about the voyage of the whaling ship Pequod.", "4.2"),
    Book(10, "War and Peace", "Leo Tolstoy", "A historical novel that chronicles the French invasion of Russia.",
         "4.5"),
    Book(11, "Anna Karenina", "Leo Tolstoy", "A novel about a tragic adulterous love affair.", "4.6"),
    Book(12, "The Catcher in the Rye", "J.D. Salinger",
         "A novel about the experiences of a young man named Holden Caulfield.", "4.3"),
    Book(13, "Franny and Zooey", "J.D. Salinger",
         "A book consisting of two interconnected stories about the Glass family.", "4.1")
]


@app.get("/Books")
def read_all_book():
    return Books
