import nltk 

nltk.download()

text = "hello word i m  abdelmajid zaddi "
sentencer = nltk.sent_tokenize(text)
token = nltk.word_tokenize(sentencer)

print(sentencer)
print(token)