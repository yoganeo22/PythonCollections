## example 1: lambda
x = [ 4, -5, 6]
y = lambda x: abs(x//2)
z = list(map(y, x))

print(z)
# [2, 3, 3]


## example 2: lambda
def add(x,y):
    return x+y
print(add(1, 2))

# to replace the above, use lambda
print(lambda x,y: x+y(1, 2))
