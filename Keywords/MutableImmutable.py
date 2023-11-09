# Immutable - cannot be changed after creation
# ie. int, float, bool, string, unicode, and tuple
tuple1 = (0, 1, 2, 3) 
#tuple1[0] = 4
print(tuple1)

message = "Welcome"
#message[0] = 'p'
print(message)


# Mutable - can be changed after creation
# ie. List, Dict and Set
my_set = {1, 2, 3}
new_set = my_set
new_set.add(4)
 
print(my_set)    
print(new_set)