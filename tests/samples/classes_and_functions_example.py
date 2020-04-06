
class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def print1():
        print('q')

    @staticmethod
    def Print2():
        print('q')

    @staticmethod
    def _print3():
        print('q')
