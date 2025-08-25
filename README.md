Predicción de Heladas en Cultivos
Descripción del Proyecto
Este proyecto es una plataforma de predicción inteligente contra heladas diseñada para agricultores. Utiliza datos de sensores en tiempo real para generar alertas precisas y personalizadas, lo que permite a los productores proteger sus cultivos de manera eficiente y reducir gastos operativos innecesarios.

El objetivo es resolver el problema de las pérdidas económicas significativas causadas por heladas inesperadas y la imprecisión de los pronósticos generales.

Características Principales
Análisis Hiperlocal: Recopila datos de sensores a nivel de parcela para una precisión milimétrica.

Algoritmos de Predicción: Utiliza modelos de machine learning para aprender del microclima y predecir el riesgo de heladas.

Alertas Personalizadas: Emite notificaciones confiables con recomendaciones concretas.

Tecnologías Utilizadas
Python: Lenguaje de programación principal para el desarrollo.

Flask: Framework para la creación de la API.

Scikit-learn: Para el entrenamiento y gestión del modelo de predicción.

Joblib: Para serializar y cargar el modelo entrenado.

Pandas: Para la manipulación y el análisis de datos.

Uso de la API
Para probar la API, puedes usar un cliente HTTP como Postman o cURL.

URL: http://127.0.0.1:5000/predict

Método: POST

Cuerpo de la Solicitud (JSON):

JSON

{
  "age": 0.05,
  "sex": 0.05,
  "bmi": 0.05,
  "bp": 0.05,
  "s1": 0.05,
  "s2": 0.05,
  "s3": 0.05,
  "s4": 0.05,
  "s5": 0.05,
  "s6": 0.05
}
