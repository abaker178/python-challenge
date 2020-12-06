# dependencies
import os
import re # finally!

# variables
filename = input("Which text file from ../Resources/ would you like to anayze? (do not include extension) ") + ".txt"
textpath = os.path.join("Resources",filename)
wordcount = 0

# functions
# get the total word count
def getWordCount(t):
    return len(t.split(" "))

# get sentence count

# get average letters per word

# get average words per sentence

# open CSV, read it, store headers, store the rest of the data, then close the file
with open(textpath, "r") as textreader:
    text = textreader.read()

# print results
title = "Paragraph Analysis"
print(title)
print("-" * len(title))
print(f"Approximate Word Count: {getWordCount(text)}")
#print(f"Approximate Sentence Count: {getSentCount(text)}")
#print(f"Average Letter Count: {getLettersPerWord(text)}")
#print(f"Average Sentence Length: {getWordsPerSentence(text)}")