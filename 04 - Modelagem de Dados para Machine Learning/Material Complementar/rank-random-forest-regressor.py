import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def rank_features(file_path, target_column):
    # Lê o arquivo .xlsx com o engine especificado
    df = pd.read_excel(file_path)

    # Separa as features (X) e o target (y)
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Substitui dados faltantes pela média das colunas
    imputer = SimpleImputer(strategy='mean')
    X_imputed = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X_imputed, y, test_size=0.3, random_state=42)

    # Treinar um modelo de regressão
    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Importância das features
    feature_importances = model.feature_importances_

    # Cria um DataFrame com as importâncias
    feature_ranking = pd.DataFrame({
        'Feature': X.columns,
        'Importance': feature_importances
    })

    # Ordenar o ranqueamento de forma decrescente
    feature_ranking = feature_ranking.sort_values(by='Importance', ascending=False)

    # Exibir o ranqueamento
    print("Ranqueamento das variáveis mais importantes para descrever o perfil:")
    print(feature_ranking)

# Exemplo de uso
file_path = 'data/Dados2.xlsx'  # Substitua pelo caminho do seu arquivo
target_column = 'Q060'          # A coluna que descreve o perfil

rank_features(file_path, target_column)
