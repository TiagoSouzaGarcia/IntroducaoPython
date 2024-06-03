# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.0]

def mediaAprovacao(lista: list=[0]) -> float:
  ''' Função para calcular a média de notas passadas por uma lista

  lista: list, default [0]
    Lista com as notas para calcular a média
  return = calculo: float
    Média calculada
  '''
  calculo = sum(lista)/ len(lista)

  if calculo >= 6.0:
    situacao = 'Aprovado(a)'
  else:
    situacao = 'Reprovado(a)'
  return (calculo, situacao)

help(mediaAprovacao)
mediaAprovacao(notas)
calculo, situacao = mediaAprovacao(notas)
print(calculo)
print(situacao)
print(f'O(a) estudante atingiu uma média de {calculo} e foi {situacao}.')



