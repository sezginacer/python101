def adder(first=0, second=0):
    """adds two numbers"""
    return first + second

print(adder.__class__)
print(adder.__doc__)


def doubler(func):
    def g(a, b):
        return 2 * func(a, b)
    return g

g = doubler(func=adder)
print(g(2, 3))

a, *args, b = [2, 3, 3, 5, 6]
print(args)


@doubler
def subtractor(a, b):
    return a - b

# subtractor = doubler(subtractor)

print(subtractor(5, 1))


def honorific(cls):
    class HonorificCls(cls):
        @property
        def fullname(self):
            return 'Eng. ' + super(HonorificCls, self).fullname
    return HonorificCls


@honorific  # @honorific
class Name(object):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return ' '.join([self.first, self.last])

me = Name('Sezgin', 'ACER')
# print(me.fullname)
print("fullname : {0}".format(me.fullname))
# or me = honorific(Name)('Sezgin', 'ACER')
# print(me.fullname)
a = dir(adder)
b = dir(adder())

print("len a: {0}, len b: {1}".format(len(a), len(b)))
c = open("dir.txt", "w+")
c.write(str(a))
c.write('\n')
c.write(str(b))
