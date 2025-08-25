from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Inicializar la aplicación Flask
app = Flask(__name__)

# Cargar el modelo de machine learning pre-entrenado
model = joblib.load('diabetes_model.pkl')

# Definir un endpoint para las predicciones
@app.route('/predict', methods=['POST'])
def predict():
    # 1. Obtener los datos de la solicitud (request) en formato JSON
    data = request.get_json(force=True)

    # 2. Convertir los datos de la solicitud a un DataFrame de Pandas
    # Los nombres de las columnas deben coincidir con las características del modelo
    input_data = pd.DataFrame([data])

    # 3. Realizar la predicción
    prediction = model.predict(input_data)

    # 4. Convertir el resultado de la predicción a un formato legible (lista)
    output = prediction.tolist()

    # 5. Devolver la predicción en formato JSON
    return jsonify({'prediction': output})

# Ejecutar la aplicación
if __name__ == '__main__':
    # La aplicación se ejecutará en http://127.0.0.1:5000
    app.run(debug=True)