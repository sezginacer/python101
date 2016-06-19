#!/usr/bin/python3.5

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other):
        return Animal(self.name + " - " + other.name, self.age + other.age)

    def __str__(self):
        return self.name + " - " + str(self.age)

a = Animal('aynali', 9)
b = Animal('pastali', 5)
c = Animal('yasta', 7)
d = a + b + c
print(d)
