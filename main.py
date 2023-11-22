# практичне завдання
"""Зміна поведінки операторів класу: Створіть метаклас,
який дозволяє змінювати поведінку різних операторів
(наприклад, +, -, *, /) для об'єктів певного класу."""


class OperatorOverloadMeta(type):
    def __new__(cls, name, bases, dct):
         dct["__add__"] = lambda self, other: self.add(other)
         return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=OperatorOverloadMeta):
    def __init__(self, value):
        self.value = value

    def add(self, other):
        return  self.value + other.value if isinstance(other, MyClass) else self.value + other

obj1 = MyClass(5)
obj2 = MyClass(6)
print(obj1 + obj2)