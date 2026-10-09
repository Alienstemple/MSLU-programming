# Класс = данные + код, группировка
# Класс - описание, объект - экземпляр
# "Где это применяется" md
# Картинки


class Cat:
    def __init__(self, name, age):
        self.name = name      # атрибут: имя кошки
        self.age = age        # атрибут: возраст

    def meow(self):          # метод: что кошка умеет делать
        print(f"{self.name}: Мяу!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} теперь {self.age} лет")


# Создаём объекты (экземпляры) класса
murka = Cat("Мурка", 3)
barsik = Cat("Барсик", 5)

murka.meow()          # Мурка: Мяу!
barsik.meow()         # Барсик: Мяу!

murka.birthday()      # Мурка теперь 4 лет
print(barsik.age)     # 5: у Барсика свой возраст

# Состояние - поля, Поведение - методы
# Нет модификаторов доступов, есть соглашение об именах


class CatWithAccess:
    def __init__(self, name, age):
        self.name = name           # публичное поле
        self._mood = "сонная"      # внутреннее поле, договорённость
        self.__age = age           # "приватное" поле, искажение имени (Name mangling)

    @property
    def age(self):                # чтение: murka.age
        return self._age

    @age.setter
    def age(self, value):         # запись: murka.age = 5
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self._age = value

    def __repr__(self):
        return f"Cat({self.name!r}, {self.age})"


murka = CatWithAccess("Мурка", 3)
# print(murka.__age)   # AttributeError: 'CatWithAccess' object has no attribute '__age'

# Методы __str__ и __repr__ для строкового представления объекта
# __str__ - человекочитаемое представление
# __repr__ - для отладки в консоли
# Вызывается так:  murka    str(murka)    repr(murka)
# def __str__(self):
#     return f"{self.name}, {self.age} лет"


# 1 Наследование, 2 абстракция, 3 инкапсуляция (API), 4 полиморфизм - 4 принципа ООП

# ABC - Abstract Base Class
from abc import ABC, abstractmethod


class Animal(ABC):             # наследуем от ABC
    @abstractmethod
    def speak(self):           # метод без реализации, «обещание»
        pass


class CatAnimal(Animal):
    def speak(self):
        return "Мяу"


print(CatAnimal().speak())    # 'Мяу'
# Animal()  # TypeError: Can't instantiate abstract class Animal ...


# Приватные поля не видны наследнику
# Проверка принадлежности
# isinstance(murka, CatWithAccess)   # True
# isinstance(murka, Animal)          # True: кошка является животным
# issubclass(CatAnimal, Animal)      # True

# Наследники переопределяют методы родителя

# Нет final, нельзя наследоваться от некоторых встроенных типов - bool, range, slice, NoneType

# Single responsibility - единственная ответственность