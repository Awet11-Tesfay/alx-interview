#!/usr/bin/python3
""" Determines a valid UTF-8 encoding """


def validUTF8(data):
    """ Number of bytes in the current UTF-8 character """
    num_bytes = 0

    for i in data:

        bin_rep = format(i, '#010b')[-8:]

        if num_bytes == 0:

            for bit in bin_rep:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:

            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
