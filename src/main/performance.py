import timeit

numero = 5  # Usamos um número fixo para os testes

# Definindo as diferentes abordagens para a tabuada

#Lop for simples
def tabuada_1(numero: int):
    print(f'Tabuada do {numero}:')
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Map e lambda
def tabuada_2(numero: int):
    print(f'Tabuada do {numero}:')
    list(map(lambda i: print(f"{numero} x {i} = {numero * i}"), range(1, 11)))

#list comprehension
def tabuada_3(numero: int):
    print(f'Tabuada do {numero}:')
    [print(f"{numero} x {i} = {numero * i}") for i in range(1, 11)]

#enumerate
def tabuada_4(numero: int):
    print(f'Tabuada do {numero}:')
    for i, _ in enumerate(range(1, 11), start=1):
        print(f"{numero} x {i} = {numero * i}")

# Função para medir o tempo de execução
def medir_tempo(func):
    tempo = timeit.timeit(lambda: func(numero), number=1000)
    print(f'Tempo de execução de {func.__name__}: {tempo:.6f} segundos')
    return tempo

# Medindo o tempo de execução de cada função
quanto1 = medir_tempo(tabuada_1)
quanto2 = medir_tempo(tabuada_2)
quanto3 = medir_tempo(tabuada_3)
quanto4 = medir_tempo(tabuada_4)

print(quanto1, quanto2, quanto3, quanto4)

# Funções ajustadas para cenários reais, apenas calculando valores e não imprimindo

def tabuada_5(numero: int):
    resultados = []
    for i in range(1, 11):
        resultados.append(numero * i)
    return resultados

def tabuada_6(numero: int):
    return list(map(lambda i: numero * i, range(1, 11)))

def tabuada_7(numero: int):
    return [numero * i for i in range(1, 11)]

def tabuada_8(numero: int):
    resultados = []
    for i, _ in enumerate(range(1, 11), start=1):
        resultados.append(numero * i)
    return resultados

# Medindo o tempo de execução de cada função ajustada
tempo_1_calc = medir_tempo(tabuada_5)
tempo_2_calc = medir_tempo(tabuada_6)
tempo_3_calc = medir_tempo(tabuada_7)
tempo_4_calc = medir_tempo(tabuada_8)

tempo_1_calc, tempo_2_calc, tempo_3_calc, tempo_4_calc
