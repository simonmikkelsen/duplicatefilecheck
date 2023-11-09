Python script that will end up being able to find duplicate files in a file system with a huge amount of files including large files.

It will first run a scan that calculates a hash code for each file. Files above a certain size can optionally be set to not hash all of the file
greatly speeding things up. This is ok if you knows you have a lot of e.g. video files and will do a manual check afterwards.

After hash codes are calculated another script can use them to identify duplicate files and folders.

The script is not yet finished.
