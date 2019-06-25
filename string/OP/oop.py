class AClass():
    name = "Sasha"

    def __init__(self, name, first_name):
        self.name = name
        self.first_name = "Trasenko"

if __name__ == '__main__':
    a = AClass("A", "Object")
    b = AClass("B", "Object")
    a.atr1 = 1
    print(dir(a))
    print(dir(b))
    print(a.__dict__)
    print(b.__dict__)
    print(a.name)
    print(b.name)
    print(a.first_name)
    print(b.first_name)
    print(a)
    print(b)
