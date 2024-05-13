from fastapi import FastAPI, Body

app = FastAPI()

Books = [
    {
        'title': 'Mystery of the Ancient Ruins',
        'author': 'Clara Bell',
        'category': 'Mystery',
        'year': 2019,
        'publisher': 'Adventure Press',
        'isbn': '987-6543210987'
    },
    {
        'title': 'The Last of the Sky Pirates',
        'author': 'Eliot Reed',
        'category': 'Fantasy',
        'year': 2023,
        'publisher': 'Skybound Books',
        'isbn': '564-7382910564'
    },
    {
        'title': 'Quantum Web',
        'author': 'Lara Joyce',
        'category': 'Science Fiction',
        'year': 2022,
        'publisher': 'Future Worlds',
        'isbn': '348-1122334456'
    },
    {
        'title': 'Gardens of the Moon',
        'author': 'Steven Erikson',
        'category': 'Fantasy',
        'year': 1999,
        'publisher': 'Bantam Books',
        'isbn': '978-0553819571'
    },
    {
        'title': 'Gardens of the Moon',
        'author': 'Steven Erikson',
        'category': 'Fantasy',
        'year': 1999,
        'publisher': 'Bantam Books',
        'isbn': '978-0553819571'
    },
    {
        'title': 'The Enchanted Forest',
        'author': 'Helena York',
        'category': 'Fantasy',
        'year': 2018,
        'publisher': 'Mythical Press',
        'isbn': '200-1234567890'
    }
]


@app.get("/books")
async def read_all_books():
    return Books


# Path parameters
@app.get('/books/{index}')
async def get_book_by_index(index: int):
    print('index: ', index)
    if 0 <= index < len(Books):
        return Books[index]
    return "Invalid Index"


# Query Params
@app.get("/books/")
async def get_books_by_category(category: str):
    books_to_return = []
    for book in Books:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/add_book")
async def add_new_book(new_book=Body()):
    Books.append(new_book)
    print(new_book)
    return "Book added successfully"
