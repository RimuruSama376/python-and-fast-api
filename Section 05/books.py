from fastapi import FastAPI

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
    }
]


@app.get("/books")
async def read_all_books():
    return Books


@app.get('/books/{index}')
async def get_book_by_index(index: int):
    print('index: ', index)
    if 0 <= index < len(Books):
        return Books[index]
    return "Invalid Index"
