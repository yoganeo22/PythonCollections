import enum

class FRUITS(enum.Enum):
    APPLE = 0
    BANANA = 1
    CASHEW = 2

class Processor:
    def Checker(self, num):
        '''
        Print the enum
        :param num: int
        :return: None
        '''
        if num == 0:
            print("My Fruits: {}".format(FRUITS(num).name))
        elif num == 1:
            print("My Fruits: {}".format(FRUITS(num).name))
        elif num == 2:
            print("My Fruits: {}".format(FRUITS(num).name))



if __name__ == "__main__":
    print("Showing Enum in python.")

    mChecker = Processor()
    for x, element in enumerate(FRUITS):
        mChecker.Checker(x)


# --- output --- #
# Showing Enum in python.
# My Fruits: APPLE
# My Fruits: BANANA
# My Fruits: CASHEW
