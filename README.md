# El poder viral
*Análisis predictivo de la viralidad de contenidos en Mashable.*

**Carmen Ríos Rodríguez**
*Data Analyst*

## 1. **Objetivo del proyecto**
El objetivo de este proyecto es identificar los factores clave que determinan si un artículo de noticias digitales se convertirá en "viral". Mediante el uso de modelos de Machine Learning, buscamos predecir el éxito de una publicación (medido en número de veces compartida) basándonos en atributos como la temática, el día de publicación, el uso de multimedia y el análisis de sentimiento del texto.

## 2. **Contexto del negocio**
En la era de la saturación de información, del exceso de noticias y la sobreestimulación, entender qué contenidos resuenan con la audiencia es crítico para los medios digitales. Este estudio utiliza un dataset de artículos publicados por Mashable para responder a la pregunta: ¿Podemos predecir la viralidad antes de publicar?

El proyecto incluye:
    * Limpieza exhasutiva del dataset de más de 40 mil registros
    * Un análisis exhaustivo de la correlación entre variables externas (imágenes, enlaces) e internas (subjetividad, polaridad).
    * El entrenamiento y comparación de múltiples modelos de clasificación para determinar la probabilidad de éxito.
    * El despliegue de una herramienta interactiva (Streamlit) que permite a los redactores probar sus artículos antes de lanzarlos.


## 3. Fuentes y variables
- Iniciamos con un dataset con +40 mil registros donde se analizan bajo 63 variables la estructura y la sentimentalidad y viralidad de los artículos de Mashable. 
    #### 3.1. Diccionario original: 
    - Diccionario original de nuestro dataset
        **1. Metadatos del Artículo**

        url: El enlace al artículo (se usa como identificador).

        timedelta: Días transcurridos entre la publicación del artículo y la extracción de los datos.

        n_tokens_title: Número de palabras en el título.

        n_tokens_content: Número de palabras en el contenido del artículo.

        num_keywords: Número de palabras clave asociadas al artículo.

        **2. Contenido y Enlaces**

        n_unique_tokens: Tasa de palabras únicas en el contenido.

        n_non_stop_words: Tasa de palabras que no son "stop words" (palabras comunes como "el", "de", "y").

        n_non_stop_unique_tokens: Tasa de palabras únicas que no son "stop words".

        num_hrefs: Número de enlaces (hipervínculos).

        num_self_hrefs: Número de enlaces que apuntan a otros artículos del mismo Mashable.

        num_imgs / num_videos: Cantidad de imágenes y vídeos incluidos.

        average_token_length: Longitud promedio de las palabras en el contenido.

        **3. Canales de Datos (Temática)**

        Estas son variables binarias (0 o 1). Indican si el artículo pertenece a una categoría específica:

        data_channel_is_lifestyle: Estilo de vida.

        data_channel_is_entertainment: Entretenimiento.

        data_channel_is_bus: Negocios (Business).

        data_channel_is_socmed: Redes Sociales.

        data_channel_is_tech: Tecnología.

        data_channel_is_world: Noticias mundiales.

        **4. Estadísticas de Palabras Clave (Keywords)**

        Miden el éxito previo de las palabras clave utilizadas en el artículo (basado en cuántas veces se compartieron otros artículos con esas mismas keywords):

        kw_min_min / kw_max_min / kw_avg_min: Rendimiento mínimo/máximo/promedio de la palabra clave que peor funcionó.

        kw_min_max / kw_max_max / kw_avg_max: Rendimiento mínimo/máximo/promedio de la palabra clave que mejor funcionó.

        kw_min_avg / kw_max_avg / kw_avg_avg: Rendimiento mínimo/máximo/promedio de la media de las palabras clave.

        **5. Día de la Semana**

        Indican qué día fue publicado el artículo (binarias):

        weekday_is_monday a weekday_is_sunday.

        is_weekend: Indica si se publicó en sábado o domingo.

        **6. NLP y Análisis de Sentimiento**

        LDA_00 a LDA_04: Distribución de 5 temas extraídos mediante Latent Dirichlet Allocation (un algoritmo que agrupa artículos por temas abstractos).

        global_subjectivity: Nivel de subjetividad del texto.

        global_sentiment_polarity: Polaridad del sentimiento general (positivo o negativo).

        global_rate_positive_words / global_rate_negative_words: Tasa de palabras positivas y negativas en el texto.

        avg_positive_polarity / avg_negative_polarity: Promedio de la intensidad de las palabras positivas/negativas.

        title_subjectivity / title_sentiment_polarity: Subjetividad y sentimiento aplicados específicamente al título.

        **7. Variable Objetivo (Target)**

        shares: El número total de veces que el artículo fue compartido en redes sociales. Esta es la métrica de éxito.
    
    #### 3.1. Diccionario final: 
    -  El dataset final (df_final.csv) es el resultado de un proceso de limpieza y selección de características:
        * Rendimiento histórico: rendimiento_promedio_media.
        * Contenido multimedia: num_enlaces, num_imgs.
        * Análisis de texto: subjetividad_global, polaridad_negativa_media, subjetividad_titulo.
        * Temporalidad: fin_de_semana.
        * Target: es_viral (variable binaria).


