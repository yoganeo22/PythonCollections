citizens = [('Steve', 10), ('Dominic', 12)]

def prod(citizen):
    name = citizen[0]
    balance = citizen[1] * 0.93
    return (name, balance)

result = list(map(prod, citizens))
print(result)
# [('Steve', 9.3), ('Dominic', 11.16)]
