cadastro = ("Júlia", 23, "São Paulo", "SP", "Python para DS 1")

print(cadastro[0]) # imprime Júlia
print(cadastro[-1]) # imprime Python para DS 1

nome, idade, cidade, estado, turma = cadastro

print(f'A estudante {nome} tem {idade} anos e mora em {cidade}-{estado}. Ela está matriculada na turma de {turma}.')

estudantes = ["João", "Maria", "José", "Cláudia", "Ana"]
estudantes

from random import randint

def gera_codigo():
  return str(randint(0,999))

for estudante in range(len(estudantes)):
  estudantes[estudante] = (estudantes[estudante], gera_codigo())
estudantes

print(estudantes)
