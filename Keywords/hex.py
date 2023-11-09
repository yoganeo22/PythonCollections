# int to hex and hex to int
x = 15
y = hex(x)
print(y)        # 0xf
y = 0xff
print(int(y))   # 255

# int to binary
x -= 1
print(bin(x))   # 0b1110
x = '0b11010'
print(int(x, 2))    # 20
