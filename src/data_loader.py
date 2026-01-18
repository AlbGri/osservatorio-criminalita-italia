"""Funzioni per caricamento dati."""
import pandas as pd
from config import DATA_PATHS


def load_delitti_normalizzati() -> pd.DataFrame:
    """Carica dati delitti normalizzati per 1000 abitanti."""
    return pd.read_csv(DATA_PATHS['delitti_normalizzati'])


def load_percezione_vs_dati() -> pd.DataFrame:
    """Carica dati percezione vs criminalità registrata."""
    return pd.read_csv(DATA_PATHS['percezione_vs_dati'])


def load_categorie() -> pd.DataFrame:
    """Carica dati categorie reato normalizzati."""
    return pd.read_csv(DATA_PATHS['categorie'])


def load_allarme_sociale() -> pd.DataFrame:
    """Carica dati reati alto allarme sociale."""
    return pd.read_csv(DATA_PATHS['allarme_sociale'])
