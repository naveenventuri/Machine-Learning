import string
file=open("SMSSpamCollection","r+")
translator=str.maketrans('','',string.punctuation)
testwordprob={}
wordcount1={}
wordcount2={}
totwordcount={}
totwordprob={}
ham=0
spam=0
totalham=0
totalspam=0
prob1=1
prob2=1
lines=file.readlines()
print(len(lines))
for k in lines:
#	lc+=1
#	if(lc==1062):
#		break
	line=k.translate(translator)
	words=line.lower().split()
	if(words[0]=="ham"):
		ham+=1
		iterwords=iter(words)
		next(iterwords)
		for word in iterwords:
			if word not in wordcount1:
				wordcount1[word]=1
			else:
				wordcount1[word]+=1
	if(words[0]=="spam"):
		spam+=1
		iterwords=iter(words)
		next(iterwords)
		for word in iterwords:
			if word not in wordcount2:
				wordcount2[word]=1
			else:
				wordcount2[word]+=1
probham=ham/(ham+spam)
probspam=spam/(ham+spam)
for k,v in wordcount1.items():
	if k not in totwordcount:
		totwordcount[k]=[v,1]
	else:
		value=totwordcount[k]
		totwordcount[k]=[v,value[1]]
for k,v in wordcount2.items():
	if k not in totwordcount:
		totwordcount[k]=[1,v]
	else:
		value=totwordcount[k]
		totwordcount[k]=[value[0],v]
for k in totwordcount:
	value=totwordcount[k]
	totalham+=value[0]
	totalspam+=value[1]
for k in totwordcount:
	value=totwordcount[k]
	totwordprob[k]=[value[0]/totalham,value[1]/totalspam]
print('Traning Completed')
test=lines[1060]
test=test.translate(translator)
testword=test.lower().split()
count=0
for word in testword:
	for k in totwordcount:
		count+=1
		if(k==word):
			break
	if(count==len(totwordcount)):
		testwordprob[word]=[1/totalham,1/totalspam]
	else:
		testwordprob[word]=totwordprob[word]
for k in testwordprob:
	value=testwordprob[k]
	prob1=prob1*value[0]
	prob2=prob2*value[1]
prob1=prob1*probham
prob2=prob2*probspam
if(prob1>prob2):
	print("ham")
else:
	print("Spam")
