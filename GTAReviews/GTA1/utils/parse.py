import json 
import re
import nltk

file = open("..\GTA1reviews.jl", "r")
i = 1
for line in file:
    fileout = open("..\parsed1GTA" + str(i) + ".txt", 'w')
    lineParse = json.loads(line)

    unicodestring = lineParse['text']
    
    string = unicodestring
    string2 = re.sub(r'[^a-z, A-Z, 0-9, \,, ., !, ?, /]*', '', string)
    string2 = nltk.word_tokenize(string2)
    string2 = nltk.pos_tag(string2)
    for t in string2:
        string3 = t[0] + '/' + t[1] + ' '
        print(string3)
        fileout.write(string3)

    print("------------------------------")
    i+= 1