import re

def carregarVocabulario(filename):
  dic = set()
  for line in open(filename, 'r', encoding='utf8'):
    dic.add(line.rstrip().lower())
  return sorted(dic)

dic = carregarVocabulario('vocabulario.txt')

def gerarPalavras(texto):
  pass
  naoQuero = ['(', ')', '[', ']', '.', ',', ':', ';', '?', '!', '\n', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  for x in naoQuero:
      texto = texto.replace(x, ' ')
  texto = texto.split()
  return texto

def mmLetras(palavra1, palavra2):
  pass
  if len(palavra1)>len(palavra2) or len(palavra1)==len(palavra2):
      maior = len(palavra1)
  if len(palavra2)>len(palavra1):
      maior = len(palavra2)
  
  comum = 0
  
  for x,y in zip(palavra1, palavra2):
      if x == y:
          comum += 1

  return maior - comum

def sugerir(dic, palavra, distancia, maxSugestoes=5):
    biblio = {  }
    chaves = []
    for words in dic:
        x = distancia(palavra,words)
        if x not in biblio.keys():
            biblio[x] = []
            chaves.append(x)
        biblio[x].append(words)
    
        chaves.sort()
    
    final = []
    final += biblio[chaves[0]][:maxSugestoes]
    i = 1
    while len(final) < maxSugestoes:
        final += biblio[chaves[i]][:maxSugestoes]
        i += 1
        final = final[:maxSugestoes]
    
    final.sort()
    
    return final

def corretor(dic, texto, distancia, maxSugestoes=5): 
    keys = gerarPalavras(texto)
    filtro = [i for i in keys if i not in dic]
    for x in filtro:
        print(x, "-->", sugerir(dic, x, distancia, maxSugestoes))