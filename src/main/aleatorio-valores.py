from random import randrange, sample

lista = []

for i in range(0, 20):
    lista.append(randrange(100))

sample(lista, 5)

import math

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")

from math import *

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {sqrt(n)}")

"""from math import ceil

receita = 1000
unidade = 15

print(f" A empresa vendeu aproximadamente {ceil(receita/unidade)} unidades")"""

"""
import math

receita = 1000
unidade = 15

print(f" A empresa vendeu aproximadamente {math.ceil(receita/unidade)} unidades")
"""