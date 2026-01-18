"""Grafico 2: Percezione vs Dati Registrati."""
import plotly.graph_objects as go
import streamlit as st
from config import COLORS, CHART_HEIGHT
from charts.base import add_covid_highlight, apply_base_layout


def render(df) -> None:
    """Renderizza grafico percezione vs dati con warning e metriche."""

    # Warning metodologico
    st.warning("""
    **Divario percezione-dati:**
    La percezione di insicurezza non è "sbagliata" - risponde a fattori legittimi come
    copertura mediatica, degrado urbano, sfiducia istituzionale ed esperienza personale.
    Questi dati mostrano che percezione e criminalità registrata seguono dinamiche diverse.
    """)

    # Expander dati
    with st.expander("Vedi dati percezione vs criminalità"):
        st.dataframe(df)

    # Costruzione dual-axis chart
    fig = go.Figure()

    # Serie 1: Percezione (asse Y sinistro)
    fig.add_trace(go.Scatter(
        x=df['Anno'],
        y=df['Percezione_pct'],
        mode='lines+markers',
        name='Percezione insicurezza (%)',
        line=dict(color=COLORS['secondary'], width=3),
        marker=dict(size=10),
        yaxis='y'
    ))

    # Serie 2: Tasso delitti (asse Y destro)
    fig.add_trace(go.Scatter(
        x=df['Anno'],
        y=df['Tasso_per_1000'],
        mode='lines+markers',
        name='Tasso delitti per 1000 ab.',
        line=dict(color=COLORS['primary'], width=3, dash='dash'),
        marker=dict(size=10),
        yaxis='y2'
    ))

    # Evidenzia periodo COVID
    add_covid_highlight(fig, position='top')

    # Layout dual-axis
    fig.update_layout(
        title='Gap tra Percezione di Insicurezza e Criminalità Registrata',
        xaxis_title='Anno',
        yaxis=dict(
            title='% Famiglie percepiscono rischio criminalità',
            titlefont=dict(color=COLORS['secondary']),
            tickfont=dict(color=COLORS['secondary']),
            side='left'
        ),
        yaxis2=dict(
            title='Tasso delitti per 1000 abitanti',
            titlefont=dict(color=COLORS['primary']),
            tickfont=dict(color=COLORS['primary']),
            overlaying='y',
            side='right'
        ),
        hovermode='x unified',
        template='plotly_white',
        height=CHART_HEIGHT,
        legend=dict(x=0.5, y=1.15, xanchor='center', orientation='h')
    )

    st.plotly_chart(fig, use_container_width=True)

    # Metriche
    _render_metrics(df)


def _render_metrics(df) -> None:
    """Renderizza metriche sotto il grafico."""
    col1, col2, col3 = st.columns(3)

    with col1:
        var_percezione = df.iloc[-1]['Percezione_pct'] - df.iloc[0]['Percezione_pct']
        st.metric("Δ Percezione 2014-2023", f"{var_percezione:.1f} punti %")
    with col2:
        var_tasso = df.iloc[-1]['Tasso_per_1000'] - df.iloc[0]['Tasso_per_1000']
        st.metric("Δ Tasso criminalità", f"{var_tasso:.1f} per 1000 ab.")
    with col3:
        anno_max_gap = df.loc[
            (df['Percezione_pct'] - df['Tasso_per_1000']).idxmax()
        ]['Anno']
        st.metric("Anno gap massimo", f"{anno_max_gap:.0f}")
