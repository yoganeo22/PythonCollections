class bString:
    def __init__(self):
        print("Init...")

    def Split(self, mbyte: str, x: int, y: int):
        ''' Split byte
        :param mbyte: byte string (str)
        :param x: first index (int)
        :param y: second index (int)
        :return: splitted byte (str)
        '''
        if x < 0:
            return mbyte[x:]
        else:
            return mbyte[x:y]


if __name__ == "__main__":
    print("Get specific byte string...")

    # hello in ASCII
    Message = b'\x68\x65\x6C\x6C\x6F'
    print("Message: {}".format(Message.decode('ASCII')))

    mString = bString()
    print("Get first two byte string: {}".format(mString.Split(Message, 0, 2)))
    print("Get middle three byte string: {}".format(mString.Split(Message, 1, 4)))
    print("Get last two byte string: {}".format(mString.Split(Message, -2, 0)))


# --- Output --- #
# Get specific byte string...
# Init...
# Get first two byte string: b'he'
# Get middle three byte string: b'ell'
# Get last two byte string: b'lo'
