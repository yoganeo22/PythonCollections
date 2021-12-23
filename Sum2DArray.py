# 2D Array col x row = 3x3 (6 + 15 + 24 = 45)
arr = [[1,2,3], [4,5,6], [7,8,9]]

if __name__ == "__main__":
    print("Sum of 2D Array Ex!")
    sums = 0;

    print("len: ", len(arr));

    # Add First Column, Second Column, Third Column
    # 1 + 4 + 7 = 12
    # 2 + 5 + 8 = 27
    # 3 + 6 + 9 = 45
    for x, element in enumerate(arr):
        for y, element in enumerate(arr):
            sums += element[x]

    print("sums: {}".format(sums))

