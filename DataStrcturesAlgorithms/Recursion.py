# Program to print factorial of a number
# recursively.
# 6 = 1*2*3*4*5*6 = 720
 
# Recursive function
def recursive_factorial(n):
    # 6 * 5 * 4 * 3 * 2 * 1 = 720
    if n == 1:
        return n
    else:
        return n * recursive_factorial(n-1)

if __name__ == "__main__":
    num = 6

    if num < 1:
        print("Invalid input")
    elif num == 1:
        print("factorial of 1 is 1")
    else:
        print("recursive factorial of " + str(num) + " is " + str(recursive_factorial(num)))
        print("recursive factorial of ", num, " is ", recursive_factorial(num))