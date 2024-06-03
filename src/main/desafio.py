import numpy as np
import random as rm
from math import pow, sqrt, pi


lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

print(f"Número escolhido: {rm.choice(lista)}")

rm.randrange(100)

"""Elevação a potência"""
base = int(input("Digite a base da potência: "))
expoente = int(input("Digite o expoente da potência: "))
print(f"{base} elevado a {expoente} é igual a {pow(base, expoente)}")

"""Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. 
A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. 
Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado."""

n = int(input('Digite o nº de participantes do sorteio: '))
print(f"O número sorteado foi {rm.randint(1, n)}")

"""Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. 
O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e 
exibe uma mensagem junto a esse token gerado aleatoriamente.
'Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!'"""

nome = input("Qual o seu nome? ")
token = rm.randrange(1000, 10000, 2)
print(f"Olá, {nome}, o seu token de acesso é {token}! Seja bem-vindo(a)")

"""Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado 
'salada de frutas surpresa'. Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor 
a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:"""

#Lista de frutas disponíveis
frutas = ["maçã", "banana", "uva", "pêra",
          "manga", "coco", "melancia", "mamão",
          "laranja", "abacaxi", "kiwi", "ameixa"]

salada = rm.choices(frutas, k=3)

# Imprimindo os itens da lista de frutas gerada
print(f"A salada surpresa é: {salada[0]}, {salada[1]}, {salada[2]}")

"""Você recebeu um desafio de calcular a raiz quadrada de uma lista de números, 
identificando quais resultaram em um número inteiro. A lista é a seguinte:"""

numeros = [2, 8, 15, 23, 91, 112, 256]

"""No final, informe quais números possuem raízes inteiras e seus respectivos valores.

    Dica: use a comparação entre a divisão inteira (//) da raiz por 1 com o valor da raiz para verificar se o número é inteiro. 
    Por exemplo: 
"""
num = 1.5
num_2 = 2
print(f'{num} é inteiro? :', num // 1 == num)
print(f'{num_2} é inteiro? :', num_2 // 1 == num_2)
"""
Saída:
1.5 é inteiro? : False
2 é inteiro? : True
"""

raiz = []

for numero in numeros:
    raiz.append(sqrt(numero))

for i in range(len(raiz)):
    if raiz[i] // 1 == raiz[i]:
        print(f"O número {numeros[i]} possui raiz quadrada inteira igual a {int(raiz[i])}")


"""Faça um programa para uma loja que vende grama para jardins. Essa loja trabalha com jardins circulares e 
o preço do metro quadrado da grama é de R$ 25,00. Peça à pessoa usuária o raio da área circular e devolva o valor em reais 
do quanto precisará pagar.

Dica: use a variável pi e o método pow() da biblioteca math. O cálculo da área de um círculo é de: A = π*r^2 
(lê-se pi vezes raio ao quadrado).
"""

raio = float(input("Digite o raio da área circular em metros: "))
#Cálculo da área com os métodos da math e obtenção do custo em reais
area = pi*pow(raio,2)
valor = area * 25.00

# Exibição do cálculo e custo na tela. O round(n,2) arredonda o valor em duas casas decimais.
print(f"Voce precisará pagar R$ {round(valor, 2)} por uma área de  {round(area,2)} metros de grama")
