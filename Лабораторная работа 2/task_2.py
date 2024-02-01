BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Созднаие и подготовка к работе объекта "Книга"

        :param id_: Индекс книги
        :param name: Название книги
        :param pages: Страница книги
        """
        self.id_ = id_
        self.name = name
        self.pages = pages


# TODO написать класс Library

class Library:
    def __init__(self, books=None):
        """
        Созднаие и подготовка к работе объекта "Библиотека"

        :param books: Книги
        """
        if books is None:
            self.books = []
        else:
            self.books = books


    def get_next_book_id(self):
        """
        Функция, возвращающая идентификатор для добавления новой книги в библиотеку
        """
        if len(self.books) == 0:
            return 1
        else:
            return self.books[-1].id_ + 1

    def get_index_by_book_id(self, book_id):
        """
        Функция, возвращающая индекс книги в списке, который хранится в атрибуте экземпляра класса
        """
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
            else:
                raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
