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
st.subheader("Dashboard MVP")

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

# Sezione Grafico 2: Percezione vs Dati Registrati
st.header("Percezione della Sicurezza vs Criminalità Registrata (2014-2023)")

# Box giallo avviso
st.warning("""
**Divario percezione-dati:**  
La percezione di insicurezza non è "sbagliata" - risponde a fattori legittimi come 
copertura mediatica, degrado urbano, sfiducia istituzionale ed esperienza personale.  
Questi dati mostrano che percezione e criminalità registrata seguono dinamiche diverse.
""")

# Carica dati combinati
df_percezione_vs_dati = pd.read_csv('data/processed/percezione_vs_dati_2014_2023.csv')

# Mostra dati
with st.expander("Vedi dati percezione vs criminalità"):
    st.dataframe(df_percezione_vs_dati)

# DUAL-AXIS CHART con Plotly
fig_dual = go.Figure()

# Serie 1: Percezione (asse Y sinistro)
fig_dual.add_trace(go.Scatter(
    x=df_percezione_vs_dati['Anno'],
    y=df_percezione_vs_dati['Percezione_pct'],
    mode='lines+markers',
    name='Percezione insicurezza (%)',
    line=dict(color='#E63946', width=3),
    marker=dict(size=10),
    yaxis='y'
))

# Serie 2: Tasso delitti (asse Y destro)
fig_dual.add_trace(go.Scatter(
    x=df_percezione_vs_dati['Anno'],
    y=df_percezione_vs_dati['Tasso_per_1000'],
    mode='lines+markers',
    name='Tasso delitti per 1000 ab.',
    line=dict(color='#2E86AB', width=3, dash='dash'),
    marker=dict(size=10),
    yaxis='y2'
))

# Evidenzia periodo COVID
fig_dual.add_vrect(
    x0=2019.5, x1=2021.5,
    fillcolor='rgba(200, 200, 200, 0.2)',
    layer='below',
    line_width=0,
    annotation_text='COVID-19',
    annotation_position='top',
    annotation=dict(font_size=9, font_color='gray')
)

# Layout dual-axis
fig_dual.update_layout(
    title='Gap tra Percezione di Insicurezza e Criminalità Registrata',
    xaxis_title='Anno',
    yaxis=dict(
        title='% Famiglie percepiscono rischio criminalità',
        titlefont=dict(color='#E63946'),
        tickfont=dict(color='#E63946'),
        side='left'
    ),
    yaxis2=dict(
        title='Tasso delitti per 1000 abitanti',
        titlefont=dict(color='#2E86AB'),
        tickfont=dict(color='#2E86AB'),
        overlaying='y',
        side='right'
    ),
    hovermode='x unified',
    template='plotly_white',
    height=550,
    legend=dict(x=0.5, y=1.15, xanchor='center', orientation='h')
)

st.plotly_chart(fig_dual, use_container_width=True)

# Insight chiave
col1, col2, col3 = st.columns(3)
with col1:
    var_percezione = df_percezione_vs_dati.iloc[-1]['Percezione_pct'] - df_percezione_vs_dati.iloc[0]['Percezione_pct']
    st.metric("Δ Percezione 2014-2023", f"{var_percezione:.1f} punti %")
with col2:
    var_tasso = df_percezione_vs_dati.iloc[-1]['Tasso_per_1000'] - df_percezione_vs_dati.iloc[0]['Tasso_per_1000']
    st.metric("Δ Tasso criminalità", f"{var_tasso:.1f} per 1000 ab.")
with col3:
    anno_max_gap = df_percezione_vs_dati.loc[
        (df_percezione_vs_dati['Percezione_pct'] - 
         df_percezione_vs_dati['Tasso_per_1000']).idxmax()
    ]['Anno']
    st.metric("Anno gap massimo", f"{anno_max_gap:.0f}")

st.divider()

# Sezione Grafico 3: Tipologie Reato nel Tempo
st.header("Evoluzione Tipologie di Reato (2014-2023)")

# Box giallo avviso
st.warning("""
**Dinamiche diverse per tipologia:**  
Aumenti in specifiche categorie (es. truffe online) possono riflettere cambiamenti sociali 
e tecnologici senza indicare più criminalità complessiva. Le categorie riflettono 
classificazioni penali, non la percezione comune del reato.
""")

# Layout a 2 colonne
col_left, col_right = st.columns(2)

