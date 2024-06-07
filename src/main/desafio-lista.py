import numpy as np

"""1. Escreva um código que lê a lista abaixo e faça:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

    A leitura do tamanho da lista
    A leitura do maior e menor valor
    A soma dos valores da lista

Ao final exiba uma mensagem dizendo:

"A lista possui [tam] números em que o maior número é [maior] e o menor número é [menor].
A soma dos valores presentes nela é igual a [soma]"""

# Solução 1
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
tam = len(lista)
soma = sum(lista)
maior = max(lista)
menor = min(lista)

print(f"A lista possui {tam} números em que o maior número é {maior} e o menor número é {menor}. A soma dos valores é igual a {soma}")

# -------------------------------------------

"""2. Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

Tabuada do 7:
7 x 0 = 0
7 x 1 = 7
[...]
7 x 10 = 70
"""

# Solução 2

numero = int(input('Digite um número inteiro para a tabuada de 1 a 10:'))

def tabuada(numero: int):
    print(f'Tabuada do {numero}:')
    for i in range(11):
        print(f"{numero} x {i} = {numero * i}")

tabuada(numero)

"""Crie a função que leia a lista abaixo e retorne uma nova lista com os múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

Utilize o return na função e salve a nova lista na variável mult_3."""

lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

#Solução 3

mult_3 = []
#for
"""def multiplo_3(lista: int):
        for i in range(len(lista)):
            if lista[i] % 3 == 0:
                mult_3.append(lista[i])
        return mult_3
mult_3 = multiplo_3(lista)
mult_3"""
#passando uma função
"""
def eh_multiplo_de_3(x):
    return x % 3 == 0

def multiplo_3(lista):
    return list(filter(eh_multiplo_de_3, lista))

mult_3 = multiplo_3(lista)
print(mult_3)
"""
#lambda com filtro e list
'''def multiplo_3(lista):
    return list(filter(lambda x: x %3 ==0, lista))

mult_3 = multiplo_3(lista)
print(mult_3)'''

#list comprehension
'''def multiplo_3(lista):
    return [x for x in lista if x % 3 == 0]

mult_3 = multiplo_3(lista)
print(mult_3)'''

#Usando numpy
listaNp = np.array([97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99])

def multi_3(listaNp):
    return listaNp[listaNp % 3 ==0].tolist()

mult_3 =multi_3(listaNp)
print(f"lista multiplos 3 {mult_3}")

'''4. Crie uma lista dos quadrados dos números da seguinte lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. 
Lembre-se de utilizar as funções lambda e map() para calcular o quadrado de cada elemento da lista.'''

listaQuadrados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
quadrado = lambda x: x ** 2
resultado = list(map(quadrado, numeros))
resultado 
"""

def aoQuadrado(item):
    return item ** 2

resultado = list(map(aoQuadrado, listaQuadrados))

print(resultado)

'''
Você foi contratado(a) como cientista de dados de uma associação de skate. Para analisar as notas recebidas de skatistas 
em algumas competições ao longo do ano, você precisa criar um código que calcula a pontuação dos(as) atletas. 
Para isso, o seu código deve receber 5 notas digitadas pelas pessoas juradas.

Para calcular a pontuação de um(a) skatista, você precisa eliminar a maior e a menor pontuação dentre as 5 notas 
e tirar a média das 3 notas que sobraram. Retorne a média para apresentar o texto:

"Nota da manobra: [media]"
'''
notas = []
somatorio = 0

for i in range(5):
    nota = float(input('Digite a nota: '))
    notas.append(nota)

maior = max(notas)
menor = min(notas)

media = (sum(notas) - maior - menor) / 3

print(f"Nota da manobra é: {round(media, 2)}")

"""
Para atender a uma demanda de uma instituição de ensino para a análise do desempenho de seus(suas) estudantes, você precisa criar uma função que receba uma lista de 4 notas e retorne:

    maior nota
    menor nota
    média
    situação (Aprovado(a) ou Reprovado(a))

