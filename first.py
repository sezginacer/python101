#! /usr/bin/python3.5

"""" integers """

44 // 3  # rounds to integer
5 ** 3  # 5^3

"""   strings   """

a = 'sezgin\'s phone'  # use \ to avoid errors
print(a)
print(r'sezgin\n cemre')  # use \n as normal text due to r

a = "gaggasd" * 5  # a = 5 times "gassasd"

user = "fox jumps over"

user[-1]  # is last character
user[1:5]  # is "ox j"

user[:7]  # first 7 characters
user[2:]  # except first two chars
len(user)  # return the length of string

"""        lists             """

players = [45, 78, 89, 56]  # list decleration
players.append(52)  # adds 52 to the end of the list
del players

"""         ifs and elses         """

a = 9

if a > 5:
    print(a)
elif a > 10:
    del a
elif a is 9:
    print(a)
else:
    a += 5

"""         for loop        """

foods = ["bread", "beef", "juice", "bacon"]

for f in foods:  # foods[:2], foods[2:] yes this is possbile !!
    f += "me"
    print(f)

for x in range(10):  # 0, 1, 2 ... 9
    print(x)

for x in range(5, 12):  # 5, 6, 7 ... 11
    print(x)

for x in range(10, 40, 5):  # 10, 15, ... 35
    print(x)

"""     while loop      """

backtrack = 0
while backtrack < 10:
    print(backtrack)
    backtrack += 1

"""     break       """

magic = 61
for ts in range(1, 101):
    if ts is magic:
        print(ts, "is a magic number")
        break  # breaks for loop
    else:
        print(ts)

# ****** print(9, " me") --> "9 me"

"""         continue        """

numbers = [2, 5, 12, 15, 18]

for i in range(20):
    if i in numbers:
        print(i, "in the list")
        continue  # skip next lines of codes and go to for loop
    print(i)

"""     functions       """


def function(parameter):
    parameter += 10  # process parameters
    return parameter


def get_gender(gender="unknown"):  # gender's default value is "unknown"
    if gender is "m":
        gender = "Male"
    elif gender is "f":
        gender = "Female"
    print(gender)


get_gender("f")


def dumb(name="sezgin", action="ate", item="tuna"):
    print(name, action, item)


dumb()
dumb("cemre", "studies", "lesson")
dumb(name="cemre", item="meat")
dumb(item="bread")


def add_number(*args):  # takes infinite number of argument *****
    total = 0
    for k in args:
        total += k
    print(total)


add_number(1212, 1221, 2121)


def health_calc(age, apples_rate, cigs_smoked):
    answer = (100 - age) + (apples_rate * 3.5) - (cigs_smoked * 2)
    print(answer)


data = [27, 20, 0]
health_calc(*data)  # * unpacks the arguments

"""         sets            """

groceries = {"milk", "starcrunch", "beer", "duct tape", "beer"}

print(groceries)
if "milk" in groceries:
    print("milk in groceries")

"""         dictionary          """

classmates = {"Tony": "cool but smells", "Emma": "sits behind me", "Lucy": "asks too many guestions"}

print(classmates["Emma"])

for k, v in classmates.items():  # k is key, v is value
    print(k + " " + v)

"""         modules         """

"""
import tuna
tuna.fish()
"""

"""         download file       """

import random
import urllib.request


def download_file(url):
    name = random.randrange(1, 101)
    full_name = str(name) + ".pdf"
    urllib.request.urlretrieve(url, full_name)


try:
    download_file("http://web.itu.edu.tr/~acers/Sezgin.ACER.CV.en.pdf")
except Exception:
    print("Error occured!")

"""         file operations         """

fw = open("samples.txt", "w")
fw.write("İstanbul Technical University\n")
fw.write("İstanbul\n")
fw.close()

fr = open("samples.txt", "r")
text = fr.read()
print(text)
fr.close()

"""         download file - 2 (table-shaped file)      """

from urllib import request

goog_url = "http://some_url"


def download_something(url):
    response = request.urlopen(url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close()


"""         Web Crawler         """

# import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages=1):  # its all about html
    page = 1
    while page < max_pages:
        url = "https://buckysroom.org/trade/search.php?page=" + str(page)
        source_code = request.get(url)
        plaint_text = source_code.text
        soup = BeautifulSoup(plaint_text)
        for link in soup.findAll("a", {"class": "item-name"}):
            href = "https://buckysroom.org" + link.get("href")
            title = link.string
            # print(href)
            # print(title)
            get_single_item_data(href)
            page += 1


def get_single_item_data(item_url):
    source_code = request.get(item_url)
    plaint_text = source_code.text
    soup = BeautifulSoup(plaint_text)
    for item_name in soup.findAll("div", {"class": "i-name"}):
        print(item_name.string)
    for link in soup.findAll("a"):
        href = "https://buckysroom.org" + link.get("href")
        print(href)


try:
    trade_spider()
except Exception:
    print("Error!")

"""         Exceptions          """

try:
    # tuna = int(input("Number: "))
    # tuna = 18 / tuna
    # print(tuna)
    pass
except ValueError:
    print("value error!")  # string entered
except ZeroDivisionError:
    print("zero division!")  # divided by zero
finally:
    print("see you!")  # staff must always be done

"""         classes         """


class Enemy:  # class name had better start with capital letter !!!

    def __init__(self, life):
        self.life = life

    def attack(self):
        print("ouch!!")
        self.life -= 1

    def check_life(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")

    def get_life(self):
        print(self.life)


a = Enemy(1)
a.attack()
a.attack()
a.check_life()
a.attack()
a.attack()
a.check_life()


class Tuna:
    def __init__(self):
        print("object created!")

    def swim(self):
        print("I am swimming")


tuna = Tuna()
tuna.swim()


class Girl:
    gender = "female"  # this is class variable

    def __init__(self, name):
        self.name = name  # this is instance variable


leyla = Girl("Leyla")
seda = Girl("Seda")

"""         inheritance         """


class Parent:
    def print_last_name(self):
        print("ACER")


class Child(Parent):
    def print_first_name(self):
        print("Sezgin")

    def print_last_name(self):  # override print_last_name in Parent class
        print("ACAR")


me = Child()
me.print_first_name()
me.print_last_name()


class Mario:
    def move(self):
        print("I am moving!")


class Shroom:
    def eat_shroom(self):
        print("Now I am big!")


class BigMario(Mario, Shroom):
    pass


mario = BigMario()
mario.eat_shroom()
mario.move()

"""         threading           """

import threading


class Messenger(threading.Thread):
    def run(self):
        for _ in range(10):  # if variable wont be used, then use _
            print(threading.current_thread().getName())


x = Messenger(name="Send out messages")
y = Messenger(name="Receive messages")
x.start()
y.start()

"""         word counter        """

import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    for post_text in soup.findAll("a", {"class": "index_singleListingTitles"}):
        content = post_text.string
        words = content.lower().split()  # split() splits from spaces
        for each_word in words:
            word_list.append(each_word)
            # print(each_word)
    clean_up_list(word_list)


def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        sysbols = "é!'^+%&/()=?_;:\".,"
        for i in range(0, len(sysbols)):
            word = word.replace(sysbols[i], "")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)


def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):  # 1 means sort by value
        print(key, value)


