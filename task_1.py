class Animals:
    """ Базовый класс животные."""

    def __init__(self, name: str, age: int, weight: float, sound: str):
        """
        Инициализация атрибутов класса
        :param name: Название животного, защищенный атрибут,
        так как у каждого животного должны быть свои
        характеристики
        :param age: Возраст животного
        :param weight: Вес животного
        :param sound: Звук, издаваемый животным, защищенный
        атрибут, так как для экземпляров базового класса животное
        может издавать только один специфический звук
        """
        self._name = name
        self.age = age
        self.weight = weight
        self._sound = sound

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, new_age: int) -> None:
        if not isinstance(new_age, int):
            raise TypeError("Возраст должен быть типа int")
        if new_age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age: int = new_age

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, new_weight: float) -> None:
        if not isinstance(new_weight, float):
            raise TypeError("Вес должен быть типа float")
        if new_weight < 0:
            raise ValueError("Вес не может быть отрицательным")
        self._weight = new_weight

    @property
    def sound(self) -> str:
        return self._sound

    def __str__(self) -> str:
        return f"Животное: {self.name}. Возраст: {self.age} лет, " \
               f" Вес: {self.weight} кг, Звук: {self.sound}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, " \
               f"age={self.age!r} лет, weight={self.weight!r} кг, sound={self.sound!r})"

    def make_sound(self) -> str:
        """
        Издать звук
        """
        return self.sound


class Cat(Animals):
    """ Дочерний класс: Кот."""

    def __init__(self, name: str, age: int, weight: float, sound: str, color: str):
        """
        Инициализация атрибутов дочернего класса Кот
        :param name: Имя кота
        :param age: Возраст кота
        :param weight: Вес кота
        :param sound: Звук, издаваемый котом
        :param color: Окрас кота
        """

        super().__init__(name, age, weight, sound)
        self.color = color

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        if not isinstance(new_name, str):
            raise TypeError("Имя должно быть типа str")
        self._name = new_name

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        if not isinstance(new_color, str):
            raise TypeError("Цвет должен быть типа str")
        self._color = new_color

    def __str__(self) -> str:
        return f"Имя: {self.name}, Возраст: {self.age} лет, " \
               f"Вес: {self.weight} кг, Звук: {self.sound}, Окрас: {self.color}"

    def make_sound(self):
        """
        Кот издает мяу-мяу!
        Перегрузка метода make_sound, специфичная для кота
        """
        print("Мяу-мяу!")

    def catch_mouse(self) -> str:
        """
        Сообщение о поимке мыши
        """
        return f"{self.name} поймал мышь!"

    @staticmethod
    def meow():
        """
        Мяукнуть
        """
        print("Мяу")


animal_ = Animals("Собака", 3, 10.0, "Гав")
print(animal_)
print(animal_.make_sound())

print(Cat("Мурзик", 4, 5.0, "Муррр", "Черный"))
Cat.meow()

little_cat = Cat("Мурзик", 4, 5.0, "Муррр", "Черный")
print(little_cat.catch_mouse())
little_cat.make_sound()

little_cat.color = "Белый"
print(little_cat)

if __name__ == "__main__":
    pass
