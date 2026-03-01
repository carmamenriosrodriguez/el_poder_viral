import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt

def aplicar_rnd():
    df = pd.read_csv('df_final.csv')
    features = df.drop(columns=['es_viral'])
    target = df['es_viral']
    model = RandomForestClassifier(n_estimators=500, max_leaf_nodes=16, 
                                 n_jobs=-1, random_state=0)
    model.fit(features, target)
    
    return model, features.columns.tolist()

def hacer_prediccion(model, columns, datos_usuario):
    input_df = pd.DataFrame([datos_usuario], columns=columns)
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]
    return pred, prob

def obtener_importancia_variables(model, columns):
    importancias = pd.Series(model.feature_importances_, index=columns)
    return importancias.sort_values(ascending=False)

def cargar_datos():
    return pd.read_csv('df.csv')

def crear_visualizaciones(df):
    sns.set_theme(style="white")
    
    size = (6, 5)

    fig1, ax1 = plt.subplots(figsize = size)
    sns.barplot(
        x='fin_de_semana', 
        y='num_compartidos', 
        data=df, 
        palette='magma', 
        ax=ax1, 
        errorbar=None
    )
    ax1.set_title('Promedio de alcance: Día laboral vs Fin de semana')
    ax1.set_xticklabels(['Día laboral', 'Fin de semana'])
    ax1.set_ylabel('Promedio de compartidos')
    ax1.set_xlabel('')
    

    fig1, ax1 = plt.subplots(figsize = size)
    sns.barplot(x='fin_de_semana', y='num_compartidos', data=df, 
                palette='magma', ax=ax1, errorbar=None)
    ax1.set_title('Impacto del día de publicación')
    ax1.set_xticklabels(['Día Laboral', 'Fin de Semana'])
    ax1.set_ylabel('Media de Compartidos')
    ax1.set_xlabel('')
    fig2, ax2 = plt.subplots()
    cols = ['num_imgs', 'num_videos', 'num_palabras_contenido', 'num_compartidos']
    nombres_bien = ['Imágenes', 'Vídeos', 'Nº palabras', 'Shares']
    df_corr = df[cols].copy()
    df_corr.columns = nombres_bien
    sns.heatmap(df_corr.corr(), annot=True, cmap='magma', ax=ax2)


    fig3, ax3 = plt.subplots(figsize=size)
    sample = df.sample(min(1000, len(df)))
    sns.scatterplot(data=sample, x='subjetividad_global', y='polaridad_global', 
                    size='num_compartidos', hue='num_compartidos', alpha=0.5, ax=ax3)
    ax3.set_title('Análisis de Sentimiento')
    ax3.set_xlabel('Subjetividad Global')
    ax3.set_ylabel('Polaridad Global')
    plt.tight_layout()

 
    fig4, ax4 = plt.subplots(figsize=size)
    dic_nombres_cat = {
        'lifestyle': 'Lifestyle', 'entretenimiento': 'Entretenimiento',
        'negocios': 'Negocios', 'redes_sociales': 'Redes sociales',
        'tecnologia': 'Tecnología', 'noticias_globales': 'Noticias globales'
    }
    medias = {dic_nombres_cat[c]: df[df[c] == 1]['num_compartidos'].mean() for c in dic_nombres_cat.keys()}
    df_plot = pd.DataFrame(list(medias.items()), columns=['Cat', 'Mean']).sort_values('Mean')
    sns.barplot(x='Mean', y='Cat', data=df_plot, palette='magma', ax=ax4, errorbar=None)
    ax4.set_title('Rendimiento por tsemática', pad=20, fontweight='bold')
    ax4.set_ylabel('Temática')
    ax4.set_xlabel('Media de compartidos')
    plt.tight_layout()

    return fig1, fig2, fig3, fig4

dic_temas = {
    0: "Entretenimiento",
    1: "Lifestyle",
    2: "Negocios",
    3: "Noticias globales",
    4: "Redes sociales",
    5: "Tecnología"
}

