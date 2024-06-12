"""Dict Comprehension
É uma forma simples e concisa de criar ou modificar um dicionário.
Podemos aplicar condicionais e laços para criar diversos tipos de dicionários a partir de padrões que desejamos para a nossa estrutura de dados
e com o suporte de iteráveis como listas ou sets.
Formato padrão:
{chave: valor for item in lista}
"""

lista_completa = [[('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')],
                  [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprovado', 'Aprovado', 'Reprovado', 'Aprovado', 'Aprovado']]

coluna = ["Notas", "Média Final", "Situação"]
cadastro = {coluna[i]: lista_completa[i+1] for i in range(len(coluna))}

cadastro["Estudante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
cadastro
