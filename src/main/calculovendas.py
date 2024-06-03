import pandas as pd

#Função para calcular a variação percentual
def calcular_variacao_percentual(valor_2022, valor_2023):
    try:
        variacao = ((valor_2023 - valor_2022) / valor_2022) * 100
        return variacao
    except ZeroDivisionError:
        return None

# Função para fornecer sugestões baseadas na variação percentual
def fornecer_sugestoes(variacao):
    if variacao is None:
        return "Não foi possível calcular a variação percentual devido a divisão por zero."
    elif variacao > 20:
        return f"As vendas aumentaram {variacao:.2f}%. Sugestão: Bonificação para o time de vendas."
    elif 2 < variacao <= 20:
        return f"As vendas aumentaram {variacao:.2f}%. Sugestão: Pequena bonificação para o time de vendas."
    elif -10 <= variacao <= 2:
        return f"A variação foi de {variacao:.2f}%. Sugestão: Planejamento de políticas de incentivo às vendas."
    elif variacao < -10:
        return f"As vendas diminuíram {variacao:.2f}%. Sugestão: Corte de gastos."
    else:
        return "Sugestão não disponível para esta variação."


# Função principal para analisar as vendas
def analisar_vendas(arquivo_2022, arquivo_2023):
    # Ler todas as abas das planilhas
    vendas_2022 = pd.read_excel(arquivo_2022, sheet_name=None)
    vendas_2023 = pd.read_excel(arquivo_2023, sheet_name=None)

    # Dicionário para armazenar os resultados
    resultados = {}

    for vendedor in vendas_2022.keys():
        if vendedor in vendas_2023:
            # Calcular o total de vendas por ano para o vendedor
            total_2022 = vendas_2022[vendedor]['Valor'].sum()
            total_2023 = vendas_2023[vendedor]['Valor'].sum()

            # Calcular a variação percentual
            variacao = calcular_variacao_percentual(total_2022, total_2023)

            # Obter a sugestão
            sugestao = fornecer_sugestoes(variacao)

            # Armazenar o resultado
            resultados[vendedor] = {
                'Total 2022': total_2022,
                'Total 2023': total_2023,
                'Variação (%)': variacao,
                'Sugestão': sugestao
            }
        else:
            resultados[vendedor] = {
                'Total 2022': vendas_2022[vendedor]['Valor'].sum(),
                'Total 2023': 'N/A',
                'Variação (%)': 'N/A',
                'Sugestão': 'Dados de 2023 não disponíveis para este vendedor.'
            }

    return resultados

# Função para exibir os resultados
def exibir_resultados(resultados):
    for vendedor, dados in resultados.items():
        print(f"\nVendedor: {vendedor}")
        for key, value in dados.items():
            print(f"{key}: {value}")


# Executar a análise de vendas
if __name__ == "__main__":
    arquivo_2022 = 'vendas_2022.xlsx'
    arquivo_2023 = 'vendas_2023.xlsx'

    resultados = analisar_vendas(arquivo_2022, arquivo_2023)
    exibir_resultados(resultados)