string = "sezgin acer istanbul teknik üniversitesi"
a = string.split(" ")
print(a)
for item in a:
    print(item)
string = string.title()
print(string)
dic = dict(name='isim', surname='soyad')
print(len(string))
print(complex(1, 5))
a = complex(1, 5)
b = 1 + 5j
print(a.real, a.imag)
print(a == b)
print(a*b)
a = float(5)
print(a.is_integer())
# exit()
print("Sezgin" in string)
