file = open('dir.txt', 'w+')
print('sezgin', file=file)
file.close()


def display(*args, **kwargs):
    for item in args:
        print(item)

    if 'name' in kwargs:
        name = kwargs.get('name')
        print(name)

lis = ['sezgin', 'cemre', 'resul', 'emir']
display(*lis, name='sezgin')

clubs = {'FB': 1907, 'GS': 1905, 'BJK': 1903, 'TS': 1967}
for key, value in clubs.items():
    print('{} : {}'.format(key, value))


def func(**kwargs):
    print(kwargs)
    print("name in kwargs: ", 'name' in kwargs)

func(name="sezgin", surname="acer")

'''
def dict(**kwargs):  # declaration of dict
    return kwargs

items = dict(name='sezgin', surname='acer')
'''