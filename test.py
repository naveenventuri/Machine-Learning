import string 
translator=str.maketrans('','',string.punctuation)
s='naveen :)'
print(s.translate(translator))