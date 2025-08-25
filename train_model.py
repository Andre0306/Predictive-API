import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# 1. Cargar el conjunto de datos (puedes descargarlo de Kaggle o usar un dataset de ejemplo)
# Para este ejemplo, usaremos un dataset pre-cargado.
from sklearn.datasets import load_diabetes
diabetes_data = load_diabetes()
df = pd.DataFrame(data=diabetes_data.data, columns=diabetes_data.feature_names)
df['target'] = diabetes_data.target

# 2. Preprocesar los datos
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Entrenar el modelo
model = LogisticRegression(max_iter=200) # Se aumenta max_iter para evitar advertencias
model.fit(X_train, y_train)

# 4. Guardar el modelo en un archivo para usarlo en la API
joblib.dump(model, 'diabetes_model.pkl')
print("Modelo guardado exitosamente como 'diabetes_model.pkl'")