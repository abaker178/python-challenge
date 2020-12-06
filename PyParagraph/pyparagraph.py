# dependencies
import os
import re # finally!

# variables
filename = input("Which text file from ../Resources/ would you like to anayze? (do not include extension) ") + ".txt"
textpath = os.path.join("Resources",filename)

# functions

# open CSV, read it, store headers, store the rest of the data, then close the file
with open(textpath, "r") as textreader:
    text = textreader.read()

# get word count

# get sentence count

# get average letters per word

# get average words per sentence

# print results