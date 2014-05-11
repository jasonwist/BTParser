import string # needed for finding numbers in the string


class BTParser(torrent):
    """

    """

    DICT_START = 'd'
    INT_START = 'i'
    LIST_START = 'l'
    STR_START = string.digits   # So I can compare
    END_CHAR = 'e'
    LENGTH_KEY = ':'




    def __int__(self, torrent):
        """

        """

        self.torrent_data = torrent




    def parseTorrent(self):
        """

        """

        data = self.torrent_data

        parsed_data = {}

        index = 0

        while index in range(len(data)):

            # INT
            if data[index] == self.INT_START:
                print 'int found' # DEBUG

                self.decodeInt(index)

            # STRING
            elif data[index] in self.STR_START:
                print 'string found' # DEBUG

                self.decodeString(index)

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






            index += 1

        return parsed_data



    def decodeInt(self, index):
        """

        """
        int_start = index+1

        while data[index] != self.END_CHAR:
            index += 1

        int_end = index

        new_int = data[int_start:int_end]

        decoded_data.append(dict(i=new_int))


    def decodeString(self, index):
        """

        """
        length_in_str = ''
        new_str = ''

        while data[index] != LENGTH_KEY:
            length_in_str += data[index]
            index += 1

        str_length = int(length_in_str)

        index += 1

        while index <= index + str_length:
            new_str += data[index]
            index += 1

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

    print 'Parsed Data:',
    print parsed_data

