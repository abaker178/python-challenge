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

# get average letters per word
def getLettersPerWord(t):
    return int(round(getLetterCount(t) / getWordCount(t), 0))

# get average words per sentence
def getWordsPerSentence(t):
    return int(round(getWordCount(t) / getSentenceCount(t),0))

# open text file, store it as a list of lines, then close the file
with open(textpath, "r") as textreader:
    textlistraw = textreader.readlines()

# format text to all be on one line
textlistraw = list(filter(lambda line: line!="\n", textlistraw)) # did a bunch of extra practice on SoloLearn. Learned about filtering and lambda functions
textlist = [line.replace("\n", "") for line in textlistraw]
text = " ".join(textlist)

# print results
title = "Paragraph Analysis"
print(title)
print("-" * len(title))
print(f"Approximate Word Count: {getWordCount(text)}")
print(f"Approximate Sentence Count: {getSentenceCount(text)}")
print(f"Average Letter Count: {getLettersPerWord(text)}")
print(f"Average Sentence Length: {getWordsPerSentence(text)}")