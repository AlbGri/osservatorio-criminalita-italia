"""Osservatorio Criminalità Italia - Dashboard MVP."""
import streamlit as st

# Aggiungi src al path per import
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from config import PROJECT_TITLE
from data_loader import (
    load_delitti_normalizzati,
    load_percezione_vs_dati,
    load_categorie,
    load_allarme_sociale
)
from charts import trend_nazionale, percezione_vs_dati, tipologie_reato
from components import header, footer

# Configurazione pagina
st.set_page_config(
    page_title=PROJECT_TITLE,
    layout="wide"
)

# Header
header.render()

# Grafico 1: Trend nazionale
st.header("Trend Delitti Denunciati in Italia (2014-2023)")
trend_nazionale.render(load_delitti_normalizzati())
st.divider()

# Grafico 2: Percezione vs Dati
st.header("Percezione della Sicurezza vs Criminalità Registrata (2014-2023)")
percezione_vs_dati.render(load_percezione_vs_dati())
st.divider()

# Grafico 3: Tipologie reato
st.header("Evoluzione Tipologie di Reato (2014-2023)")
tipologie_reato.render(load_categorie(), load_allarme_sociale())
st.divider()

# Footer
footer.render()
