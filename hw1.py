#HomeWork1
import os
import glob
import re
import string
import collections
from operator import itemgetter
import math
freq = {}

count=0
workdir = "C:/Python34/transcripts/*.txt"
filelist = glob.glob(workdir)

for file in filelist:
    stringsoftext = open(file).read().lower()
    findmatch = re.findall(r'\b[a-z]{1,15}\b', stringsoftext)
    for word in findmatch:
        count = freq.get(word,0)
        freq[word] = count + 1

    freq_list = freq.keys()

print('\nNumber of word tokens\nWords\tCount')
for words in freq_list:
    print (words,'\t', freq[words])


countword = 0
print("\n\n\n\n\n\n---------1 time occurrence of word--------")
for words in freq_list:
    if freq[words] == 1:
        print (words,"\t", freq[words])
        countword += 1

print("Number of words which occur once are:" ,countword)


countunique = 1
print('\n\n\nList of unique words\n')
for words in freq_list:
    #print (countunique , '.' , words)
    countunique +=1

print("Number of unique words in db: ", countunique - 1)

countfiles = 0
print("\n\n\nThe average number of word tokens per document\n")
for file in filelist:
    f = open(file, 'r')
    countfiles = countfiles+1
    f.close()
print("Number of files in directory are: ", countfiles, "\n")

numofwords = 0


for words in freq_list:
    numofwords += freq[words] 

print ("Number of words in database are: ",numofwords, "\n")

print("Avg num of words per doc are: ", float(numofwords / countfiles), "\n\nApproximate Avg number of words are: ", round(numofwords / countfiles))



l=0
fileinc = 0
wordscount = 0
Totalfilescount = 0

#wordscount
for words in freq_list:
    wordscount = freq[words] + wordscount

#Totalfilescount
for file in filelist:
    f = open(file, 'r')
    Totalfilescount = Totalfilescount+1
    f.close()

#tf =frequency , pterm=frequency/wordscount and idf = log of totalfilescount/how many files word occured

MF = int(input("\n\n\nHow many most frequent words are to be known? "))
mostfreq = sorted(freq.items(), key=itemgetter(1), reverse=True)[:MF]

print ("Words\tTF\tIDF\tTF*IDF\t\tTotalwords\tP(term)")
for word, frequency in mostfreq:
    stringsot = open(file).read().lower()
    find = re.findall(r'\b[a-z]{1,15}\b', stringsot)
    for l in find:
        if l == word:
            fileinc = fileinc + 1                
    pterm = round(frequency/wordscount, 3)
    idf = round(math.log(Totalfilescount/fileinc), 3)
    tfidf = round(frequency*idf, 3)
    print (word,"\t", frequency,"\t", idf,"\t", tfidf,"\t",wordscount, "\t",pterm)
    fileinc = 0
