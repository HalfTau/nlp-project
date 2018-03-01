from nltk.corpus import PlaintextCorpusReader
from nltk import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

corpus_root = '..\\'
wordlists = PlaintextCorpusReader(corpus_root, 'parsed1GTA[0-9]+.txt')

#-------Code below is just messing around --------------
#print(wordlists.fileids())
#print(wordlists.sents(wordlists.fileids()[0]))
#print(wordlists.raw())

sid = SentimentIntensityAnalyzer()
stop_Words = set(stopwords.words('english'))
print(stop_Words)
all_sents = []
all_sents = sent_tokenize(wordlists.raw(wordlists.fileids()[3]))
space = " "
for s in all_sents:
    s = s.split()
    s = [w for w in s if not w in stop_Words]
    s = space.join(s)
    print(s)
    ss = sid.polarity_scores(s)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()
    
    
print()    
print("With stop words: ")   
for s in all_sents:
    print(s)
    ss = sid.polarity_scores(s)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()