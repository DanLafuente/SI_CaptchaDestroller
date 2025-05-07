# SI_CaptchaDestroller
SIUUUUUUUUUU
El problema a solucionar: Ser capaz de leer y escribir un captcha

Metodo de resolucion: principalemte CNN y RNN mas tarde (la base es CNN)

1. Problema simple: reconocer digitos deformados
2. Prblema compuesto: reconocer una cadena de digitos y letras bien separadas (que los caracteres no se junten)
3. PROBLEMA BOSS: reconocer digitos y letras que se juntan/mezclan (sería ser capaces de separar las letras y digitos que se han solapado)
   

## Cosas que creo que no podemos usar

### 1. Scikit-learn (sklearn):  Aprendizaje automático clásico.
(seguro que no)
#### 1.1. XGBoost: Modelos de boosting muy eficientes, ideal para competiciones como Kaggle.
#### 1.2. LightGBM: Similar a XGBoost pero más rápido en grandes volúmenes de datos.
#### 1.3. CatBoost: Ideal para datos categóricos, sin necesidad de codificación manual.
#### 1.4. TPOT: AutoML basado en evolución genética, busca el mejor pipeline de modelos.
#### 1.5. MLJAR: AutoML sin código para clasificación y regresión.
(ya no estoy tan seguro)
#### 1.6. H2O.ai: Plataforma de ML escalable, soporta autoML, redes neuronales, y más.
#### 1.7. Orange: Librería y entorno visual para machine learning.

### 2. Seaborn: Visualización estadística (que no podemos visualizar?)
(seguramente que no)
#### 2.1. Plotly: Gráficos interactivos, ideal para dashboards y aplicaciones web apps.
#### 2.2. Bokeh: Interactividad avanzada y fácil integración con el navegador.
#### 2.3. Holoviews: Alta abstracción sobre Bokeh/Matplotlib; ideal para análisis exploratorio.
#### 2.4. ggplot (Python): Inspirado en ggplot2 de R, permite visualización declarativa.
(ya no estoy tan seguro)
#### 2.5. Altair: Sintaxis declarativa y sencilla. Basado en Vega-Lite.
(supongo que si)
#### 2.6. Matplotlib: Base de casi todas las librerías de visualización en Python. Muy flexible.

### 3. Mirar:
(mirar) =>	TensorFlow, PyTorch, Keras (Deep Learning)

(mirar) =>	cv2 (OpenCV) (procesar imágenes y videos) ->
pip install opencv-python
pip install opencv-contrib-python