
DICT_START = 'd'
INT_START = 'i'
LIST_START = 'l'
# start of a string is numbers
END_CHAR = 'e'
LENGTH_KEY = ':'



"""
Read in the file. See wht it gives me.
"""


data = open("safe", "rb").read()


def debencode(data):
    print data




# for d in data:
    # if d == 'i':
    #     print 'int found'
    # elif d == 'l':
    #     print 'list found'
    # elif d == 'd':
    #     print 'dictionary found'
    # elif d < 0:
    #     print 'string found'
    # else:
    #     'the fuck is that'



debencode(data)