# --- COLONNA SINISTRA: Tutte le categorie ---
with col_left:
    st.subheader("Quadro Generale per Categoria")
    
    # Carica dati categorie
    df_categorie_norm = pd.read_csv('data/processed/delitti_categorie_normalizzato_2014_2023.csv')
    
    with st.expander("Vedi dati categorie"):
        st.dataframe(df_categorie_norm, height=200)
    
    # LINE CHART categorie
    fig_categorie = go.Figure()
    
    categorie_list = df_categorie_norm['Categoria'].unique()
    colori = {
        'Furti': '#1f77b4',                    # Blu standard
        'Violenze contro la persona': '#d62728',  # Rosso vivo
        'Truffe e Frodi': '#ff7f0e',          # Arancione
        'Rapine': '#8B4513',                   # Marrone (non rosso!)
        'Droga': '#9467bd',                    # Viola
        'Altro': '#7f7f7f'                     # Grigio
    }
    
    for categoria in categorie_list:
        df_cat = df_categorie_norm[df_categorie_norm['Categoria'] == categoria]
        fig_categorie.add_trace(go.Scatter(
            x=df_cat['Anno'],
            y=df_cat['Tasso_per_1000'],
            mode='lines+markers',
            name=categoria,
            line=dict(width=2.5, color=colori.get(categoria, '#999999')),
            marker=dict(size=6)
        ))
    
    # Evidenzia periodo COVID
    fig_categorie.add_vrect(
        x0=2019.5, x1=2021.5,
        fillcolor='rgba(200, 200, 200, 0.2)',
        layer='below',
        line_width=0,
        annotation_text='COVID-19',
        annotation_position='top',
        annotation=dict(font_size=9, font_color='gray')
    )
    
    fig_categorie.update_layout(
        title='Tasso per 1000 abitanti',
        xaxis_title='Anno',
        yaxis_title='Tasso per 1000 ab.',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        legend=dict(x=0, y=-0.2, xanchor='left', orientation='h'),
        margin=dict(l=20, r=20, t=40, b=80)
    )
    
    st.plotly_chart(fig_categorie, use_container_width=True)
    
    # Metriche categorie
    st.caption("**Variazioni 2014-2023**")
    furti_2014 = df_categorie_norm[(df_categorie_norm['Anno']==2014) & (df_categorie_norm['Categoria']=='Furti')]['Tasso_per_1000'].values[0]
    furti_2023 = df_categorie_norm[(df_categorie_norm['Anno']==2023) & (df_categorie_norm['Categoria']=='Furti')]['Tasso_per_1000'].values[0]
    var_furti = ((furti_2023 - furti_2014) / furti_2014) * 100
    
    truffe_2014 = df_categorie_norm[(df_categorie_norm['Anno']==2014) & (df_categorie_norm['Categoria']=='Truffe e Frodi')]['Tasso_per_1000'].values[0]
    truffe_2023 = df_categorie_norm[(df_categorie_norm['Anno']==2023) & (df_categorie_norm['Categoria']=='Truffe e Frodi')]['Tasso_per_1000'].values[0]
    var_truffe = ((truffe_2023 - truffe_2014) / truffe_2014) * 100
    
    st.markdown(f"Furti: {var_furti:.1f}% | Truffe: {var_truffe:.1f}%")

# --- COLONNA DESTRA: Reati alto allarme sociale ---
with col_right:
    st.subheader("Reati ad Alto Impatto Mediatico")
    
    st.info("""
    **Focus su reati rari ma ad alto allarme sociale.**  
    Rappresentano <2% dei delitti totali ma dominano percezione pubblica e copertura mediatica.
    """)
    
    # Carica dati allarme
    df_allarme_norm = pd.read_csv('data/processed/reati_allarme_sociale_2014_2023.csv')
    
    with st.expander("Vedi dati reati allarme"):
        st.dataframe(df_allarme_norm, height=200)
    
    # LINE CHART reati allarme
    fig_allarme = go.Figure()
    
    reati_list = df_allarme_norm['Reato'].unique()
    colori_allarme = {
        'Omicidi volontari consumati': '#d62728',      # Rosso vivo
        'Tentati omicidi': '#ff7f0e',                  # Arancione
        'Violenze sessuali': '#8B008B',                # Viola scuro (dominante)
        'Atti sessuali con minorenne': '#e377c2',      # Rosa
        'Rapine in abitazione': '#bcbd22',             # Giallo-verde
        'Sequestri di persona': '#17becf'              # Cyan
    }
    
    for reato in reati_list:
        df_reato = df_allarme_norm[df_allarme_norm['Reato'] == reato]
        fig_allarme.add_trace(go.Scatter(
            x=df_reato['Anno'],
            y=df_reato['Tasso_per_100k'],
            mode='lines+markers',
            name=reato,
            line=dict(width=2.5, color=colori_allarme.get(reato, '#999999')),
            marker=dict(size=6)
        ))
    
    # Evidenzia periodo COVID
    fig_allarme.add_vrect(
        x0=2019.5, x1=2021.5,
        fillcolor='rgba(200, 200, 200, 0.2)',
        layer='below',
        line_width=0,
        annotation_text='COVID-19',
        annotation_position='top',
        annotation=dict(font_size=9, font_color='gray')
    )
    
    fig_allarme.update_layout(
        title='Tasso per 100k abitanti',
        xaxis_title='Anno',
        yaxis_title='Tasso per 100k ab.',
        hovermode='x unified',
        template='plotly_white',
        height=500,
        legend=dict(x=0, y=-0.2, xanchor='left', orientation='h'),
        margin=dict(l=20, r=20, t=40, b=80)
    )
    
    st.plotly_chart(fig_allarme, use_container_width=True)
    
    # Metriche allarme
    st.caption("**Variazioni 2014-2023**")
    omicidi_2014 = df_allarme_norm[(df_allarme_norm['Anno']==2014) & (df_allarme_norm['Reato']=='Omicidi volontari consumati')]['Tasso_per_100k'].values[0]
    omicidi_2023 = df_allarme_norm[(df_allarme_norm['Anno']==2023) & (df_allarme_norm['Reato']=='Omicidi volontari consumati')]['Tasso_per_100k'].values[0]
    var_omicidi = ((omicidi_2023 - omicidi_2014) / omicidi_2014) * 100
    
    violenze_2014 = df_allarme_norm[(df_allarme_norm['Anno']==2014) & (df_allarme_norm['Reato']=='Violenze sessuali')]['Tasso_per_100k'].values[0]
    violenze_2023 = df_allarme_norm[(df_allarme_norm['Anno']==2023) & (df_allarme_norm['Reato']=='Violenze sessuali')]['Tasso_per_100k'].values[0]
    var_violenze = ((violenze_2023 - violenze_2014) / violenze_2014) * 100
    
    st.markdown(f"Omicidi: {var_omicidi:.1f}% | Violenze sessuali: {var_violenze:.1f}%")

st.divider()

# Footer
st.caption("Fase 1 MVP Completata | Repository: [GitHub](https://github.com/AlbGri/osservatorio-criminalita-italia)")