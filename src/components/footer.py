"""Footer della dashboard."""
import streamlit as st
from config import GITHUB_URL, METHODOLOGY_URL


def render() -> None:
    """Renderizza footer con warning finale e link."""

    # Box critico limiti strutturali
    st.warning(f"""
    ⚠️ **Limite strutturale dei dati italiani**

    Questo progetto usa solo denunce perché l'Italia, a differenza di UK/USA/Germania,
    non pubblica:
    - Indagini vittimizzazione annuali (UK: 35k famiglie/anno dal 1982)
    - Dati sanitari aggregati su violenze (già raccolti ma non pubblici)
    - Esiti processuali linkabili alle denunce

    **Non è limite tecnico: è scelta politica.**

    Dettagli completi in [Metodologia]({METHODOLOGY_URL}#limiti-strutturali-cosa-litalia-potrebbe-misurare-ma-non-fa)
    """)

    # Footer
    st.caption(f"Fase 1 MVP Completata | Repository: [GitHub]({GITHUB_URL})")
