nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input('Digite sua altura: ').replace(',', '.'))

print('Seu nome é: ', nome, '\nSua idade é: ', idade, '\nSua altura é: ', altura)
print("Seu nome é: %s, sua idade é: %d e sua altura é %.2f" %(nome, idade, altura))

print('Função soma!')
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a+b)

print("Função multiplifacação!")
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
print(a*b)

print("Função divisão")
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador/denominador)

print("Função resto!")
numerador = int(input('Digite o numerador: '))
denominador = int(input('Digite o denominador (OBS: o valor não pode ser nulo): '))
print(numerador%denominador)

print("Função potencia!")
operador = int(input('Digite o operador valor: '))
potencia = int(input('Digite a potência valor: '))
print(operador**potencia)

print("Função média")
nota_1 = float(input('Digite a 1° nota: '))
nota_2 = float(input('Digite a 2° nota: '))
nota_3 = float(input('Digite a 3° nota: '))
print(f'Média {(nota_1+nota_2+nota_3)/3}.')

print("Função média ponderada!")
media_ponderada = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print(f'Média {media_ponderada}.')

print("Frase sem espaço!")
frase = ' Olá Python!  '
print(frase.strip())

frase = input('Digite uma frase: ')
print(frase.strip().lower())

print("Frase troca 'e' por 'f'!")
frase = input('Digite uma frase: ')
print(frase.lower().replace('e','f'))

frase = input('Digite uma frase: ')
print(frase.lower().replace('a',chr(64)))

frase = input('Digite uma frase: ')
print(frase.lower().replace('s',chr(36)))

if 2<7:
    print('Hello!')
elif 3>10:
    print('Tchau!')