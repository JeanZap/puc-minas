# Importar bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score

# Carregar a base de dados (substitua 'seu_arquivo.csv' pelo nome do seu arquivo)
df = pd.read_excel('data/Dados.xlsx')

# Separar as features (X) e a coluna alvo (y)
X = df.drop(columns=['Q060'])  # Remover a coluna Q060 das features
y = df['Q060']  # Definir a coluna Q060 como alvo

# Dividir os dados em treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo da árvore de decisão
tree_model = DecisionTreeClassifier(random_state=42)

# Treinar o modelo com os dados de treino
tree_model.fit(X_train, y_train)

# Fazer previsões com os dados de teste
y_pred = tree_model.predict(X_test)

# Avaliar a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy * 100:.2f}%')

# Calcular a F1-Score (média ponderada)
fmeasure = f1_score(y_test, y_pred, average='weighted')
print(f'F1-Score (medida-F): {fmeasure:.2f}')

# Relatório detalhado de classificação
print('Relatório de Classificação:')
print(classification_report(y_test, y_pred))