import json
import re
import nltk
import os

dirs = ['GTAReviews', 'AssassinsCreedReviews', 'DSReviews']
root = os.getcwd()
for d in dirs:
    for filename in os.listdir(d):
        if(filename.endswith('reviews.jl')):
            game = (os.path.join(d, filename).split('\\')[1].split('.')[0].split('reviews')[0])
            file = open(root +'\\' + d + '\\' + filename, "r")
            i = 1
            for line in file:
                pathdest = root + '\\corpus\\' + game
                if game not in os.listdir(root + '\\corpus'):
                    os.mkdir(pathdest)
                fileout = open('corpus\\' + game + '\\' + game + 'parsed' + str(i) + ".txt", 'w')
                lineParse = json.loads(line)

                unicodestring = lineParse['text']

                string = unicodestring
                string2 = re.sub(r'[^a-z, A-Z, 0-9, \,, ., !, ?, /]*', '', string)
                string2 = nltk.sent_tokenize(string2)

                #string2 = nltk.pos_tag(string2)
                for t in string2:
                    string3 = t + ' '
                    print(string3)
                    fileout.write(string3)

                print("------------------------------")
                i+= 1
