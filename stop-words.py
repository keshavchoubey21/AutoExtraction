from pprint import pprint



import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()

ff = open("myfile.txt","r", encoding="utf-8")
doc = nlp(ff.read())
out = [[X.text, X.label_] for X in doc.ents]
pprint(out)
count = 0
for k in out :
    if k[1] == 'PERSON':
      count = count +1
print(count)
