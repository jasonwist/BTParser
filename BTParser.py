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

        self.parsed_data = []

        index = 0

        while index < (len(self.data) -1):
            index, new_data = self.decode(index)
            self.parsed_data.append(new_data)

        return self.parsed_data


    def decode(self, index):
        # INT
        if self.data[index] == self.INT_START:
            print 'int found' # DEBUG
            return self.decodeInt(index)

        # STRING
        elif self.data[index] in self.STR_START:
            print 'string found' # DEBUG
            return self.decodeString(index)

        # LIST
        elif self.data[index] == self.LIST_START:
            print 'list found' # DEBUG
            return self.decodeList(index)

        # DICT
        elif self.data[index] == self.DICT_START:
            print 'dictionary found' # DEBUG
            return self.decodeDict(index)

        else:
            raise ValueError  # DEBUG NEED TO FIX


    def decodeInt(self, index):
        """
        index: the index of INT_START

        returns the index after END_CHAR, new_int
        """
        print 'decodeInt():', # DEBUG
        print index # DEBUG

        int_start = index+1

        while self.data[index] != self.END_CHAR:
            index += 1

        int_end = index

        new_int = self.data[int_start:int_end]

        print 'new_int', # DEBUG
        print new_int   # DEBUG
        print 'return_index',    # DEBUG
        print (index + 1) # DEBUG
        print 'exit_decodeInt()'    #DBUG

        return (index + 1), new_int


    def decodeString(self, index):
        """
        index: the index of the first STR_START

        returns the index after the last string char, new_str
        """

        print 'decodeString():', # DEBUG
        print index # DEBUG

        length_in_str = ''
        new_str = ''

        while (self.data[index] != self.STR_LENGTH_KEY) and (self.data[index] in self.STR_START):
            length_in_str += self.data[index]
            index += 1

        str_length = int(length_in_str)

        str_key = index
        index += 1

        while index <= (str_key + str_length):
            new_str += self.data[index]
            index += 1

        print 'new_str', # DEBUG
        print new_str   # DEBUG
        print 'return_index', # DEBUG
        print index # DEBUG
        print 'exit_decodeString()' # DEBUG

        return index, new_str

    def decodeList(self, index):
        """
        index: the index of LIST_START

        returns the index after END_CHAR, new_list
        """

        print 'decodeList():', # DEBUG
        print index # DEBUG

        new_list = []

        index += 1

        while self.data[index] != self.END_CHAR:

            index, new_item = self.decode(index)
            new_list.append(new_item)

        print 'new_list', # DEBUG
        print new_list  # DEBUG
        print 'return_index', # DEBUG
        print (index + 1) # DEBUG
        print 'exit_decodeList()'   # DEBUG

        return (index + 1), new_list

    def decodeDict(self, index):
        """
        index: the index of DICT_START

        returns the index after END_CHAR, new_dict
        """
        print 'decodeDict():', # DEBUG
        print index # DEBUG

        new_dict = {}

        index += 1

        while self.data[index] != self.END_CHAR:

            index, new_key = self.decode(index)
            index, new_value = self.decode(index)
            new_dict[new_key] = new_value

        print 'new_dict', # DEBUG
        print new_dict  # DEBUG
        print 'return_index', # DEBUG
        print (index + 1) # DEBUG
        print 'exit_decodeDict()'   # DEBUG

        return (index + 1), new_dict



if __name__ == '__main__':

    torrent_data = open("l5.torrent", "rb").read()

    parser = BTParser(torrent_data)

    parsed_data = parser.parseTorrent()

    print 'Parsed Data:',   # DEBUG
    print parsed_data   # DEBUG

