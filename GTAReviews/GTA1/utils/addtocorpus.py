from nltk.corpus import PlaintextCorpusReader
from nltk.text import Text
from nltk import FreqDist

corpus_root = '..\\'
wordlists = PlaintextCorpusReader(corpus_root, 'parsed1GTA[0-9]+.txt')
print(wordlists.fileids())
print(wordlists.words(wordlists.fileids()[0]))
print(wordlists.raw())
textList = Text(wordlists.words(wordlists.fileids()[0]))
##documents = [list(wordlists.words(fileid))
##            for fileid in wordlists.fileids()]
##print(documents)
##
##all_words = []
##
##for w in wordlists.words():
##    all_words.append(w.lower())
##    
##all_words = FreqDist(all_words)
##
##word_features = list(all_words.keys())[:100]
##
##print(word_features)
