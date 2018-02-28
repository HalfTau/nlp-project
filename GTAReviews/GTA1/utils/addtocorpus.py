from nltk.corpus import PlaintextCorpusReader

corpus_root = '..\\'
wordlists = PlaintextCorpusReader(corpus_root, 'parsed1GTA[0-9]+.txt')
print(wordlists.fileids())
print(wordlists.words(wordlists.fileids()[0]))
print(wordlists.raw())