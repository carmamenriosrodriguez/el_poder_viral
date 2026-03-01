import streamlit as st
import backend
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="El poder viral", layout="wide")

@st.cache_resource
def main():
    return backend.aplicar_rnd()

model, columnas = main()

col_title, col_img = st.columns([2, 1]) 
with col_title:
    st.title("El poder viral: del dato al hecho")
    st.markdown("### Carmen Ríos, *Data Analyst from Mashable**")
with col_img:
    st.image("https://media.licdn.com/dms/image/sync/v2/D4E27AQGMuY35nq_RDw/articleshare-shrink_800/B4EZl8Chr8GoAI-/0/1758722662629?e=2147483647&v=beta&t=O_5lLNlznVtthxcdMVgaAk6UH-42VahSKbGeUOmw2As", width=300)

#(para agrandar la letra he introducido esto que he tenido que mirar):
st.markdown("""
    <style>
    .stTabs [data-baseweb="tab"] p {
        font-size: 22px; 
        font-weight: bold;
        color: #D1BBFF;
    }
    .stTabs [aria-selected="true"] p {
        color: #FFFFFF !important;
    }
    .stTabs [aria-selected="true"] {
        border-bottom-color: #FFFFFF !important;
    }
    .stTabs [data-baseweb="tab"]:hover p {
        color: #F0E6FF;
    }
    </style>
    """, unsafe_allow_html=True)

introducción, experimento, visualizaciones, machine_learning, modelo = st.tabs([
    "-Contexto-", 
    "-Experimento-",
    "-KPIs-",
    "-Machine Learning-", 
    "-Predicción- "
])

 #1
with introducción:
    st.markdown("# :yellow[**- El relato de las nuevas historias -**]")
    col1, col2 = st.columns([2,1])
    with col1:
        st.markdown("### :violet[🌍 El contexto]")
        st.write("##### - Redes, algoritmos, plataformas... todo está conectado.")
        
        st.markdown("### :violet[📈 El reto]")
        st.write(" #####  - No es crear historias, es hacer que lleguen.")

        st.markdown("### :violet[💥 El impacto]")
        st.write("##### - Las historias no han perdido fuerza... **su impacto se ha multiplicado**.")
        
        st.markdown("### :violet[💾 La clave]")
        st.write("##### - Los datos permiten entender cómo actúan los usuarios.") 
    with col2:
        st.image("https://i.pinimg.com/736x/c7/02/49/c70249e7b2014bbf2e51e76117bea456.jpg", caption="Nuestros lectores")

    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px; margin-bottom: 0px;">
            <h2 style="color: white; font-weight: bold; margin-bottom: 5px;">
                ¿Qué hace que una historia se vuelva viral?
            </h2>
            <hr style="border: 0; height: 2px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), #7d4cfc, rgba(0, 0, 0, 0)); width: 50%; margin: auto;">
        </div>
        """, 
        unsafe_allow_html=True
)
    st.divider()
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px; margin-bottom: 50px; padding: 20px;">
            <blockquote style="font-size: 20px; font-style: italic; color: #E0E0E0; border: none; margin-bottom: 20px;">
                "You're never going to kill storytelling, because it's built into the human plan. We come with it."
            </blockquote>
            <cite style="display: block; font-size: 16px; color: #7d4cfc; font-weight: bold; margin-top: 20px;">
                — Margaret Atwood
            </cite>
        </div>
        """, 
        unsafe_allow_html=True
    )


