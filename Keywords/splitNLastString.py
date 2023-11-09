a = [
    "aaa.txt",
    "bbb.jpg",
    "ccc.c",
    "ddd.exe",
    "eee.png"
]
b = []

print("Before: ", a)
for file in a:
    b.append(file.split('.')[0: -1])

print("After: ", b)
# aaa
# bbb

c = [
    "aaa txt",
    "bbb jpg",
    "ccc c",
    "ddd exe",
    "eee png"
]
d = []

print("Before: ", c)
for file in c:
    d.append(file.split(' ')[-1])

print("After: ", d)
# txt
# jpg