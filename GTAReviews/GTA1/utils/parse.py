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

    print(string2)
    fileout.write(string2)

    print("------------------------------")
    i+= 1
