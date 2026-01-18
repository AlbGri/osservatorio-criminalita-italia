"""Box warning riutilizzabili."""
import streamlit as st


def metodologia_denunce() -> None:
    """Warning standard su denunce vs crimini."""
    st.warning("""
    **Nota metodologica importante:**
    Questi dati mostrano **denunce registrate**, non crimini effettivamente commessi.
    """)


def percezione_vs_dati() -> None:
    """Warning su divario percezione-dati."""
    st.warning("""
    **Divario percezione-dati:**
    La percezione di insicurezza non è "sbagliata" - risponde a fattori legittimi come
    copertura mediatica, degrado urbano, sfiducia istituzionale ed esperienza personale.
    """)


def tipologie_reato() -> None:
    """Warning su dinamiche diverse per tipologia."""
    st.warning("""
    **Dinamiche diverse per tipologia:**
    Aumenti in specifiche categorie (es. truffe online) possono riflettere cambiamenti sociali
    e tecnologici senza indicare più criminalità complessiva.
    """)
