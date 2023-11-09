mArray = [1, 2, 3, 4, 5]
mArray.append(6)
print(mArray)


def printArrayElement():
    data = [['aaa', 10.0],
            ['bbb', 12.2],
            ['ccc', 13.3]
    ]
    for value in data:
        print(value[0], " and ", value[1])

# print array example
printArrayElement()