from nltk.corpus import PlaintextCorpusReader
from nltk import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

corpus_root = '..\corpus\ACU'
wordlists = PlaintextCorpusReader(corpus_root, '.*')

#-------Code below is just messing around --------------
#print(wordlists.fileids())
#print(wordlists.sents(wordlists.fileids()[0]))
#print(wordlists.raw())
#print(len(wordlists.fileids()))

reviewSenti = []
sid = SentimentIntensityAnalyzer()
stop_Words = set(stopwords.words('english'))
gameSenti = []; 
#print(stop_Words)
for i in range(len(wordlists.fileids())):
    all_sents = []
    revSent = []
    all_sents = sent_tokenize(wordlists.raw(wordlists.fileids()[i]))
    #print(all_sents)
    space = " "
    for s in all_sents:
        #s = s.split()
        #s = [w for w in s if not w in stop_Words]
        #s = space.join(s)
        #print(s)
        ss = sid.polarity_scores(s)
        revSent.append(ss)
        comp = 0;
        neu = 0;
        neg = 0;
        pos = 0;
        for sentiment in sorted(ss):
            #print('{0}: {1}, '.format(sentiment, l[sentiment]), end='')
            if sentiment == 'compound':
                comp += ss[sentiment]
            if sentiment == 'neu':
                neu += ss[sentiment]
            if sentiment == 'neg':
                neg += ss[sentiment]
            if sentiment == 'pos':
                pos += ss[sentiment]

#how the array is formatted:  comp / neu / neg / pos
    if len(revSent) > 0:
        reviewSenti.append({'compound' : comp / len(revSent),
                        'neu' : neu / len(revSent),
                        'neg' : neg / len(revSent),
                        'pos' : pos / len(revSent)})
    
        
#print(reviewSenti)

#go through all of the review sentiments and aggregate the scores
comp = 0;
neu = 0;
neg = 0;
pos = 0;
for review in reviewSenti:
    #print(review)
    for sentiment in review:
        if sentiment == 'compound':
            comp += review[sentiment]
        if sentiment == 'neu':
            neu += review[sentiment]
        if sentiment == 'neg':
            neg += review[sentiment]
        if sentiment == 'pos':
            pos += review[sentiment]

print('{0}: {1:.5g}, {2}: {3:.5g}, {4}: {5:.5g}, {6}: {7:.5g}'.format(
    "compound", comp / len(reviewSenti),
    "neu", neu / len(reviewSenti),
    "neg", neg / len(reviewSenti),
    "pos", pos / len(reviewSenti), end=''))

##print()    
##print("With stop words: ")   
##for s in all_sents:
##    print(s)
##    ss = sid.polarity_scores(s)
##    for k in sorted(ss):
##        print('{0}: {1}, '.format(k, ss[k]), end='')
##    print()
