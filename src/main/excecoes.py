notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0], 'Cláudia': [5.5, 6.6, 8.0],
 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
  nome = input("Digite o nome do(a) estudante: ")
  resultado = notas[nome]
  print(resultado)
except Exception as e:
  print(type(e), f"Error: {e}")
  print('Estudante não matriculado na turma')


funcionarios = {'José': 2000, 'Ana': 2200,'João': 2500, 'Maria': 3800}

try:
  aumento = list(map(lambda x: x * 1.1, funcionario.values()))
except Exception as e:
  print(type(e), f'Erro: {e}')
else:
  print(aumento)
finally:
  print("Processo concluido!")