"""Grafico 1: Trend nazionale criminalità."""
import plotly.graph_objects as go
import streamlit as st
from config import COLORS, CHART_HEIGHT
from charts.base import add_covid_highlight, apply_base_layout


def render(df) -> None:
    """Renderizza grafico trend nazionale con warning e metriche."""

    # Warning metodologico
    st.warning("""
    **Nota metodologica importante:**
    Questi dati mostrano **denunce registrate**, non crimini effettivamente commessi.
    Alcuni reati hanno bassa propensione alla denuncia (es. violenze domestiche),
    altri alta (es. furti auto assicurati). Il grafico riflette sia la criminalità reale
    che la propensione a denunciare e l'efficienza delle forze dell'ordine.
    """)

    # Expander dati
    with st.expander("Vedi dati"):
        st.dataframe(df)

    # Costruzione grafico
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df['Anno'],
        y=df['Tasso_per_1000'],
        mode='lines+markers',
        name='Tasso delitti per 1000 abitanti',
        line=dict(color=COLORS['primary'], width=3),
        marker=dict(size=10)
    ))

    add_covid_highlight(fig, position='top left')
    apply_base_layout(
        fig,
        'Tasso Delitti Denunciati per 1000 Abitanti - Italia (2014-2023)',
        CHART_HEIGHT
    )

    fig.update_layout(
        xaxis_title='Anno',
        yaxis_title='Delitti per 1000 Abitanti'
    )

    st.plotly_chart(fig, use_container_width=True)

    # Metriche
    _render_metrics(df)


def _render_metrics(df) -> None:
    """Renderizza metriche sotto il grafico."""
    col1, col2, col3 = st.columns(3)

    variazione = ((df.iloc[-1]['Tasso_per_1000'] - df.iloc[0]['Tasso_per_1000'])
                  / df.iloc[0]['Tasso_per_1000']) * 100

    with col1:
        st.metric("Variazione tasso 2014-2023", f"{variazione:.2f}%")
    with col2:
        st.metric("Anno minimo", f"{df.iloc[df['Tasso_per_1000'].idxmin()]['Anno']:.0f}")
    with col3:
        st.metric("Anno massimo", f"{df.iloc[df['Tasso_per_1000'].idxmax()]['Anno']:.0f}")
