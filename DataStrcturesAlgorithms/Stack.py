# Python code to demonstrate Implementing  
# stack using list 
stack = ["Amar", "Akbar", "Anthony"] 
stack.append("Ram") 
stack.append("Iqbal") 

# print(stack.peek) -> to peek the top data in stack (not support in python)
# print(stack.search) -> search in stach (not support in python)
print(stack) 
  
# Removes the last item 
print(stack.pop()) 
  
print(stack) 
  
# Removes the last item 
print(stack.pop()) 
  
print(stack) 

# Output:
# ['Amar', 'Akbar', 'Anthony', 'Ram', 'Iqbal']
# Iqbal
# ['Amar', 'Akbar', 'Anthony', 'Ram']
# Ram
# ['Amar', 'Akbar', 'Anthony']

# some uses of stack
# 1. undo/redo in text editor
# 2. move forward/backward through browser history
# 3. backtracking algorithms (maze, file directories)
# 4. calling functions 