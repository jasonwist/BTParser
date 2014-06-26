import string # needed for finding numbers in the string
import time # needed for epoch to human time


class BTParser():

    DICT_START = 'd'
    INT_START = 'i'
    LIST_START = 'l'
    STR_START = string.digits   # So I can compare the char against 0-9
    END_CHAR = 'e'
    STR_LENGTH_KEY = ':'


    def __init__(self):
        """
        """
        pass


    def parse_torrent(self, torrent_name):
        """
        Parses the given torrent file and returns a dictionary of the wanted information
        If the required information cannot be found the value will be 'Not available'

        I did this for basic troubleshooting, in production I would have just not had the key value pair
        at all or set it to a value indicating it didn't exist in the torrent file

        :param torrent_name: The name of the target file
        :return torrent_info: A dictionary of the required information
        """

        self.data = open(torrent_name, "r").read()

        self.parsed_data = []

        index = 0

        while index < (len(self.data) -1):
            index, new_data = self.decode(index)
            self.parsed_data.append(new_data)

        torrent_info = self.torrent_info()

        return torrent_info


    def decode(self, index):
        """
        Uses the index given to determine what type of value will be decoded

        Ints and Strings are the base cases, Lists and Dicts keep calling decode()

        :param index: The index of the first char of the data type
        :return (index, new_data): The char right after data type's value, A new decoded data
        """

        # INT
        if self.data[index] == self.INT_START:
            # print 'int found' # DEBUG
            return self.decode_int(index)

        # STRING
        elif self.data[index] in self.STR_START:
            # print 'string found' # DEBUG
            return self.decode_str(index)

        # LIST
        elif self.data[index] == self.LIST_START:
            # print 'list found' # DEBUG
            return self.decode_list(index)

        # DICT
        elif self.data[index] == self.DICT_START:
            # print 'dictionary found' # DEBUG
            return self.decode_dict(index)

        else:
            raise ValueError  # OMGWTFBBQ


    def decode_int(self, index):
        """
        Given the start of the integer, return the decoded integer and the position of the start of the next data type

        :param index: The index of the start of the data type (i)
        :return index, new_int: The index after 'e', The decoded int
        """
        # print 'decode_int():', # DEBUG
        # print index # DEBUG

        int_start = index+1

        while self.data[index] != self.END_CHAR:
            index += 1

        int_end = index

        new_int = self.data[int_start:int_end]

        # print 'new_int', # DEBUG
        # print new_int   # DEBUG
        # print 'return_index',    # DEBUG
        # print (index + 1) # DEBUG
        # print 'exit_decode_int()'    #DBUG

        return (index + 1), new_int


    def decode_str(self, index):
        """
        Given the start of the string, return the decoded string and the position of the start of the next data type

        :param index: The index of the start of the data type (0-9)
        :return: index, new_str: The index after the last char in the string, The decoded string
        """

        # print 'decode_str():', # DEBUG
        # print index # DEBUG

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

        # print 'new_str', # DEBUG
        # print new_str   # DEBUG
        # print 'return_index', # DEBUG
        # print index # DEBUG
        # print 'exit_decode_str()' # DEBUG

        return index, new_str


    def decode_list(self, index):
        """
        Given the start of the list, return the decoded list and the position of the start of the next data type

        Every time a new list item is discovered call decode() give it the starting index and add it to the list
        A new (incremented) index is one of the products of decode() so it will automatically point to the next
        list item or the end of list char 'e'

        :param index: The index of the start of the data type (l)
        :return: index, new_str: The index after 'e', The decoded list
        """

        # print 'decode_list():', # DEBUG
        # print index # DEBUG

        new_list = []

        index += 1

        while self.data[index] != self.END_CHAR:

            index, new_item = self.decode(index)
            new_list.append(new_item)

        # print 'new_list', # DEBUG
        # print new_list  # DEBUG
        # print 'return_index', # DEBUG
        # print (index + 1) # DEBUG
        # print 'exit_decode_list()'   # DEBUG

        return (index + 1), new_list


    def decode_dict(self, index):
        """
        Given the start of the dict, return the decoded dict and the position of the start of the next data type

        Every time a new list item is discovered call decode() twice to get the key-value pair
        The key will always be first and the value will always be after the key
        Add the key-value pair to the dictionary

        :param index: The index of the start of the data type (d)
        :return: index, new_str: The index after 'e', The decoded dict
        """
        # print 'decode_dict():', # DEBUG
        # print index # DEBUG

        new_dict = {}

        index += 1

        while self.data[index] != self.END_CHAR:

            index, new_key = self.decode(index)
            index, new_value = self.decode(index)

            new_dict[new_key] = new_value

        # print 'new_dict', # DEBUG
        # print new_dict  # DEBUG
        # print 'return_index', # DEBUG
        # print (index + 1) # DEBUG
        # print 'exit_decode_dict()'   # DEBUG

        return (index + 1), new_dict


    def torrent_info(self):
        """
        Parses the wanted information that was decoded from the torrent

        :return torrent_info: A dictionary containing the required information for the project
        """
        torrent_info = {}

        torrent_info['Created on'] = self.creation_date()
        torrent_info['Torrent Client'] = self.creation_client()
        torrent_info['Tracker URL'] = self.tracker_url()
        torrent_info['Files in Torrent'] = self.files()

        return torrent_info

    def creation_date(self):
        """
        Locates the creation date of the torrent an converts it from epoch to GMT

        :return creation date: The creation date in GMT
        """
        creation_date_epoch = self.parsed_data[0].get('creation date')

        if creation_date_epoch != None:
            return time.strftime("%a, %b %d %Y %H:%M:%S", time.gmtime(int(creation_date_epoch)))
        else:
            return 'Not available'


    def tracker_url(self):
        """
        Locates the tracker URL for the torrent

        :return announce: The tracker URL
        """
        return self.parsed_data[0].get('announce', 'Not available')


    def creation_client(self):
        """
        Locates the client that created the torrent

        :return created by: The name of the client
        """
        return self.parsed_data[0].get('created by', 'Not available')


    def files(self):
        """
        Locates the information of the file(s) in the torrent
        Then goes into Single File Mode or Multiple File Mode

        :return file(s): A dict or list of dicts that contains each files md5checksum, name and length (Bytes)
        """
        info = self.parsed_data[0].get('info')

        if info is not None:
            files = info.get('files')

            if files is None:
                return self.single_file_mode(info)

            else:
                return self.multiple_file_mode(info)

        else:
            return 'Not available'

    def single_file_mode(self, info):
        """
        Gets the required info of the file

        :param info: A dict containing the required information
        :return file_info: Return a dict of name, length (Bytes) and md5sum of the file
        """

        single_file_info = {}

        single_file_info['name'] = info.get('name', 'Not available')
        single_file_info['length'] = info.get('length', 'Not available')
        single_file_info['md5sum'] = info.get('md5sum', 'Not available')

        return single_file_info

    def multiple_file_mode(self, info):
        """
        Gets the required info of the files

        :param info: A list containing dictionaries of the required information
        :return file_info: Return a list of dictionaries that contain the name, length (Bytes) and md5sum of the files
        """
        list_of_files = []

        files = info.get('files')

        if files:
            for f in files:

                new_file = {}
                path = f.get('path')

                if path:
                    new_file['name'] = path.pop() # The last string in the path list is the file name
                else:
                    new_file['name'] = 'Not available'

                new_file['length'] = f.get('length', 'Not available')
                new_file['md5sum'] = f.get('md5sum', 'Not available')
                list_of_files.append(new_file)

            return list_of_files

        else:
            return 'Not available'