from abc import ABC, abstractmethod, abstractstaticmethod


class IPerson(ABC):

    @abstractmethod
    def person_method(self):
        pass


class Person(IPerson):

    def person_method(self):
        print("I am a person!")


class ProxyPerson(IPerson):

    def __init__(self):
        self.person = Person()

    def person_method(self):
        print("This is proxy")
        self.person.person_method()


if __name__ == "__main__":
    p = ProxyPerson()
    p.person_method()
