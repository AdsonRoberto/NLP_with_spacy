!pip install spacy==2.2.3

import spacy
spacy.__version__

!python -m spacy download pt

pln = spacy.load('pt')
pln

documento = pln('Estou aprendendo processamento de linguagem natural, curso em Curitiba')

for token in documento:
  print(token.text, token.pos_)