class MyMeta(type):
    def __new__(cls, name, bases, dct):
        #маніпуляція з класом
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    attr = 10
    def metod(self):
        pass
