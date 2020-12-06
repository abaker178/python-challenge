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

# get the total letter count
def getLetterCount(t):
    return len(re.findall(r"[a-zA-Z]", t))

# get total sentence count
def getSentenceCount(t):
    return len(re.split("(?<=[.!?])[\"\']? +", t))

# open text file, store it as a list of lines, then close the file
with open(textpath, "r") as textreader:
    textlist_raw = textreader.readlines()

# format text to all be on one line
textlist_raw = list(filter(lambda line: line!="\n", textlist_raw)) # did a bunch of extra practice on SoloLearn. Learned about filtering and lambda functions
textlist = [line.replace("\n", "") for line in textlist_raw]
text = " ".join(textlist)

# print results
title = "Paragraph Analysis"
print("")
print(title)
print("-" * len(title))
print(f"Approximate Word Count: {getWordCount(text)}")
print(f"Approximate Sentence Count: {getSentenceCount(text)}")
print(f"Average Word Length: {round(getLetterCount(text) / getWordCount(text), 1)} letters per word")
print(f"Average Sentence Length: {round(getWordCount(text) / getSentenceCount(text), 1)} words per sentence")
print("")