## 4. Metodología y modelos
Se probaron diversos enfoques para maximizar la capacidad predictiva:

    * K-Nearest Neighbors (KNN): Utilizado inicialmente para explorar agrupamientos y regresión básica.

    * Modelos de ensamble: Se compararon Random Forest, AdaBoost y Gradient Boosting.

También hubo una optimización de los dos modelos que mejor funcionaron. Se realizó una búsqueda de hiperparámetros mediante GridSearchCV y RandomizedSearchCV para ajustar el modelo final.

- ´Modelo Final´: Un Random Forest Classifier optimizado (500 estimadores) que equilibra precisión y generalización, integrado en el backend de la aplicación.
Este modelo funciona como una estructura colectiva que combina las conclusiones de múltiples árboles de decisión independientes. Al procesar fragmentos de información de manera aleatoria y alejar el sesgo individual, logramos una exactitud de casi el 65%.

Este modelo es el motor de nuestra herramienta predictiva, permitiendo a los redactores prever si un futuro artículo tiene el potencial de "romper el silencio" digital.

## 5. Algunos resultados
¿Qué hace que una historia se vuelva viral?
Tras analizar el comportamiento digital, identificamos cuatro pilares psicológicos que los datos confirman como motores de la viralidad:
* Emoción intensa: Sorpresa, indignación, ternura o miedo.
* Identificación personal: El lector se ve reflejado.
* Utilidad práctica: Contenido que resuelve o enseña.
* Capacidad de conversación: Historias que impulsan a ser compartidas para generar debate

## 6. Limitaciones
* Complejidad de variables: La enorme cantidad de variables y, en ocasiones, su débil correlación directa inicial, supuso un reto para el ajuste del modelo.
* Evolución del comportamiento: El modelo requiere entrenamiento continuo con nuevos entornos y datos para seguir el ritmo de la cambiante conducta de los usuarios.
* Subjetividad del éxito: La viralidad se define mediante un umbral (threshold) de "shares", lo cual puede variar según la categoría del artículo.
* Datos temporales: El análisis se basa en una captura estática de datos; no considera tendencias virales de última hora o eventos globales impredecibles.
* Balance de clases: Se observó una distribución desigual entre artículos virales y no virales, lo que requirió ajustes en las métricas de evaluación (Accuracy vs. F1-Score).

## 7. Próximos pasos
* Análisis NLP avanzado: Incorporar modelos de lenguaje (como BERT) para entender mejor el contexto semántico más allá de la polaridad básica.
* Segmentación por red social: Diferenciar si un artículo es viral en X (Twitter), Facebook o LinkedIn de forma independiente.
* Actualización en tiempo real: Conectar la aplicación a una API de noticias para analizar tendencias en vivo.

## 8. Cómo replicar el proyecto
    a. Clonar el repositorio.
    b. Instalar librerías: pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit.
    c. Preparación de datos: Ejecutar el notebook 01. Limpieza (El poder viral).ipynb para generar los archivos procesados.
    d. Entrenamiento: Los notebooks 02, 03 y 04 contienen el flujo de experimentación de modelos.
    e. Ejecutar la App: ```bash
    streamlit run app.py


`Dominar la viralidad no es solo predecir un éxito, es asegurar que nuestras voces no se pierdan en el vacío y que cada mensaje encuentre su eco en el corazón del lector.`