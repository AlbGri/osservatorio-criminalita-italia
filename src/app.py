import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# Configurazione pagina
st.set_page_config(
    page_title="Osservatorio Criminalità Italia",
    layout="wide"
)

# Header
st.title("Osservatorio Criminalità Italia")
st.subheader("Dashboard interattiva - Fase 0 MVP")

# Divider
st.divider()

# Sezione 1: Info progetto
st.header("Progetto")
st.write("""
Questo è un progetto di visualizzazione dati sulla criminalità in Italia 
basato su fonti ufficiali (ISTAT, Ministero dell'Interno).
""")

# Sezione 2: Trend Delitti con Dati Normalizzati
st.header("Trend Delitti Denunciati in Italia (2014-2023)")

# Box giallo avviso limiti dati
st.warning("""
**Nota metodologica importante:**  
Questi dati mostrano **denunce registrate**, non crimini effettivamente commessi. 
Alcuni reati hanno bassa propensione alla denuncia (es. violenze domestiche), 
altri alta (es. furti auto assicurati). Il grafico riflette sia la criminalità reale 
che la propensione a denunciare e l'efficienza delle forze dell'ordine.
""")

# Carica dati normalizzati
df_normalizzato = pd.read_csv('data/processed/delitti_italia_normalizzato_2014_2023.csv')

# Mostro dataframe
with st.expander("Vedi dati"):
    st.dataframe(df_normalizzato)

# LINE CHART con Plotly Graph Objects
fig_line = go.Figure()

# Traccia principale: tasso normalizzato
fig_line.add_trace(go.Scatter(
    x=df_normalizzato['Anno'],
    y=df_normalizzato['Tasso_per_1000'],
    mode='lines+markers',
    name='Tasso delitti per 1000 abitanti',
    line=dict(color='#2E86AB', width=3),
    marker=dict(size=10)
))

# Evidenziare periodo COVID (2020-2021) con area ombreggiata
fig_line.add_vrect(
    x0=2019.5, x1=2021.5,
    fillcolor='rgba(255, 0, 0, 0.1)',
    layer='below',
    line_width=0,
    annotation_text='Periodo COVID-19',
    annotation_position='top left',
    annotation=dict(font_size=10, font_color='red')
)

# Layout customizzato
fig_line.update_layout(
    title='Tasso Delitti Denunciati per 1000 Abitanti - Italia (2014-2023)',
    xaxis_title='Anno',
    yaxis_title='Delitti per 1000 Abitanti',
    hovermode='x unified',
    template='plotly_white',
    height=550
)

st.plotly_chart(fig_line, use_container_width=True)

# Statistiche chiave
col1, col2, col3 = st.columns(3)
with col1:
    variazione = ((df_normalizzato.iloc[-1]['Tasso_per_1000'] - df_normalizzato.iloc[0]['Tasso_per_1000']) / df_normalizzato.iloc[0]['Tasso_per_1000']) * 100
    st.metric("Variazione tasso 2014-2023", f"{variazione:.2f}%")
with col2:
    st.metric("Anno minimo", f"{df_normalizzato.iloc[df_normalizzato['Tasso_per_1000'].idxmin()]['Anno']:.0f}")
with col3:
    st.metric("Anno massimo", f"{df_normalizzato.iloc[df_normalizzato['Tasso_per_1000'].idxmax()]['Anno']:.0f}")

st.divider()

# Sezione 3: Tutorial Plotly - Bar Chart (manteniamo con dati dummy per esempio)
st.header("Confronto Tipologie Delitti (Dati Dummy)")

# Dati dummy per bar chart
tipologie = ['Furti', 'Rapine', 'Truffe', 'Lesioni', 'Danneggiamenti']
valori = np.random.randint(100000, 800000, size=len(tipologie))

df_bar = pd.DataFrame({
    'Tipologia': tipologie,
    'Casi': valori
})

# BAR CHART con Plotly Express (più veloce per grafici semplici)
fig_bar = px.bar(
    df_bar,
    x='Tipologia',
    y='Casi',
    title='Delitti per Tipologia - Anno 2024',
    color='Casi',
    color_continuous_scale='Blues'
)

# Customizzazioni layout
fig_bar.update_layout(
    xaxis_title='Tipologia Delitto',
    yaxis_title='Numero Casi',
    template='plotly_white',
    height=500,
    showlegend=False
)

st.plotly_chart(fig_bar, use_container_width=True)

# Nota tecnica
st.info("I dati del secondo grafico sono casuali e servono solo per dimostrare le capacità di Plotly. Verranno sostituiti con dati reali nelle prossime fasi.")

# Footer
st.divider()
st.caption("Fase 0 - Settimana 1 | Repository: [GitHub](https://github.com/AlbGri/osservatorio-criminalita-italia)")