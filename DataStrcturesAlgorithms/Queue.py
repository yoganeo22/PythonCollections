# Python code to demonstrate Implementing  
# Queue using list 
from collections import deque 

# Example 1
queue = ["Amar", "Akbar", "Anthony"] 
queue.append("Ram") 
queue.append("Iqbal") 
print(queue) 
  
# Removes the first item 
print(queue.pop(0)) 
  
print(queue) 
  
# Removes the first item 
print(queue.pop(0)) 
  
print(queue) 

# output
# ['Amar', 'Akbar', 'Anthony', 'Ram', 'Iqbal']
# Amar
# ['Akbar', 'Anthony', 'Ram', 'Iqbal']
# Akbar
# ['Anthony', 'Ram', 'Iqbal']

# Example 2
# Initializing a queue 
q = deque() 
  
# Adding elements to a queue 
q.append('Amar') 
q.append('Akbar') 
q.append('Anthony') 

print("\nInitial queue") 
print(q) 
  
# Removing elements from a queue 
print("\nElements dequeued from the queue") 
print(q.popleft()) 
print(q.popleft()) 
  
print("\nQueue after removing elements") 
print(q) 
  
# Uncommenting q.popleft() 
# will raise an IndexError 
# as queue is now empty 

# Output:
#Initial queue
#deque(['Amar', 'Akbar', 'Anthony'])

#Elements dequeued from the queue
#Amar
#Akbar

#Queue after removing elements
#deque(['Anthony'])
