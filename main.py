# практичне завдання
"""Метаклас для кешування результатів методів класу:
 Реалізуйте метаклас, який автоматично кешує
 результати виклику методів класу для підвищення швидкодії."""


class Cached(type):
    def __new__(cls, name, bases, dct):
        cache = {}

        def wrap_method(method):
            def wrapped(*args, **kwargs):
                cache_key = (method.__name__, args, frozenset(kwargs.items()))
                if cache_key not in cache:
                    cache[cache_key] = method(*args, **kwargs)
                print(cache)
            return wrapped
        for attr_name, attr_value in dct.items():
            if callable(attr_value):
                dct[attr_name] = wrap_method(attr_value)
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=Cached):
    def calculate(self, x):
        return print(f"Розрахунок для {x} - {x ** 2}")
obj = MyClass()
obj.calculate(5)
obj.calculate(100)
obj.calculate(120)