def find_sum(array):
    total = 0
    for i in (array):
        total += i
    return total

if __name__ == "__main__":
    array = []
    # O(n) where time complexity is linear as the number of data grows
    # one loop
    for i in range (0, 1000000):
        array.append(i)
    total = find_sum(array)
    print("Total is ", total) #0.69s

    # O(1) where time complexity is constant
    # find a data in the array by its index
    array = [1, 2, 3]
    print(array[1])

    # O(n2) where time complexity is quadratic
    # denotes by loop inside a loop

    # O(log N) where time complexity is logarithmic
    # binary search example

    # O(2n) where time complexity is exponential
    # loop thru every possible scenario in the array