#2
with experimento:

    st.markdown("# :yellow[- ¿Qué hace que una historia se vuelva viral? -]")
    st.markdown("### **+39,000 registros** analizados bajo 63 variables resumidas en:")

    
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    estilo_tarjeta = """
        <div style="
            background-color: rgba(125, 76, 252, 0.15); 
            border: 1px solid #7d4cfc; 
            padding: 10px; 
            border-radius: 10px; 
            height: 180px; 
            color: white;
            line-height: 1.3;
            overflow: hidden;">
            <b style="color: #a582ff; font-size: 27px; text-transform: uppercase; display: block; margin-bottom: 10px;">
                {titulo}
            </b>
            <p style="font-size: 20px; margin-top: 5px; color: #E0E0E0;">
                {contenido}
            </p>
        </div>
    """

    with c1:
        st.markdown(estilo_tarjeta.format(titulo="Día de publicación", contenido="Lunes, martes, miércoles, jueves, viernes, sábado o domingo."), unsafe_allow_html=True)
    with c2:
        st.markdown(estilo_tarjeta.format(titulo="Temática", contenido="Lifestyle, negocios, entretenimiento, tecnología, redes sociales y noticias globales."), unsafe_allow_html=True)
    with c3:
        st.markdown(estilo_tarjeta.format(titulo="Metadatos", contenido="URLs, número de palabras en el título..."), unsafe_allow_html=True)
    with c4:
        st.markdown(estilo_tarjeta.format(titulo="Contenido", contenido="Tasas de palabras únicas, imágenes..."), unsafe_allow_html=True)
    with c5:
        st.markdown(estilo_tarjeta.format(titulo="Éxito previo", contenido="Rendimiento de palabras clave..."), unsafe_allow_html=True)
    with c6:
        st.markdown(estilo_tarjeta.format(titulo="Sentimiento", contenido="Subjetividad, polaridad y algoritmo LDA."), unsafe_allow_html=True)
 
    st.divider()
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px; margin-bottom: 50px; padding: 20px;">
            <blockquote style="font-size: 20px; font-style: italic; color: #E0E0E0; border: none; margin-bottom: 20px;">
                "No hay peor agonía que llevar con nosotros una historia que no ha sido contada"
            </blockquote>
            <cite style="display: block; font-size: 16px; color: #7d4cfc; font-weight: bold; margin-top: 20px;">
                — Maya Angelou.
            </cite>
        </div>
        """, 
        unsafe_allow_html=True
    )

#3
with visualizaciones: 
    st.markdown("# :yellow[ - ¿Qué nos dicen nuestros datos? -]")
    df_graficos = backend.cargar_datos()
    f1, f2, f3, f4 = backend.crear_visualizaciones(df_graficos)

    col_left, col_right = st.columns(2)

    with col_left:
        st.write("### ¿Influye el día de publicación?")
        st.pyplot(f1)
        st.write("### Psicología del contenido")
        st.pyplot(f3)

    with col_right:
        st.write("### El valor del contenido visual")
        st.pyplot(f2)
        st.write("### Rendimiento por temática")
        st.pyplot(f4)

    st.divider()


    st.title("Las respuestas claves:")

    st.markdown("""
        <style>
        .revelar-caja {
            background-color: #E6E6FA; 
            color: #E6E6FA;           /* Texto oculto al inicio */
            padding: 10px;           
            text-align: center;
            border-radius: 12px;
            font-size: 24px;          
            font-weight: 900;         
            height: 120px;            
            transition: 0.4s;
            cursor: pointer;
            border: 2px solid #D8BFD8;
            display: flex;
            align-items: center;
            justify-content: center;
            line-height: 1.1;         
        }
        .revelar-caja:hover {
            background-color: #DDA0DD; 
            color: #4B0082 !important; 
            transform: scale(1.05);    
        }
        </style>
    """, unsafe_allow_html=True)

    columns = st.columns(4)
    respuestas = [
        "Emoción intensa", 
        "Identificación personal", 
        "Utilidad práctica", 
        "Conversación"
    ]

    for i, texto in enumerate(respuestas):
        with columns[i]:
            # Usamos st.markdown para renderizar cada caja con el nuevo estilo
            st.markdown(f'<div class="revelar-caja">{texto}</div>', unsafe_allow_html=True)

    st.divider()
    st.markdown(
            """
            <div style="text-align: center; margin-top: 50px; margin-bottom: 50px; padding: 20px;">
                <blockquote style="font-size: 20px; font-style: italic; color: #E0E0E0; border: none; margin-bottom: 20px;">
                    "La tecnología es una palabra que describe algo que no funciona todavía."
                </blockquote>
                <cite style="display: block; font-size: 16px; color: #7d4cfc; font-weight: bold; margin-top: 20px;">
                    — Douglas Adams.
                </cite>
            </div>
            """, 
            unsafe_allow_html=True
            )



#4

with machine_learning:
    st.markdown("# :yellow[- ¿Podemos predecir la viralidad? -]")
    st.markdown("## :violet[🌱 El modelo Random Forest]")
    st.write("""
    #### Probamos diferentes modelos y encontramos uno: el modelo de **Random Forest**.""")
    st.write("""
    ##### Combina múltiples árboles de decisión independientes para obtener 
    ##### un resultado final más preciso y estable.
    """)



    col_m1, col_m2 = st.columns([4, 1], gap="large")
    with col_m1:
        st.write("## :violet[**¿Cómo aprendió nuestra IA?**]")
        st.markdown("""
        1. #### **Entrenamiento:** Miles de ejemplos con respuesta conocida.
        2. #### **Aprendizaje:** Buscando patrones (ej. relación entre 'palabra' y éxito).
        3. #### **Predicción:** Procesando datos nuevos a través de su estructura colectiva.
        4. #### **Comprobación:** Evaluar si nuestro modelo funciona. 
        """)
        st.metric("Exactitud de predicción", "65%", delta="RF Model")
            
    with col_m2:
        st.image("https://i.pinimg.com/1200x/69/3a/6a/693a6a2ca237180d02ac6139a590aab9.jpg", caption = "**El nuevo modelo**",  use_container_width=True)
        
    st.divider()        
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px; margin-bottom: 50px; padding: 20px;">
            <blockquote style="font-size: 20px; font-style: italic; color: #E0E0E0; border: none; margin-bottom: 20px;">
                "We read to find out who we are. What other people, real or imaginary, do and think and feel... is an essential guide to our understanding of what we ourselves are and may become."
            </blockquote>
            <cite style="display: block; font-size: 16px; color: #7d4cfc; font-weight: bold; margin-top: 20px;">
                — Ursula K. Le Guin.
            </cite>
        </div>
        """, 
        unsafe_allow_html=True
        )


# 4

st.markdown("""
    <style>
    /* Cambia el tamaño de las etiquetas (labels) de los inputs */
    .stWidget label p {
        font-size: 20px !important;
        font-weight: bold;
    }
    
    /* Cambia el tamaño del texto dentro de los selectbox y inputs numéricos */
    .stSelectbox div[data-baseweb="select"] div, 
    .stNumberInput input {
        font-size: 18px !important;
    }

    /* Cambia el tamaño de los números sobre los sliders */
    .stSlider div[data-testid="stTickBarMin"], 
    .stSlider div[data-testid="stTickBarMax"],
    .stSlider div[role="slider"] {
        font-size: 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)

