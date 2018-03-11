from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from nltk import bigrams 
from nltk import FreqDist 

import os

print("Game Reviews: ")
for name in os.listdir('..\\corpus\\'):
    print(name)

corpus = input("Enter game to run: ")

corpus_r00t = '..\\corpus\\' + corpus
#corpus_root = '..\\corpus\\AC1'
wordlists = PlaintextCorpusReader(corpus_r00t, '.*')

#-------Code below is just messing around --------------
#print(wordlists.fileids())
#print(wordlists.sents(wordlists.fileids()[0]))
#print(wordlists.raw())
#print(sent_tokenize(wordlists.raw()))

#Refining word removal
stop_Words = set(stopwords.words('english'))
stop_Words.add("i")
stop_Words.add("it")
stop_Words.add("im")
stop_Words.add("you")
stop_Words.add("would")
stop_Words.add("game")
stop_Words.add("games")

wordCorpus = []
wordCorpus = wordlists.words()
wordCorpus = [w.lower() for w in wordCorpus if w.isalpha()]
wordCorpus = [word for word in wordCorpus if not word in stop_Words]

uOut = open("..\\NGrams\\" + corpus + "Unigrams.txt", 'w')
#----Most Frequent unigrams
ugram = {}
ugram = FreqDist(wordCorpus)

for w in ugram.most_common(25):
    uOut.write(str(w) + '\n')

print("Wrote Most Common Unigrams to " + corpus + "Unigrams.txt")
uOut.close()

bOut = open("..\\NGrams\\" + corpus + "Bigrams.txt", 'w')
#-----Most Frequent BiGrams
wordCorpus = list(bigrams(wordCorpus))
#print(wordCorpus)
top = {}
top = FreqDist(wordCorpus)

for w in top.most_common(25):
    bOut.write(str(w) + '\n')

print("Wrote Most Common Bigrams to " + corpus + "Bigrams.txt")
bOut.close()


#sid = SentimentIntensityAnalyzer()
##print(stop_Words)
#all_sents = []
#all_sents = sent_tokenize(wordlists.raw(wordlists.fileids()[3]))
#space = " "
#for s in all_sents:
#    s = s.split()
#    s = [w for w in s if not w in stop_Words]
#    s = space.join(s)
#    print(s)
#    ss = sid.polarity_scores(s)
#    for k in sorted(ss):
#        print('{0}: {1}, '.format(k, ss[k]), end='')
#    print()
#    
#    
#print()    
#print("With stop words: ")   
#for s in all_sents:
#    print(s)
#    ss = sid.polarity_scores(s)
#    for k in sorted(ss):
#        print('{0}: {1}, '.format(k, ss[k]), end='')
#    print()