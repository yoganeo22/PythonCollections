def func(**k):
    print(k)
    ans = k['a']+k['b']+k['c']
    print(ans)
    return
    
func(a=1, b=2, c=3)

# dictionary
# {'a': 1, 'b': 2, 'c': 3}
# 6