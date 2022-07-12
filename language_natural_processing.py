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

  texto = 'A IBM é uma empresa dos Estados Unidos voltada para a área de informática. Sua sede no Brasil fica em São Paulo e a receita em 2018 foi de aproximadamente 320 bilhões de reais'

  documento = pln(texto)

  for entidade in documento.ents:
  print(entidade.text, entidade.label_)

  from spacy import displacy
displacy.render(documento, style = 'ent', jupyter = True)

texto = 'Bill Gates nasceu em Seattle em 28/10/1955 e foi o criador da Microsoft'

documento = pln(texto)
for entidade in documento.ents:
  print(entidade.text, entidade.label_)

displacy.render(documento, style = 'ent', jupyter = True)

for entidade in documento.ents:
  if entidade.label_ == 'PER':
    print(entidade.text)


from spacy.lang.pt.stop_words import STOP_WORDS

print(STOP_WORDS)

len(STOP_WORDS)

pln.vocab['ir'].is_stop

pln.vocab['caminhar'].is_stop

documento = pln('Estou aprendendo processamento de linguagem natural, curso em Curitiba')

for token in documento:
  if not pln.vocab[token.text].is_stop:
    print(token.text)

documento = pln('reserve uma passagem saindo de Guarulhos e chegando em Curitiba')

origem = documento[5]
destino = documento[9]
origem, destino

list(origem.ancestors)

list(destino.ancestors)

documento[0].is_ancestor(documento[2])

documento = pln('Reserva de uma mesa para o restaurante e de um táxi para o hotel')

tarefas = documento[3], documento[10]
locais = documento[6], documento[13]

tarefas, locais

for local in locais:
  print('-----', local)
  for objeto in local.ancestors:
    print(objeto)

for local in locais:
  for objeto in local.ancestors:
    if objeto in tarefas:
      print("Reserva de {} é para o {}".format(objeto, local))
      break

list(documento[6].children)