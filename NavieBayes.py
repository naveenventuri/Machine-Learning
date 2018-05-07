import string
file=open("SMSSpamCollection","r+")
testfile=open("test1.txt","w")
testfile2=open("test2.txt","w")
translator=str.maketrans('','',string.punctuation)
testwordprob1={}
testwordprob2={}
wordcount1={}
wordcount2={}
totwordcount1={}
totwordcount2={}
totwordprob1={}
totwordprob2={}
ham=0
spam=0
linespam=[]
lineham=[]
lines=file.readlines()
print(len(lines))
for k in lines:
	k=k.lower()
	line=k.translate(translator)
	words=line.split(None)
	if(words[0]=="ham"):
		ham+=1
		iterwords=iter(words)
		next(iterwords)
		for word in iterwords:
			testfile.write("%s\n"%word)
			if word not in wordcount1:
				wordcount1[word]=1
			else:
				wordcount1[word]+=1
	if(words[0]=="spam"):
		spam+=1
		iterwords=iter(words)
		next(iterwords)
		for word in iterwords:
			testfile2.write("%s\n"%word)
			if word not in wordcount2:
				wordcount2[word]=1
			else:
				wordcount2[word]+=1
print(wordcount1["dhoni"],wordcount2["dhoni"])
print(ham,spam)
probham=ham/(ham+spam)
probspam=spam/(ham+spam)
for k,v in wordcount1.items():
	if k not in totwordcount1:
		totwordcount1[k]=v
	else:
		totwordcount1[k]=0
for k,v in wordcount2.items():
	if k not in totwordcount1:
		totwordcount1[k]=0
	else:
		totwordcount1[k]=v
for k,v in wordcount1.items():
	if k not in totwordcount2:
		totwordcount2[k]=0
	else:
		totwordcount2[k]=v
for k,v in wordcount2.items():
	if k not in totwordcount2:
		totwordcount2[k]=v
	else:
		totwordcount2[k]=0
testcase=input("Enter your file name")
testfile=open(testcase+".txt","r+")
for word in testfile.read().lower().split():
	testwordprob1[word]=1
	testwordprob2[word]=1
	if (totwordcount1[word])==0:
		for k,v in totwordcount1.items():
			totwordcount1[k]=v+1
	if (totwordcount2[word])==0:
		for k,v in totwordcount2.items():
			totwordcount2[k]=v+1
total1=0	
for k,v in totwordcount1.items():
	total1=total1+v
total2=0
for k,v in totwordcount2.items():
	total2=total2+v
for k,v in totwordcount1.items():
	totwordprob1[k]=v/total1
for k,v in totwordcount2.items():
	totwordprob2[k]=v/total2

for k,v in testwordprob1.items():
	testwordprob1[k]=totwordprob1[k]
for k,v in testwordprob2.items():
	testwordprob2[k]=totwordprob2[k]
prob1=1
prob2=1
for k,v in testwordprob1.items():
	prob1=prob1*v
for k,v in testwordprob2.items():
	prob2=prob2*v
prob1=prob1*probham
prob2=prob2*prospam

if(prob1>prob2):
	print("ham")
else:
	print("Spam")
