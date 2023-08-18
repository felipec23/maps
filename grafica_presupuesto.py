import streamlit as st
import pandas as pd
import numpy as np

# Set streamlit page config to wide
st.set_page_config(layout="wide")

df = pd.read_excel("Ubicaciones colegios Cucuta.xlsx")

# Crear columna con costo total del proyecto, es un valor aleatorio entre 60000000 y 1500000000
df['Costo total'] = df['Codigo DANE'].apply(lambda x: np.random.randint(60000000, 1500000000))

proyectos = [
    "Renovación de aulas con equipos audiovisuales modernos",
    "Construcción de una biblioteca amplia y bien equipada",
    "Instalación de paneles solares para energía renovable",
    "Renovación de laboratorios de ciencias con equipos de última generación",
    "Construcción de un gimnasio cubierto",
    "Creación de áreas verdes y espacios de recreación al aire libre",
    "Mejora de la accesibilidad para personas con discapacidad",
    "Renovación de baños y servicios sanitarios",
    "Ampliación de la cafetería y áreas de descanso",
    "Construcción de una pista deportiva multifuncional",
    "Instalación de sistemas de purificación de agua potable",
    "Mejora de la conectividad Wi-Fi en todo el campus",
    "Creación de un centro de orientación vocacional",
    "Renovación de salones de música y arte",
    "Implementación de aulas virtuales y plataformas de e-learning",
    "Construcción de un auditorio para eventos y conferencias",
    "Instalación de sistemas de climatización eficiente",
    "Renovación de la infraestructura de laboratorios informáticos",
    "Creación de un huerto escolar y programas de educación ambiental",
    "Mejora de la seguridad mediante cámaras y sistemas de control de acceso",
    "Construcción de una pista de atletismo",
    "Instalación de espacios para clases al aire libre",
    "Renovación de la infraestructura de la cocina y comedor",
    "Creación de un centro de apoyo psicopedagógico",
    "Implementación de sistemas de gestión de residuos",
    "Construcción de aulas especializadas para actividades extracurriculares",
    "Instalación de estaciones de carga para vehículos eléctricos",
    "Renovación de la infraestructura de laboratorios de idiomas",
    "Desarrollo de áreas para experimentos y proyectos científicos",
    "Creación de un vivero para plantas y árboles autóctonos"
]

# Crear columna con proyecto aleatorio
df['Proyecto'] = df['Codigo DANE'].apply(lambda x: np.random.choice(proyectos))
df['Grupo de impacto'] = df['Codigo DANE'].apply(lambda x: np.random.choice(["Primaria", "Secundaria", "Media"]))
df["Meses de ejecución"] = df['Codigo DANE'].apply(lambda x: np.random.randint(1, 8))
import plotly.express as px
   
# Display map
fig = px.scatter_mapbox(df,
                        lat="lat",
                        lon="lon",
                        hover_name="Proyecto",
                        center={'lat': 7.904151632106986, 'lon': -72.50514508890222},
                        # size='Costo total',
                        color_discrete_sequence=px.colors.qualitative.Safe,
                        hover_data={
                            "lat": False,
                            "lon": False,
                            "Institución educativa": True,
                            "Codigo DANE": True,
                            "Proyecto": False,
                            "Costo total": True,
                            "Grupo de impacto": True,
                            "Meses de ejecución": True},
                        # title="Organizaciones por ubicación",
                        zoom=11.9,
                        height=500,
                        
                        )

fig.update_layout(mapbox_style="carto-positron")

st.sidebar.markdown('## Filtros')

# Filtro por grupo de impacto
grupo_impacto = st.sidebar.selectbox(
    'Grupo de impacto',
    df['Grupo de impacto'].unique()
)

# Decrease or increase margins
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":5})

titulo = 'Proyectos de infraestructura educativa en Cúcuta'

container_titulo = st.container()
container_map = st.container()
container_map.plotly_chart(fig, use_container_width=True)
container_titulo.header(titulo)
container_titulo.markdown('Cada círculo representa un proyecto.')
