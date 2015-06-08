# -*- coding: utf-8 -*-

"""
    working_with_files.py - Advanced Topics 3.  Working with files, reading and writing
"""
print
import os

# This is a useful oneliner to get the directory the script is located
basedir = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(basedir, os.pardir, 'data'))
foo_txt = os.path.join(data_dir, 'foo.txt')

assert os.path.isdir(data_dir)

"""
    Before reading/writing to files, the file must be opened.
    After finished working, the file must be closed.
"""

f = open(foo_txt, 'r')  # This opens the file for reading, 'r'

"""
    The open function returns what is called a 'file descriptor',
    it is an object that points to an open file and has simple
    methods associated with it, like 'read', 'readline', etc.
"""
print "Read the whole file: {}".format(f.read())
f.seek(0)  # Manually seek to a position in the file

print "Read first 3 characters: {}".format(f.read(3))
print "Next 4 characters: {}".format(f.read(4))
f.seek(0)  # Manually seek to a position in the file

print "I am back at the beginning: {}".format(f.read(3))
f.close()  # Closing files is very important


f = open(foo_txt, 'r')

print "The whole line can be read:"
print f.readline()
print "At the end of the file, an empty string is returned: '{}'".format(f.readline())
f.close()

"""
    Alternatively, lines can be read by iterating over the file object
"""
f = open(foo_txt, 'r')
print
print "File objects are iterable:"
for line in f:
    print line

f.close()

"""
    A more elegant syntax for working with files is the 'with/as' statement, it handles closing for you.
"""
print
print "The with/as statement is more elegant:"

with open(foo_txt, 'r') as f:
    for line in f:
        print line  # This will keep printing the lines until the file ends


#raw_input("More...")
print

"""
    Writing to files is performed similarly, this time passing the write flag, 'w'
    to the open function.
"""

bar_txt = os.path.join(data_dir, 'bar.txt')
# Here we ensure that the file doesn't exist when we try to write to it
if os.path.isfile(bar_txt):
    os.remove(bar_txt)
f = open(bar_txt, 'w')
f.writelines(["Hello world", os.linesep, "Nice to see you here", os.linesep])
f.close()

print "See? {}".format(open(bar_txt, 'r').read())

"""
    Additionally, we can append to existing files using the append flag, 'a'
"""

f = open(bar_txt, 'a')
f.writelines(["This line was appended"])
f.close()

print "With the appended line: {}".format(open(bar_txt, 'r').read())

#raw_input("More...")
print
"""
    Common data files are .csv (comma separated values), it is a very old and low maintenance way
    of sharing data between mediums, ie spreadsheets
"""
import csv  # The csv module is builtin and useful for this purpose
csv_file = os.path.join(data_dir, 'data.csv')

assert os.path.isfile(csv_file)

reader = csv.DictReader(open(csv_file, 'r'))

"""
    DictReader automatically parses with column headers, alternatively the
    csv.reader() function can be used
"""

# Instantiate data structure
csv_data = {}
for field in reader.fieldnames:
    csv_data[field] = []

print csv_data
# Read data file manually
for line in reader:
    # Each line is a dict of {field_name: line_value} key/value pairs
    for field in reader.fieldnames:
        csv_data[field].append(line[field])  #

"""
    Notice the data is read as strings.  Using this somewhat crude module we
    have to manually force the data types ourselves.
"""
print "csv_data: {}".format(csv_data)

csv_data["Score"] = [int(_) for _ in csv_data["Score"]]  # Note the succinct one-liner list notation
csv_data["Pass/Fail"] = [bool(_ == 'True') for _ in csv_data["Pass/Fail"]]  # Note: False not read properly
print
print "Formatted csv_data: {}".format(csv_data)
#raw_input("More...")

"""
    Writing data structures to a csv is similar to reading.  First open the file for writing,
    and pass the file object to a csv Writer object.
"""

csv_file = os.path.join(data_dir, 'out_data.csv')
if os.path.isfile(csv_file):
    print "Removing existing file: {}".format(csv_file)
    os.remove(csv_file)

with open(csv_file, 'w') as f:
    writer = csv.writer(f)

    # Write the column headers to the file
    writer.writerow(csv_data.keys())

    # The zip function is very useful for reordering lists of lists
    writer.writerows(zip(*csv_data.values()))

print
print "Checking the written output: {}".format(open(csv_file, 'r').read())
