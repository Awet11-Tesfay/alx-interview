#!/usr/bin/python3
""" Write a method that determines if a given dataset represents a valid UTF-8
"""


def validUTF8(data):
    """ Return true if data is a valid UTF-8 encoding. else return false
    """
    
    do1 = 1 << 7
    do2 = 1 << 6
    number_bytes = 0

    if not data or len(data) == 0:
        return True

    for x in data:
        m_number_byte = 1 << 7
        if number_bytes == 0:
            while (m_number_byte & x):
                m_number_byte = m_number_byte >> 1

            if number_bytes == 0:
                continue
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:

            if not (x & do1 and not (x & do2)):
                return False
            number_bytes -= 1

    if number_bytes:
        return False
    else:
        return True
