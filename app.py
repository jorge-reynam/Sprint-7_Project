import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de Datos de Vehículos Usados')



#PRIMER HISTOGRAMA

column = st.selectbox(
    'Selecciona la columna para el histograma:',
    ['price', 'model_year', 'cylinders', 'transmission'],
    key='column_selector_1'
)

if st.button('Construir histograma', key='hist_button_1'):
    st.write(f'Creación de un histograma para la columna **{column}**')
    fig = go.Figure(data=[go.Histogram(x=car_data[column])])
    fig.update_layout(title_text=f'Distribución de {column}')
    st.plotly_chart(fig, use_container_width=True)



#GRÁFICO DE DISPERSIÓN

st.title("Visualización de datos de vehículos")

x_axis = st.selectbox(
    'Selecciona la variable para el eje X:',
    ['price', 'model_year', 'cylinders', 'odometer'],
    key='x_axis_selector'
)
y_axis = st.selectbox(
    'Selecciona la variable para el eje Y:',
    ['price', 'model_year', 'cylinders', 'odometer'],
    key='y_axis_selector'
)

if st.button('Construir gráfico de dispersión', key='button_scatter'):
    st.write(f'Gráfico de dispersión entre **{x_axis}** y **{y_axis}**')
    fig_scatter = go.Figure(data=[
        go.Scatter(
            x=car_data[x_axis],
            y=car_data[y_axis],
            mode='markers',
            marker=dict(opacity=0.7)
        )
    ])
    fig_scatter.update_layout(
        title=f'{y_axis} vs {x_axis}',
        xaxis_title=x_axis,
        yaxis_title=y_axis
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    


# COMPARACIÓN DE PRECIOS ENTRE DOS TIPOS DE VEHÍCULOS

st.title("Comparación de precios entre tipos de vehículos")

# Extraer los tipos únicos del DataFrame
vehicle_types = car_data['type'].dropna().unique()

# Selector doble para comparar
type1 = st.selectbox("Selecciona el primer tipo de vehículo:", vehicle_types, key='type_selector_1')
type2 = st.selectbox("Selecciona el segundo tipo de vehículo:", vehicle_types, key='type_selector_2')

# Botón para generar la comparación
if st.button("Comparar precios", key='compare_button'):
    st.write(f"Comparando precios entre **{type1}** y **{type2}**")

    # Filtrar los datos de cada tipo
    data1 = car_data[car_data['type'] == type1]
    data2 = car_data[car_data['type'] == type2]

    # Crear un boxplot para comparar las distribuciones de precio
    fig_compare = go.Figure()
    fig_compare.add_trace(go.Box(y=data1['price'], name=type1, boxmean=True))
    fig_compare.add_trace(go.Box(y=data2['price'], name=type2, boxmean=True))

    # Personalizar diseño
    fig_compare.update_layout(
        title=f"Comparación de precios: {type1} vs {type2}",
        yaxis_title="Precio (USD)",
        boxmode="group"
    )

    # Mostrar el gráfico
    st.plotly_chart(fig_compare, use_container_width=True)

    
