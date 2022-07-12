!pip install spacy==2.2.3

import spacy
spacy.__version__

!python -m spacy download pt

pln = spacy.load('pt')
pln

documento = pln('Estou aprendendo processamento de linguagem natural, curso em Curitiba')

for token in documento:
  print(token.text, token.pos_)


for token in documento:
  print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, 
        token.shape_, token.is_alpha, token.is_stop)

for token in documento:
  if token.pos_ == 'PUNCT':
    print(token.text)

for token in documento:
  print(token.text, token.lemma_)

doc = pln('encontrei encontraram encontrarão encontrariam cursando curso cursei')
[token.lemma_ for token in doc]

!pip install nltk --upgrade

stemmer = nltk.stem.RSLPStemmer()
stemmer.stem('aprender')

for token in documento:
  print(token.text, token.lemma_, stemmer.stem(token.text))