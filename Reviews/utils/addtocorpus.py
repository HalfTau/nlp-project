from nltk.corpus import PlaintextCorpusReader
from nltk import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

corpi = ['AC1', 'AC2', 'AC3', 'AC4', 'ACB', 'ACO', 'ACR', 'ACRO', 'ACS', 'ACU',
         'DS1', 'DS2', 'DS3',
         'GTA1', 'GTA2', 'GTA3', 'GTA4', 'GTA5', 'GTASA']

output = open('output.txt', 'w+')

#-------Code below is just messing around --------------
#print(wordlists.fileids())
#print(wordlists.sents(wordlists.fileids()[0]))
#print(wordlists.raw())
#print(len(wordlists.fileids()))

for game in corpi:
    corpus_root = '..\corpus\\' + game
    wordlists = PlaintextCorpusReader(corpus_root, '.*')
    output.write(game + '\n')
    ##UNCOMMENT TO BREAK AFTER 1 GAME
##    if game == "AC2":
##            break
    print('Working on ' + game + '\n')

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
            #UNCOMMENT TO SEE SENTIMENT SCORES BASED ON THE REVIEW, NOT GAME 
##            print({'compound' : comp / len(revSent),
##                            'neu' : neu / len(revSent),
##                            'neg' : neg / len(revSent),
##                            'pos' : pos / len(revSent)})
        
            
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
                #print('comp : {0}', )
                comp += review[sentiment]
            if sentiment == 'neu':
                neu += review[sentiment]
            if sentiment == 'neg':
                neg += review[sentiment]
            if sentiment == 'pos':
                pos += review[sentiment]

    #Displays the overall game sentiment score based on all reviews 
    print('{0}: {1:.5g}, {2}: {3:.5g}, {4}: {5:.5g}, {6}: {7:.5g}'.format(
        "compound", comp / len(reviewSenti),
        "neu", neu / len(reviewSenti),
        "neg", neg / len(reviewSenti),
        "pos", pos / len(reviewSenti), end='\n'))
    output.write('{0:.5g} {1:.5g} {2:.5g} {3:.5g}\n'.format(comp / len(reviewSenti),
                                                          neu / len(reviewSenti),
                                                          neg / len(reviewSenti),
                                                          pos / len(reviewSenti))) 
    print('Finished with ' + game + '\n')

output.close()
