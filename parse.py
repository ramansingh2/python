





import nltk
from nltk import CFG
grammar = CFG.fromstring("""
S -> NP VP
NP -> NOUN VP | NOUN CONJ VP | NOUN PREP DET VP | NOUN
VP -> VERB DET | ADJ NP | DET ADJ NP
DET -> 'a' | 'his'
NOUN -> 'John' | 'coach' | 'bed' | 'apartment'
ADJ -> 'new'
VERB -> 'found'
PREP -> 'in'
CONJ -> 'and'
""")
from nltk.parse import ChartParser
rd = ChartParser(grammar)
sentence1 = 'John found a new coach and a new bed in his new apartment'.split()
for t in rd.parse(sentence1):
    print(t)