Para testar o comportamento da função, os dados podem ser exibidos em um texto:
"""

listaNotasEstudantes = []
maiorNotaEstudante = 0
menorNotaEstudante = 0
situacao = ''
criterioAprovacao = float(input("Digite a nota para aprovação: "))
for i in range(4):
    listaNotasEstudantes.append(float(input("Digite a nota do estudante: ")))


def relatorio(lista):
    maiorNotaEstudante = max(lista)
    menorNotaEstudante = min(lista)
    media = sum(lista)/len(lista)

    if(media >= criterioAprovacao):
        situacao = 'Aprovado(a)'
    else:
        situacao = 'Reprovado'

    print(
        f"O(a) estudante obteve uma média de {media}, com a sua maior nota de {maiorNotaEstudante} pontos e a menor nota de {menorNotaEstudante} pontos e foi {situacao}")

relatorio(listaNotasEstudantes)

'''
Você recebeu uma demanda para tratar 2 listas com os nomes e sobrenomes de cada estudante concatenando-as 
para apresentar seus nomes completos na forma Nome Sobrenome. As listas são:
'''

nomes = ["joão", "MaRia", "JOSÉ"]
sobrenomes = ["SILVA", "souza", "Tavares"]

'''O texto exibido ao fim deve ser parecido com: Nome completo: Ana Silva
Dica: utilize a função map para mapear os nomes e sobrenomes e as funções de string para tratar o texto.
'''

nome_completo = map(lambda nome, sobrenome: f'{nome.title()} {sobrenome.title()}', nomes, sobrenomes)

for n in nome_completo:
    print(f'Nome completo: {n}')
'''-------------------------------------------------'''

'''
Como cientista de dados em um time de futebol, você precisa implementar novas formas de coleta de dados sobre o desempenho de jogadores e 
do time como um todo. Sua primeira ação é criar uma forma de calcular a pontuação do time no campeonato nacional a partir dos dados de gols
marcados e sofridos em cada jogo. Escreva uma função chamada calcula_pontos que recebe como parâmetros duas listas de números inteiros, representando os gols marcados e 
sofridos pelo time em cada partida do campeonato. A função deve retornar a pontuação do time e o aproveitamento em percentual, levando em consideração que a vitória vale 3 
pontos, o empate vale 1 ponto e a derrota 0 pontos.
Observação: se a quantidade de gols marcados numa partida for maior que a de sofridos, o time venceu. Caso seja igual, o time empatou e se for menor, o time perdeu. 
Para calcular o aproveitamento devemos fazer a razão entre a pontuação do time pela pontuação máxima que ele poderia receber.
Para teste, utilize as seguintes listas de gols marcados e sofridos:
'''
gols_marcados = [2, 1, 3, 1, 0]
gols_sofridos = [1, 2, 2, 1, 3]
vitorias = 0
derrotas = 0
empates = 0
pontos = 0


'''A pontuação do time foi de [pontos] e seu aproveitamento foi de [aprov]%'''

def calcula_pontos (gols_marcados, gols_sofridos):
    vitorias = 0
    derrotas = 0
    empates = 0
    for n in range(len(gols_marcados)):
        if gols_marcados[n] > gols_sofridos[n]:
            vitorias += 1

        elif gols_marcados[n] < gols_sofridos[n]:
            derrotas += 1
        else:
            empates += 1

    pontos = (vitorias * 3) + empates
    aprov = round(100 * pontos / (len(gols_marcados) * 3))
    return (pontos, aprov)


pontos, aprov = calcula_pontos(gols_marcados, gols_sofridos)

print(f'A pontuação do time foi de {pontos} e seu aproveitamento foi de {aprov}%')

'''-------------------------------------------------'''

'''Você recebeu o desafio de criar um código que calcula os gastos de uma viagem para um das quatro cidades partindo de Recife, sendo elas: Salvador, Fortaleza, Natal e Aracaju.

O custo da diária do hotel é de 150 reais em todas elas e o consumo de gasolina na viagem de carro é de 14 km/l, sendo que o valor da gasolina é de 5 reais o litro. O gastos com passeios e alimentação a se fazer em cada uma delas por dia seria de [200, 400, 250, 300], respectivamente.

Sabendo que as distâncias entre Recife e cada uma das cidades é de aproximadamente [850, 800, 300, 550] km, crie três funções nas quais: a 1ª função calcule os gastos com hotel (gasto_hotel), a 2ª calcule os gastos com a gasolina (gasto_gasolina) e a 3ª os gastos com passeio e alimentação (gasto_passeio).

Para testar, simule uma viagem de 3 dias para Salvador partindo de Recife. Considere a viagem de ida e volta de carro.'''

"Com base nos gastos definidos, uma viagem de [dias] dias para [cidade] saindo de Recife custaria [gastos] reais"

dias = int(input("Quantas diárias? "))
cidade = input("Qual a cidade? [Salvador, Fortaleza, Natal ou Aracaju]: ")
distancias = [850, 800, 300, 550]
passeio = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(cidade):
    if cidade == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l
    elif cidade == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l
    elif cidade == "Natal":
        return (2 * distancias[2] * gasolina) / km_l
    elif cidade == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l

def gasto_passeio(cidade, dias):
    if cidade=="Salvador":
        return passeio[0] * dias
    elif cidade=="Fortaleza":
        return passeio[1] * dias
    elif cidade=="Natal":
        return passeio[2] * dias
    elif cidade=="Aracaju":
        return passeio[3] * dias

gastos = gasto_hotel(dias) + gasto_gasolina(cidade) + gasto_passeio(cidade, dias)
print(f"Com base nos gastos definidos, uma viagem de {dias} dias para {cidade} saindo de Recife custaria {round(gastos, 2)} reais")


'''-------------------------------------------------'''

'''Você iniciou um estágio em uma empresa que trabalha com processamento de linguagem natural (NLP). 
Sua líder requisitou que você criasse um trecho de código que recebe uma frase digitada pela pessoa usuária e filtre 
apenas as palavras com tamanho maior ou igual a 5, exibindo-as em uma lista. Essa demanda é voltada para a análise 
do padrão de comportamento de pessoas na escrita de palavras acima dessa quantidade de caracteres.

Dica: utilize as funções lambda e filter() para filtrar essas palavras. Lembrando que a função embutida filter() 
recebe uma função (no nosso exemplo uma função lambda) e filtra um iterável de acordo com a função. 
Para tratar a frase use replace() para trocar a ',' '.', '!' e '?' por espaço.

Use a frase "Aprender Python aqui na Alura é muito bom" para testar o código.'''

# Requisitando uma frase e separando-a pelos espaços. Usando replace para trocar
# pontuações por espaço.
frase = input("Digite uma frase: ")
frase = frase.replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split()

# Filtrando a frase no formato de lista, passando para a lista tamanho
# apenas as palavras com 5 ou mais caracteres e imprimindo-a na tela
tamanho = list(filter(lambda x: len(x) >= 5, frase))
print(tamanho)
