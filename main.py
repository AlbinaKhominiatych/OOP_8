class MyMeta(type):
    def __new__(cls, name, bases, dct):
        #маніпуляція з класом
        dct["attr"] = 100
        print(name)
        print(bases)
        print(dct)
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=MyMeta):
    attr = 10
    def metod(self):
        pass
print(dir(MyClass))
obj = MyClass()
print(obj.attr)