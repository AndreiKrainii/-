class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Дочерний класс книги: бумажная книга."""
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        if not isinstance(new_pages, int):
            raise TypeError("Число страниц должно быть типа int")
        if new_pages < 0:
            raise ValueError("Число страниц должно быть положительным")
        self._pages = new_pages

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}, Страниц: {self.pages}"


class AudioBook(Book):
    """ Дочерний класс книги: аудиокнига."""
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        if not isinstance(new_duration, float):
            raise TypeError("Длительность должна быть типа float")
        if new_duration < 0:
            raise ValueError("Длительность должна быть положительной")
        self._duration = new_duration

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}, Длительность: {self.duration} часа"


print(PaperBook("1984", "Дж. Оруэл", 300))
print(AudioBook("Мастер и Маргарита", "М. А. Булгаков", 20.30))
