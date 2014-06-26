from BTParser import *


"""
    Basic testing, just swaping out different torrent files that are in the same directory
"""


parser = BTParser()

parsed_data = parser.parse_torrent('pingos.torrent')

print 'Parsed Data:',   # DEBUG
print parsed_data   # DEBUG