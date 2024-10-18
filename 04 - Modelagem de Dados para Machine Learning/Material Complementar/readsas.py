# import pandas as pd

# # Definir o caminho do arquivo de texto
# file_path = 'data\PNS_2013_small.txt'

# # Definir os nomes das colunas e as larguras fixas dos campos
# column_names = [
#     'V0001', 'V0024', 'UPA_PNS',    'V0006_PNS',    'UPA',  'V0015',    'V0020',
#     'V0022', 'V0026', 'V0031',      'V0025',        'A001', 'A002',     'A003',
#     'A004',  'A005',  'A006',       'A007',         'A008', 'A009',     'A010',
# ]

# # Definir as larguras correspondentes às colunas com base nas posições do código SAS
# column_widths = [
#     2, 7, 7, 4, 9, 2, 4,
#     2, 1, 1, 1, 1, 1, 1,
#     1, 1, 1, 1, 1, 2, 2
# ]

# # Ler o arquivo com larguras fixas
# df = pd.read_fwf(file_path, widths=column_widths, names=column_names)

# # Exibir uma amostra de 5 linhas do DataFrame
# print(df.sample(5))


import pandas as pd
import matplotlib.pyplot as plt


def sample_from_xlsx(file_path, column_name):
    # Lê o arquivo .xlsx com o engine especificado
    df = pd.read_excel(file_path)

    print(df.__len__)
    # Plotar o histograma da coluna selecionada
    plt.hist(df[column_name], bins=10, edgecolor='black')
    plt.title(f'Histograma da coluna {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequência')
    plt.show()


# Exemplo de uso
file_path = 'data/Dados.xlsx'  # Substitua pelo caminho do seu arquivo
column_name = 'P012'  # Substitua pelo nome da coluna que deseja plotar

sample_from_xlsx(file_path, column_name)