try:
    start("https://buckysroom.org/tops.php?type=text&period=this-month")
except:
    print("Error!")
finally:
    print("I am done..")

"""         unpack list or tuples       """

item = ["December 23, 2015", "Bread Gloves", 2.55]
date, name, price = item
print(date, name, price)


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([45, 55, 75, 12])

"""         zip         """

first = ["Bucky", "Tom", "Taylor"]
last = ["Roberts", "Hanks", "Swift"]
names = zip(first, last)
for a, b in names:
    print(a, b)

"""     lambda      """

answer = lambda x: x * 7  # inline function
answer(5)

"""         min, max, sorting       """

stocks = {
    "GOOG": 520.24,
    "FB": 76.45,
    "YHOO": 39.45,
    "AMZN": 306.21,
    "AAPL": 99.76
}

print(min(zip(stocks.values(), stocks.keys())))  # min according to values (first  parameter)
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))

"""         pillow (image mani lib)         """

from PIL import Image

try:
	img = Image.open("img.jpg")
	print(img.size)
	print(img.format)
	area = (100, 100, 100, 100)
	cropped_image = img.crop(area)
except:
	print("Error!")
# img.show()

# cropping image

area = (100, 100, 100, 100)
#cropped_image = img.crop(area)
# cropped_image.show()

"""         struct          """

from struct import *

# store as bytes data

packed_data = pack("iif", 6, 9, 15.73)  # i stands for integer, f for float
print(packed_data)

print(calcsize("i"))
print(calcsize("f"))
print(calcsize("iff"))

# get back to data

original_data = unpack("iif", packed_data)
print(original_data)
print(unpack("iif", b'\x06\x00\x00\x00\t\x00\x00\x00\x14\xae{A'))

"""         map         """

income = [10, 20, 30]


def double_money(dollars):
    return dollars * 2


new_income = list(map(double_money, income))

print(new_income)

"""         bitwise         """

a = 50  # binary --> 110010
b = 25  # binary --> 011001

c = a & b  # binary --> 010000  AND operation
print(c)

x = 240
y = x >> 2  # shift all bits to 2 right
print(y)


"""         dictionary calc         """

stocks = {
    "GOOG": 520.24,
    "FB": 76.45,
    "YHOO": 39.45,
    "AMZN": 306.21,
    "MSFT": 99.76
}

print(min(stocks)) # find min according to keys
min_price = min(zip(stocks.values(), stocks.keys()))
print(min_price)


"""         largest  | smallest         """

import heapq

grades = [12, 455, 4554, 78, 2, 56, 21]

print(heapq.nlargest(3, grades))  # show me the first biggest elements of grades

stocks = [
    {"ticker": "AAPL", "price": 200},
    {"ticker": "GOOG", "price": 800},
    {"ticker": "YHOO", "price": 54},
    {"ticker": "MSFT", "price": 313},
    {"ticker": "TUNA", "price": 68}
]

print(heapq.nsmallest(2, stocks, key=lambda stock: stock["price"]))

"""     find frequent items     """

from collections import Counter

text = "sezgin cemre resul cemre sezgin resul emir"
words = text.split()
print(words)

counter = Counter(words)
top_three = counter.most_common(2)
print(top_three)


"""     dictionary multiple key sort    """

from operator import itemgetter

users = [
    {"fname": "sezgin", "lname": "acer"},
    {"fname": "cemre", "lname": "erbasaran"},
    {"fname": "emir", "lname": "bakirhan"},
    {"fname": "resul", "lname": "gudu"}
]

for x in sorted(users, key=itemgetter("fname")):
    print(x)

print("-------")

for x in sorted(users, key=itemgetter("fname", "lname")):
    print(x)


"""     sort custom objects     """

from operator import attrgetter


class User:

    def __init__(self, x, y):
        self.name = x
        self.user_id = y

    def __repr__(self):
        return self.name + " : " + str(self.user_id)

users = [
    User("Bucky", 43),
    User("Sally", 45),
    User("Johnn", 55),
    User("Brian", 21),
    User("Laccy", 37),
]

for user in users:
    print(user)

print("-------")

for user in sorted(users, key=attrgetter("name")):
    print(user)

print("-------")

for user in sorted(users, key=attrgetter("user_id")):
    print(user)
