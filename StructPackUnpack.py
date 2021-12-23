import struct
# Details: # https://docs.python.org/3/library/struct.html

# hello = b'\x68\x65\x6C\x6C\x6F'
h = 104
e = 101
l = 108
o = 111

if __name__ == "__main__":
    print("Struct Pack Unpack Ex")

    #?: boolean (1)
    #B: unsigned char (1)
    #h: short (2)
    #l: long (4)
    #i: int (4)
    #f: float (4)
    #q: long long int (8)

    fmt = 'hhl'
    var = struct.pack(fmt, 5, 15, 16)
    print("Pack: {}".format(var))
    print("Unpack: {}".format(struct.unpack(fmt, var)))
    print("Size of String representation is {}.".format(struct.calcsize(fmt)))

    fmt2 = 'BBBBB'
    var = struct.pack(fmt2, h, e, l, l, o)
    print("Pack: {}".format(var))
    print("Unpack: {}".format(struct.unpack(fmt2, var)))
    print("Size of String representation is {}.".format(struct.calcsize(fmt2)))

    fmt3 = '>hhl'
    var = struct.pack(fmt3, 5, 15, 16)
    print("Pack: {}".format(var))
    print("Unpack: {}".format(struct.unpack(fmt3, var)))
    print("Size of String representation is {}.".format(struct.calcsize(fmt3)))

    fmt4 = '<hhl'
    var = struct.pack(fmt4, 5, 15, 16)
    print("Pack: {}".format(var))
    print("Unpack: {}".format(struct.unpack(fmt4, var)))
    print("Size of String representation is {}.".format(struct.calcsize(fmt4)))


# --- Output --- #
# Struct Pack Unpack Ex
#
# Pack: b'\x05\x00\x0f\x00\x10\x00\x00\x00'
# Unpack: (5, 15, 16)
# Size of String representation is 8.
#
# Pack: b'hello'
# Unpack: (104, 101, 108, 108, 111)
# Size of String representation is 5.
#
# Pack: b'\x00\x05\x00\x0f\x00\x00\x00\x10'
# Unpack: (5, 15, 16)
# Size of String representation is 8.

# Pack: b'\x05\x00\x0f\x00\x10\x00\x00\x00'
# Unpack: (5, 15, 16)
# Size of String representation is 8.