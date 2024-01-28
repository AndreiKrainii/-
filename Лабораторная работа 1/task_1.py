# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Book:
    def __init__(self, name: str, author: str, year: int):
        """"
        Создание и подготовка к работе объекта "Книга"

        :param name: Название книги
        :param author: Автор книги
        :param year: Год публикации книги

        Пример:
        >>> book = Book("1984", "George Orwell", 1949) # инициализация экземпляра класса
        """
        if not isinstance(name, (str)):
            raise TypeError("Название должено быть типа str")
        self.name = name
        if not isinstance(author, (str)):
            raise TypeError("Автор должен быть типа str")
        self.author = author
        if not isinstance(year, (int)):
            raise TypeError("Год должен быть типа int")
        if year < 0:
            raise ValueError("Год не может быть отрицательным")
        self.year = year

    def change_name(self, new_name: str) -> None:
        """"
        Функция заменяет название книги

        :param new_name: Новое название

        Пример:
        >>> book = Book("1984", "George Orwell", 1949)
        >>> book.change_name("Animal Farm")
        """
        if not isinstance(new_name, (str)):
            raise TypeError("Новое название должено быть типа str")
        ...

    def is_book_exist(self) -> bool:
        """
        Функция проверяет существует ли книга

        :return: Существует ли книга

        Пример:
        >>> book = Book("1984", "George Orwell", 1949)
        >>> book.is_book_exist()
        """
        ...

class Fruit:
    def __init__(self, fruit_name: str, color: str, expiration_date: int):
        """"
            Создание и подготовка к работе объекта "Фрукт"

            :param fruit_name: Название фрукта
            :param color: Цвет фрукта
            :param expiration_date: Срок годности

            Пример:
            >>> fruit = Fruit("Банан", "желтый", 5) # инициализация экземпляра класса
            """
        if not isinstance(fruit_name, (str)):
            raise TypeError("Название должено быть типа str")
        self.fruit_name = fruit_name
        if not isinstance(color, (str)):
            raise TypeError("Цвет должен быть типа str")
        self.color = color
        if not isinstance(expiration_date, (int)):
            raise TypeError("Срок годности должен быть типа int")
        if expiration_date < 0:
            raise ValueError("Срок годности  не может быть отрицательным")
        self.expiration_date = expiration_date

    def  is_expiration_date_is_end (self, day: int) -> None:
        """
        Функция проверяет срок годности фрукта

        :param day: Текущий день

        Пример:
        >>> fruit = Fruit("Банан", "желтый", 5)
        >>> fruit.is_expiration_date_is_end(6)
        """
        if not isinstance(day, (int)):
            raise TypeError("Текущий день должен быть типа int")
        if day < 1:
            raise ValueError("Текущий день не может быть меньше первого")
        self.day = day
        ...

    def buy_new_fruit(self, new_fruit: str, expiration_date: int) -> None:
        """
        Функция выполняет закупку нового фрукта по названию и сроку годности

        :param new_fruit: Навзвание нового фрукта
        :param expiration_date: Срок годности

        Пример:
        >>> fruit = Fruit("Апельсин", "оранжевый", 1)
        >>> fruit.buy_new_fruit("Апельсин", 10)
        """
        if not isinstance(new_fruit, (str)):
            raise TypeError("Название должено быть типа str")
        self.new_fruit = new_fruit
        if not isinstance(expiration_date, (int)):
            raise TypeError("Срок годности должен быть типа int")
        if expiration_date < 0:
            raise ValueError("Срок годности  не может быть отрицательным")
        self.expiration_date = expiration_date
        ...


class Rectangle:
    def __init__(self, side_a: (int, float), side_b: (int, float)):
        """
        Создание и подготовка к работе объекта "Прямоугольник"

        :param side_a: Сторона "a"
        :param side_b: Сторона "b"

        Пример:
        >>> rectangle = Rectangle(10, 20)
        """
        if not isinstance(side_a, (int, float)):
            raise TypeError("Сторона должна  быть int или float")
        if side_a <= 0:
            raise ValueError("Сторона должна быть положительным числом")
        self.side_a = side_a

        if not isinstance(side_b, (int, float)):
            raise TypeError("Сторона должна  быть int или float")
        if side_b <= 0:
            raise ValueError("Сторона должна быть положительным числом")
        self.side_b = side_b

    def calculate_square(self, square: (int, float)) ->None:

        """
        Функция вычисляет площадь прямоугольника

        :param square: Площадь прямоугольника
        :raise ValueError: Если площадь отрицательная, то возвращается ошибка

        :return: Значение площади

        Пример:
        >>> rectangle = Rectangle(10, 10)
        >>> rectangle.calculate_square(100)
        """

        if not isinstance(square, (int, float)):
            raise TypeError("Площадь должна быть int или float")
        if square <= 0:
            raise ValueError("Площадь должна быть положительным числом")
        self.square = square
        ...

    def calculate_perimetr (self, perimetr: (int, float)) ->None:

        """
        Функция вычисляет периметр прямоугльника

        :param perimetr: Периметр прямоугольника
        :raise ValueError: Если периметр отрицательный, то возвращается ошибка

        :return: Значение периметра

        Пример:
        >>> rectangle = Rectangle(10, 20)
        >>> rectangle.calculate_square(60)
        """
        if not isinstance(perimetr, (int, float)):
            raise TypeError("Периметр должен быть int или float")
        if perimetr <= 0:
            raise ValueError("Периметр должен быть положительным числом")
        self.perimetr = perimetr
        ...

if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
