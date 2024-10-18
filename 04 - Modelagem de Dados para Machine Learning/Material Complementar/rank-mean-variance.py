import pandas as pd
import numpy as np

# Supondo que você já tenha carregado seus dados em um DataFrame 'df'
# Exemplo: df = pd.read_csv('seu_arquivo.csv')
file_path = 'data/Dados.xlsx'  # Substitua pelo caminho do seu arquivo

df = pd.read_excel(file_path)

# Coluna alvo (perfil)
target_column = 'Q060'

# Preencher valores faltantes com a média da respectiva coluna
df = df.apply(lambda x: x.fillna(x.mean()), axis=0)

# Remover colunas não numéricas, se existirem
df = df.select_dtypes(include=[np.number])

# Separar a coluna alvo (perfil)
target = df[target_column]
df = df.drop(columns=[target_column])

# Função para calcular a relação média/variância


def calc_score(feature, target):
    feature_mean = feature.mean()
    target_mean = target.mean()

    feature_var = feature.var()
    target_var = target.var()

    score = abs(feature_mean - target_mean) / (feature_var + target_var)

    return score


# Calcular os scores de cada variável
ranking = {col: calc_score(df[col], target) for col in df.columns}

# Ordenar pelo score (descendente) e mostrar o ranking
ranked_features = sorted(
    ranking.items(), key=lambda item: item[1], reverse=True)

# Exibir o ranking
print("Ranking das variáveis (da melhor para a pior):")
for i, (feature, score) in enumerate(ranked_features, 1):
    print(f"{i}. {feature} - Score: {score:.4f}")