with modelo:
    st.markdown("# :yellow[- Probador de historias -]")
    st.markdown("## Introduce las características de tu próximo artículo:")
    
    with st.form("form_rf"):
        f1, f2 = st.columns(2)
        with f1:
            tematica = st.selectbox("Tema", options=list(backend.dic_temas.keys()), format_func=lambda x: backend.dic_temas[x])
            keywords = st.slider("Palabras clave", 1, 20, 7)
            imgs = st.number_input("Cantidad de imágenes", 0, 50, 1)
            enlaces = st.number_input("Cantidad de enlaces", 0, 50, 5)
            finde = st.radio("¿Publicarás en fin de semana?", [0, 1], format_func=lambda x: "Sí" if x == 1 else "No")


        with f2:
            abs_sent = st.slider("Emotividad del título", 0.0, 1.0, 0.5)
            subjetividad = st.slider("Nivel de subjetividad", 0.0, 1.0, 0.5)
            pol_neg = st.slider("Polaridad negativa", -1.0, 0.0, -0.2)
            subj_titulo = st.slider("Subjetividad del título", 0.0, 1.0, 0.5)
            rendimiento = st.slider("¿Cuántos shares sueles tener?", 0, 65000, 15000)
        
        btn = st.form_submit_button("Voy a tener suerte 🔮")

    if btn:
        datos = [rendimiento, enlaces, imgs, keywords, subjetividad, finde, pol_neg, subj_titulo, abs_sent, tematica]
        res, prob = backend.hacer_prediccion(model, columnas, datos)
        
        if res == 1:
            st.success(f"### ¡Viral! \nProbabilidad de éxito: **{prob:.2%}**")
            st.balloons()
        else:
            st.warning(f"### ¡Puedes mejorar! \nProbabilidad de éxito: **{prob:.2%}**")
    
    st.divider()
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px; margin-bottom: 50px; padding: 20px;">
            <blockquote style="font-size: 20px; font-style: italic; color: #E0E0E0; border: none; margin-bottom: 20px;">
                "Cualquier tecnología lo suficientemente avanzada es indistinguible de la magia"
            </blockquote>
            <cite style="display: block; font-size: 16px; color: #7d4cfc; font-weight: bold; margin-top: 20px;">
                — Arthur C. Clarke.
            </cite>
        </div>
        """, 
        unsafe_allow_html=True
        )