import string # needed for finding numbers in the string


class BTParser():
    """

    """

    DICT_START = 'd'
    INT_START = 'i'
    LIST_START = 'l'
    STR_START = string.digits   # So I can compare
    END_CHAR = 'e'
    STR_LENGTH_KEY = ':'


    def __init__(self, torrent):
        """

        """

        self.torrent_data = torrent




    def parseTorrent(self):
        """

        """

        self.data = self.torrent_data

        self.parsed_data = {}

        index = 0

        while index in range(len(self.data)):

            # INT
            if self.data[index] == self.INT_START:
                print 'int found' # DEBUG
                index = self.decodeInt(index)

            # STRING
            elif self.data[index] in self.STR_START:
                print 'string found' # DEBUG
                index = self.decodeString(index)

            # LIST
            # elif data[index] == self.LIST_START:
            #     print 'list found' # DEBUG
            #
            #
            #     while data[index] != self.END_CHAR:

            # elif d == self.DICT_START:
            #     print 'dictionary found' # DEBUG
            #
            #
            #     while data[index] != self.END_CHAR:


        return self.parsed_data



    def decodeInt(self, index):
        """
        index: the index of 'i'

        returns the index after 'e'
        """
        print 'decodeInt:' # DEBUG

        int_start = index+1

        while self.data[index] != self.END_CHAR:
            index += 1

        int_end = index

        new_int = self.data[int_start:int_end]

        self.parsed_data[index] = new_int

        print 'new_int', # DEBUG
        print new_int   # DEBUG

        return (index + 1)


    def decodeString(self, index):
        """
        index: the index of the first STR_START

        return the index after the last string char
        """

        print 'decodeString:' # DEBUG

        length_in_str = ''
        new_str = ''

        while (self.data[index] != self.STR_LENGTH_KEY) and (self.data[index] in self.STR_START):
            length_in_str += self.data[index]
            index += 1

        str_length = int(length_in_str)

        str_key = index

        while index <= (str_key + str_length):
            new_str += self.data[index]
            index += 1

        self.parsed_data[index] = new_str

        print 'new_str', # DEBUG
        print new_str   # DEBUG

        return index

    def decodeList(self, index):
        """

        """
        return True

    def decodeDict(self, index):
        """

        """
        return True



if __name__ == '__main__':

    torrent_data = open("safe", "rb").read()

    parser = BTParser(torrent_data)

    parsed_data = parser.parseTorrent()

    print 'Parsed Data:',   # DEBUG
    print parsed_data   # DEBUG

