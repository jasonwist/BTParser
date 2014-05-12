import BTParser


"""
    Basic testing, just swaping out different torrent files that are in the same directory
"""


parser = BTParser.BTParser()

parsed_data = parser.parseTorrent('pingos.torrent')

print 'Parsed Data:',   # DEBUG
print parsed_data   # DEBUG