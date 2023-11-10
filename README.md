Python script that will end up being able to find duplicate files in a file system with a huge amount of files including large files.

It will first run a scan that calculates a hash code for each file. Files above a certain size can optionally be set to not hash all of the file
greatly speeding things up. This is ok if you knows you have a lot of e.g. video files and will do a manual check afterwards.

After hash codes are calculated another script can use them to identify duplicate files and folders.

How to use
==========
You need Python 3 installed.

Step 1 - scan
=============
Run scan.py. If run without arguments, it will index all files in the current folder and sub folders. You can use -p to specify multiple
   paths. Use -m to specify a minimum file size to look at, e.g. -m 100m . This will speed up both scanning, post processing and give you less to worry about.

Step 2 - list
=============
Run list.py. It will print all files which might be duplicates along with file size and separate each group with an empty line.

Warning
=======
Because scan.py does not read the entire file it is very fast. But there is a risk that certain files are duplicate in the areas the tool reads but not in otheres. You should therefor use another tool to compare files before deleting them or know your files well enough to know what might be duplicate and not.
