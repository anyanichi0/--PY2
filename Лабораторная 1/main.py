from datetime import datetime as date
import doctest

 # TODO Написать 3 класса с документацией и аннотацией типов

class Contact:
    def __init__(self, name: str, sname: str):
        """Создание
        @param: str Name of your bud
        @param: str Surname of your bud
        Примеры:
        >>> contact = Contact('Olya', 'Shishina')  # инициализация экземпляра класса
        """
        self.name = name
        self.sname = sname

    def __str__(self) -> str:
        """
        Вывод полного имени

        :returns: Полное имя
        :rtype: str

        Пример:
        >>> contact = Contact('Olya', 'Shishina')  # инициализация экземпляра класса
        """
        return self.name+' '+self.sname

    def walk(self):
        """This books are made for Walking"""
        print('Walking...')


class Backpack:
    def __init__(self, name: str, contact: Contact):
        """Создание
        @param: str Name of your bag
        @param: Contact Contact of your bud
        Примеры:
        >>> bp = Backpack('BackP1', Contact('Olya', 'Shishina'))  # инициализация экземпляра класса
        """
        self.name = name
        self.contact = contact

    def __str__(self) -> str:
        """
        Вывод названия и владельца

        :returns: Название и владелец
        :rtype: str

        Пример:
        >>> bp = Backpack('BP1', Contact('Olya', 'Shishina'))  # инициализация экземпляра класса
        """
        return self.name + ' владеет ' + self.contact.name+' '+self.contact.sname

    def walk(self):
        """This books are made for Walking"""
        print('Walking...')


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
