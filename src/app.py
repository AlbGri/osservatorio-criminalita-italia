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

# Sezione 2: Trend Delitti con Dati Reali ISTAT
st.header("Trend Delitti Denunciati in Italia (2014-2023)")

# Carica dati puliti
df_totale = pd.read_csv('data/processed/delitti_totale_italia_2014_2023.csv')

# Mostro dataframe
with st.expander("Vedi dati"):
    st.dataframe(df_totale)

# LINE CHART con Plotly Graph Objects
fig_line = go.Figure()

fig_line.add_trace(go.Scatter(
    x=df_totale['Anno'],
    y=df_totale['Delitti'],
    mode='lines+markers',
    name='Delitti denunciati',
    line=dict(color='#2E86AB', width=3),
    marker=dict(size=8)
))

# Layout customizzato
fig_line.update_layout(
    title='Trend Delitti Denunciati in Italia (2014-2023)',
    xaxis_title='Anno',
    yaxis_title='Numero Delitti Denunciati',
    hovermode='x unified',
    template='plotly_white',
    height=500
)

# Formattazione asse y con separatore migliaia
fig_line.update_yaxes(tickformat=',')

st.plotly_chart(fig_line, use_container_width=True)

# Statistiche chiave
col1, col2, col3 = st.columns(3)
with col1:
    variazione = ((df_totale.iloc[-1]['Delitti'] - df_totale.iloc[0]['Delitti']) / df_totale.iloc[0]['Delitti']) * 100
    st.metric("Variazione 2014-2023", f"{variazione:.2f}%")
with col2:
    st.metric("Anno minimo", f"{df_totale.iloc[df_totale['Delitti'].idxmin()]['Anno']:.0f}")
with col3:
    st.metric("Anno massimo", f"{df_totale.iloc[df_totale['Delitti'].idxmax()]['Anno']:.0f}")

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