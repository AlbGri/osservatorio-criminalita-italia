"""Header della dashboard."""
import streamlit as st
from config import PROJECT_TITLE


def render() -> None:
    """Renderizza header e intro."""
    st.title(PROJECT_TITLE)
    st.subheader("Dashboard MVP")
    st.divider()

    st.header("Progetto")
    st.write("""
    Questo è un progetto di visualizzazione dati sulla criminalità in Italia
    basato su fonti ufficiali (ISTAT, Ministero dell'Interno).
    """)
