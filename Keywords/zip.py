items = [
    'Mystic Sword',
    'Rock'
]
rarity = [
    99,
    10
]
weight = [
    1.3,
    1.2
]

inv = zip(items, rarity, weight)    #zip: list [('Mystic Sword', 99, 1.3), ('Rock', 10, 1.2)]
print(list(inv))
#i,r,w = zip(*inv)   #unzip: tuple ('Mystic Sword', 'Rock') (99, 10) (1.3, 1.2)
#print(i,r,w)