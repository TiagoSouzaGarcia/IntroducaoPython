lista = ['Fabricio Daniel',9.5,9.0,8.0,True]
lista

for elemento in lista:
  print(elemento)

duvida = 'Quem veio antes? O ovo? Ou foi a serpente?'
lista_palavras = duvida.split('?')
print(lista_palavras)

raca_caes = ['Labrador Retriever',
             'Bulldog Francês',
             'Pastor Alemão',
             'Poodle']

raca_caes.insert(1, 'Golden Retriever')
print(raca_caes)

raca_caes.pop(1)
print(raca_caes.index('Pastor Alemão'))

raca_caes.sort()
print(raca_caes)
