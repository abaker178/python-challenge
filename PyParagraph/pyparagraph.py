# dependencies
import os
import re

# variables
filename = input("Which text file from ../Resources/ would you like to analyze? (do not include extension) ") + ".txt"
textpath = os.path.join("PyParagraph", "Resources", filename)
wordcount = 0

#### Functions ####
# get the total word count
def getWordCount(t):
    return len(t.split(" "))

# get the total letter count
def getLetterCount(t):
    return len(re.findall(r"[a-zA-Z]", t))

# get total sentence count
def getSentenceCount(t):
    # ignores potential initials (Rutherford B. Hayes) and 
    # considers if there is a quote (" or ') after the period
    return len(re.split("(?<=[^A-Z][.!?])[\"\']? +", t))


# open text file, store it as a list of lines, then close the file
with open(textpath, "r") as textreader:
    textlist_raw = textreader.readlines()

# format text to all be on one line
textlist_raw = list(filter(lambda line: line!="\n", textlist_raw))
textlist = [line.replace("\n", "") for line in textlist_raw]
text = " ".join(textlist)

# print results
title = "Paragraph Analysis"
print(f"\n{title}\
    \n{'-' * len(title)}\
    \nApproximate Word Count: {getWordCount(text)}\
    \nApproximate Sentence Count: {getSentenceCount(text)}\
    \nAverage Word Length: {round(getLetterCount(text) / getWordCount(text), 1)} letters per word\
    \nAverage Sentence Length: {round(getWordCount(text) / getSentenceCount(text), 1)} words per sentence")