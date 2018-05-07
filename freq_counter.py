import numpy as np
file1=open("spam.txt","r+")
file2=open("notspam.txt","r+")
wordcount={};

for word in file.read().lower().split():
    if word not in wordcount:
        freq1=1
        freq2=0
    else:
        freq1=+1
	wordcount[word].append(freq1)
	wordcount[word].append(freq2)
for word in file2.read().lower().split():
    if word not in wordcount:
        freq2=1;
        freq1=0;
    else:
        freq2++
    wordcount[word].append(freq1)
	wordcount[word].append(freq2)
for k,v,l in wordcount.items():
    print (k, v,l)