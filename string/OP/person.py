from datetime import datetime


class Person():

    def __init__(self):
        self.__birth_day = datetime.now()
        self.name = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_birth_day(self):
        return self.__birth_day


class Human(Person):

    def __init__(self, name):
        super().__init__()
        self._name = name


class Man(Human):

    __sex = "M"

    def get_sex(self):
        return self.__sex


class Woman(Human):

    __sex = "F"

    def get_sex(self):
        return self.__sex

    @classmethod
    def test(cls,arg):
        print(arg)
        print(cls.__sex)


if __name__ == '__main__':
    Masha = Woman("Masha")
    print(Masha.get_name())
    Vasya = Man("Vasya")
    print(Vasya.get_name())
    print(Vasya.get_birth_day())

    print(Masha.get_sex())
    print(Vasya.get_sex())

    Woman.test("!!!!")
