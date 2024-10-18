import pandas as pd
import matplotlib.pyplot as plt

# Substitua pelo caminho do seu arquivo
file_path = 'data/Dados.xlsx'  # Substitua pelo caminho do seu arquivo

# Ler o arquivo .xlsx
df = pd.read_excel(file_path)

# Verificar se as colunas 'P012' e 'Q060' existem no arquivo
if 'P012' in df.columns and 'Q060' in df.columns:
    # Filtrar os dados onde Q060 é 0 e 1
    df_q060_0 = df[df['Q060'] == 0]
    df_q060_1 = df[df['Q060'] == 1]

    # Criar subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    print(df_q060_0['P012'].size, df_q060_1['P012'].size)

    # Histograma onde Q060 é 0
    ax1.hist(df_q060_0['P012'], bins=20, color='green', edgecolor='black', alpha=0.7)
    ax1.set_title('Histograma de P012 quando Q060 = 0')
    ax1.set_xlabel('Valores (P012)')
    ax1.set_ylabel('Frequência')

    # Histograma onde Q060 é 1
    ax2.hist(df_q060_1['P012'], bins=20, color='red', edgecolor='black', alpha=0.7)
    ax2.set_title('Histograma de P012 quando Q060 = 1')
    ax2.set_xlabel('Valores (P012)')
    ax2.set_ylabel('Frequência')

    # Ajustar layout
    plt.tight_layout()

    # Exibir os gráficos
    plt.show()
else:
    print("As colunas 'P012' e 'Q060' não foram encontradas no arquivo.")
