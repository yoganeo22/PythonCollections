# 1: separating digits for readability
c = 100_1000
binary = 0b_0101
hexa = 0x_f
operation = 1_000 * 2_000

print(c)
print(hexa)
# 1001000
# 15

# 2: throw-away variable
name, _, age = ["john", 2000, 22]
print(name) #john
print(age)  #22

first, *_, last = (1, 2, 3, 4, 5)
print(first)    # 1
print(last)     # 5

for _ in range (3):
    print('Hello')
