from abc import ABC, abstractmethod, abstractstaticmethod


class IPerson(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def type(self):
        pass


class Student(IPerson):

    def __init__(self, name):
        super().__init__(name)

    def type(self):
        print('I am a Student and name is {}'.format(self.name))


class Worker(IPerson):

    def __init__(self, name):
        super().__init__(name)

    def type(self):
        print('I am a Worker and name is {}'.format(self.name))


class Human:

    @staticmethod
    def get_human(type,name):
        if type == "worker":
            return Worker(name)
        elif type == "student":
            return Student(name)
        else:
            raise Exception("Invalid option")


Human.get_human('moko', 'pooja').type()