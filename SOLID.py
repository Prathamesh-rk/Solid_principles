#SOLID Principles

#1. Single Responsibility Principle

class Animal:
    def __init__(self, name: str):
            self.name = name

    def get_name(self):
        pass


class AnimalDB:
    def get_animal(self) -> Animal:
        pass

    def save(self, animal: Animal):
        pass

#2.Open-Closed Principle

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def get_discount(self):
            return self.price * 0.2


class VIPDiscount(Discount):
    def get_discount(self):
        return super().get_discount() * 2



#3.Liskov Substitution Principle


class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass

#4.Interface Segregation Principle
class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

#5.Dependency Inversion Principle

class Connection:
    def request(self, url: str, options: dict):
        raise NotImplementedError

class NodeHttpService(Connection):
    def request(self, url: str, options:dict):
        pass

class MockHttpService(Connection):
    def request(self, url: str, options:dict):
        pass
