
DICT_START = 'd'
INT_START = 'i'
LIST_START = 'l'
STR_START = range(0, 10) # a positive int
END_CHAR = 'e'
LENGTH_KEY = ':'



"""
Read in the file. See wht it gives me.
"""


data = open("safe", "rb").read()


def debencode(data):

    decoded_data = []

    index = 0

    while index in range(len(data)):

        # INT
        if data[index] == INT_START:
            print 'int found' # DEBUG
            int_start = index+1

            while data[index] != END_CHAR:
                index += 1

            int_end = index

            new_int = data[int_start:int_end]

            decoded_data.append(dict(i=new_int))


        # LIST
        # elif d == LIST_START:
        #     print 'list found',
        # elif d == DICT_START:
        #     print 'dictionary found',
        # elif d < 0:
        #     print 'string found',
        # else:
        #     'the fuck is that'

        index += 1

    print decoded_data


debencode(data)
