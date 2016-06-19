class Animal(object):

    def __init__(self, name='', age=None):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name + ' - ' + str(self.__age)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


a = Animal('cat', 5)
b = Animal()
print(a)
print(b)
print(a.name)
a.name = 'dog'
print(a)

# protected variables starts with _   --->  _password
# private variables starts with __  ---> __password
# it can be accessed with _<class-name>__password but its DANGEROUS!
# hasattr(self, 'attribute') returns true if class has 'attribute' or not
