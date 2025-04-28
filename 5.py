"""5. Написать функцию, которая в качестве аргументов получает словарь из
элементов, представляющий книги в библиотеке: <код книги>: [<фио
автора>,<книга>] и ФИО автора и определяет коды и наименования всех
книг данного автора. """

library = {
    "001": ["Толстой", "Война и мир"],
    "002": ["Пушкин", "Евгений Онегин"],
    "003": ["Толстой", "Анна Каренина"]
}

def find_books(author):
    result = {}
    for code, (book_author, title) in library.items():
        if book_author == author:
            result[code] = title
    return result

author = input("Введите автора: ")
books = find_books(author)

if books:
    for code, title in books.items():
        print(f"Код: {code}, Книга: {title}")
else:
    print("Книги не найдены")
