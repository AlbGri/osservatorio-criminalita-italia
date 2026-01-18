"""Grafico 3: Tipologie di Reato nel Tempo."""
import plotly.graph_objects as go
import streamlit as st
from config import COLORS, CHART_HEIGHT_SMALL
from charts.base import add_covid_highlight


def render(df_categorie, df_allarme) -> None:
    """Renderizza grafici tipologie reato con layout a 2 colonne."""

    # Warning metodologico
    st.warning("""
    **Dinamiche diverse per tipologia:**
    Aumenti in specifiche categorie (es. truffe online) possono riflettere cambiamenti sociali
    e tecnologici senza indicare più criminalità complessiva. Le categorie riflettono
    classificazioni penali, non la percezione comune del reato.
    """)

    # Layout a 2 colonne
    col_left, col_right = st.columns(2)

    # Colonna sinistra: Categorie generali
    with col_left:
        _render_categorie(df_categorie)

    # Colonna destra: Reati allarme sociale
    with col_right:
        _render_allarme(df_allarme)


def _render_categorie(df_categorie) -> None:
    """Renderizza grafico categorie generali."""
    st.subheader("Quadro Generale per Categoria")

    with st.expander("Vedi dati categorie"):
        st.dataframe(df_categorie, height=200)

    # Costruzione grafico
    fig = go.Figure()

    categorie_list = df_categorie['Categoria'].unique()
    colori_categorie = {
        'Furti': COLORS['furti'],
        'Violenze contro la persona': COLORS['violenze'],
        'Truffe e Frodi': COLORS['truffe'],
        'Rapine': COLORS['rapine'],
        'Droga': COLORS['droga'],
        'Altro': COLORS['altro']
    }

    for categoria in categorie_list:
        df_cat = df_categorie[df_categorie['Categoria'] == categoria]
        fig.add_trace(go.Scatter(
            x=df_cat['Anno'],
            y=df_cat['Tasso_per_1000'],
            mode='lines+markers',
            name=categoria,
            line=dict(width=2.5, color=colori_categorie.get(categoria, '#999999')),
            marker=dict(size=6)
        ))

    # Evidenzia periodo COVID
    add_covid_highlight(fig, position='top')

    fig.update_layout(
        title='Tasso per 1000 abitanti',
        xaxis_title='Anno',
        yaxis_title='Tasso per 1000 ab.',
        hovermode='x unified',
        template='plotly_white',
        height=CHART_HEIGHT_SMALL,
        legend=dict(x=0, y=-0.2, xanchor='left', orientation='h'),
        margin=dict(l=20, r=20, t=40, b=80)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Metriche
    _render_metrics_categorie(df_categorie)


def _render_allarme(df_allarme) -> None:
    """Renderizza grafico reati allarme sociale."""
    st.subheader("Reati ad Alto Impatto Mediatico")

    st.info("""
    **Focus su reati rari ma ad alto allarme sociale.**
    Rappresentano <2% dei delitti totali ma dominano percezione pubblica e copertura mediatica.
    """)

    with st.expander("Vedi dati reati allarme"):
        st.dataframe(df_allarme, height=200)

    # Costruzione grafico
    fig = go.Figure()

    reati_list = df_allarme['Reato'].unique()
    colori_allarme = {
        'Omicidi volontari consumati': COLORS['omicidi'],
        'Tentati omicidi': COLORS['tentati_omicidi'],
        'Violenze sessuali': COLORS['violenze_sessuali'],
        'Atti sessuali con minorenne': COLORS['atti_minori'],
        'Rapine in abitazione': COLORS['rapine_abitazione'],
        'Sequestri di persona': COLORS['sequestri']
    }

    for reato in reati_list:
        df_reato = df_allarme[df_allarme['Reato'] == reato]
        fig.add_trace(go.Scatter(
            x=df_reato['Anno'],
            y=df_reato['Tasso_per_100k'],
            mode='lines+markers',
            name=reato,
            line=dict(width=2.5, color=colori_allarme.get(reato, '#999999')),
            marker=dict(size=6)
        ))

    # Evidenzia periodo COVID
    add_covid_highlight(fig, position='top')

    fig.update_layout(
        title='Tasso per 100k abitanti',
        xaxis_title='Anno',
        yaxis_title='Tasso per 100k ab.',
        hovermode='x unified',
        template='plotly_white',
        height=CHART_HEIGHT_SMALL,
        legend=dict(x=0, y=-0.2, xanchor='left', orientation='h'),
        margin=dict(l=20, r=20, t=40, b=80)
    )

    st.plotly_chart(fig, use_container_width=True)

    # Metriche
    _render_metrics_allarme(df_allarme)


def _render_metrics_categorie(df) -> None:
    """Renderizza metriche categorie."""
    st.caption("**Variazioni 2014-2023**")

    furti_2014 = df[(df['Anno'] == 2014) & (df['Categoria'] == 'Furti')]['Tasso_per_1000'].values[0]
    furti_2023 = df[(df['Anno'] == 2023) & (df['Categoria'] == 'Furti')]['Tasso_per_1000'].values[0]
    var_furti = ((furti_2023 - furti_2014) / furti_2014) * 100

    truffe_2014 = df[(df['Anno'] == 2014) & (df['Categoria'] == 'Truffe e Frodi')]['Tasso_per_1000'].values[0]
    truffe_2023 = df[(df['Anno'] == 2023) & (df['Categoria'] == 'Truffe e Frodi')]['Tasso_per_1000'].values[0]
    var_truffe = ((truffe_2023 - truffe_2014) / truffe_2014) * 100

    st.markdown(f"Furti: {var_furti:.1f}% | Truffe: {var_truffe:.1f}%")


def _render_metrics_allarme(df) -> None:
    """Renderizza metriche reati allarme."""
    st.caption("**Variazioni 2014-2023**")

    omicidi_2014 = df[(df['Anno'] == 2014) & (df['Reato'] == 'Omicidi volontari consumati')]['Tasso_per_100k'].values[0]
    omicidi_2023 = df[(df['Anno'] == 2023) & (df['Reato'] == 'Omicidi volontari consumati')]['Tasso_per_100k'].values[0]
    var_omicidi = ((omicidi_2023 - omicidi_2014) / omicidi_2014) * 100

    violenze_2014 = df[(df['Anno'] == 2014) & (df['Reato'] == 'Violenze sessuali')]['Tasso_per_100k'].values[0]
    violenze_2023 = df[(df['Anno'] == 2023) & (df['Reato'] == 'Violenze sessuali')]['Tasso_per_100k'].values[0]
    var_violenze = ((violenze_2023 - violenze_2014) / violenze_2014) * 100

    st.markdown(f"Omicidi: {var_omicidi:.1f}% | Violenze sessuali: {var_violenze:.1f}%")
