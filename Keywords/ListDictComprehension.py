names = [
    'Daniel',
    'Mark',
    'Jennifer'
]

length_list = [len(name) for name in names]  # [6, 4, 8]
length_dictionary = {name:len(name) for name in names}  # {'Daniel': 6, 'Mark': 4, 'Jennifer': 8}

print(length_list)
print(length_dictionary)