import os
print(os.__doc__)

import json

print('JSON version {}'.format(json.__version__))

from operator import attrgetter


class Animal(object):
    """Animal Class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' - ' + str(self.age)

array = [Animal('dog', 5), Animal('cat', 2), Animal('brat', 4), Animal('crocodile', 1), Animal('monkey', 7)]
for item in array:
    print(item)
print("---- sorted ----")
array = sorted(array, key=attrgetter('age'))
for item in array:
    print(item)
