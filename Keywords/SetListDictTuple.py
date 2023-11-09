arr = ['c', 'a', 'b', 'd', 'a', 'c']
arr.sort()

print("arr.sort(): ", arr)

x = set(arr)
y = list(x)
print("1. set(x): ", x)  # 'set' object is not subscriptable, can add list to it
print("2. list(x): ", y, " and list[1]: ", y[1])

# arr.sort(): ['a', 'a', 'b', 'c', 'c', 'd']    
# 1. set: set(x):  {'b', 'a', 'd', 'c'}             no duplicate
# 2. list: list(x):  ['b', 'a', 'd', 'c']           dynamic array

d = dict.fromkeys(arr)
print("3. dict: ", d, " and dict['a']: ", d['a'])

new = list(dict.fromkeys(arr).keys())
print(new)

# 3. dict:  {'a': None, 'b': None, 'c': None, 'd': None} and dict['a']:  None
# ['a', 'b', 'c', 'd']

myTuple = ("sss", 1, True)
print("4. type: ", type(myTuple), " and data: ", myTuple, " and tuple[1]: ", myTuple[1])

# 4. type:  <class 'tuple'>  and data:  ('sss', 1, True)  and tuple[1]:  1
