## BTParser


### Quest
Use Python 2.7 to perform the following task:
Write a re­usable library to parse BitTorrent files  The library should expose at least the following pieces of information (when available in the file):

* Creation date
* Client that created the file
* The tracker URL
* The name, length, and checksum of each file described in the torrent

No third­party libraries should be used for this project, only the Python standard library.


### Sources

##### All about the torrent file/Bencode
https://wiki.theory.org/BitTorrentSpecification#Info_Dictionary
http://fileformats.wikia.com/wiki/Torrent_file#File_information_.28info.29
http://en.wikipedia.org/wiki/Torrent_file
http://en.wikipedia.org/wiki/Bencode

##### Ideas/Help with the project
https://github.com/mohanraj-r/torrentparse
- I found this early on when I was looking at similar projects. I skimmed it when I was about halfway through and feeling stuck.
- I borrowed the idea of using string.digits for an easy check if it was a number to determine the start of a string
- I assumed this was another person interviewing for the same job so I didn't look at it so I wouldn't be influnced

http://effbot.org/zone/bencode.htm
- I relied on this for the bulk of my code. That's where I got 'raise ValueError' from for if the value at the index doesn't
match str,int,list,dict
- The regex seems like a sweet idea but I was too far in and didn't want to just rip the regex the person had wrote

https://wiki.theory.org/Decoding_bencoded_data_with_python
- I saw this when I was first researching.
- Making it a list, reversing it and just popping looked neat but didn't want to copy it


### Things that could be better
- There is probably a cleaner/safer/better way than just passing around an index, this was working though so I scaled it
- Write better/more tests than just printing the output to console and comparing it with what I pulled for raw data and
the actual file structure of the torrent


### Things I didn't do
- I didn't have a bunch of error handling so if a file had bad data I wouldn't catch it and my program could possibly crash
- I didn't remove key-values that weren't in the torrent (think md5sum). I had it mainly in there for debugging and I
wasn't sure when I would want to get rid of it. Obviously if I couldn't find the key in the torrent I would just not add
it to my output
