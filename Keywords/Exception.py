import traceback 

x = [1, 2, 3, 4, 5]

def Test(x):
    try:
        print(x[5])
    except:
        print(traceback.print_exc())

Test(x)
print("Test completed")