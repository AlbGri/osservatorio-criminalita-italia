"""Configurazione centralizzata per l'app."""

# Colori grafici - palette accessibile
COLORS = {
    # Primari
    'primary': '#2E86AB',
    'secondary': '#E63946',

    # Categorie reato
    'furti': '#1f77b4',
    'violenze': '#d62728',
    'truffe': '#ff7f0e',
    'rapine': '#8B4513',
    'droga': '#9467bd',
    'altro': '#7f7f7f',

    # Reati allarme sociale
    'omicidi': '#d62728',
    'tentati_omicidi': '#ff7f0e',
    'violenze_sessuali': '#8B008B',
    'atti_minori': '#e377c2',
    'rapine_abitazione': '#bcbd22',
    'sequestri': '#17becf',
}

# Periodi speciali da evidenziare
COVID_PERIOD = {
    'start': 2019.5,
    'end': 2021.5,
    'color': 'rgba(200, 200, 200, 0.2)',
    'label': 'COVID-19'
}

# Layout grafici
CHART_HEIGHT = 550
CHART_HEIGHT_SMALL = 500
TEMPLATE = 'plotly_white'

# Percorsi dati
DATA_PATHS = {
    'delitti_normalizzati': 'data/processed/delitti_italia_normalizzato_2014_2023.csv',
    'percezione_vs_dati': 'data/processed/percezione_vs_dati_2014_2023.csv',
    'categorie': 'data/processed/delitti_categorie_normalizzato_2014_2023.csv',
    'allarme_sociale': 'data/processed/reati_allarme_sociale_2014_2023.csv',
}

# Metadati progetto
PROJECT_TITLE = "Osservatorio Criminalità Italia"
GITHUB_URL = "https://github.com/AlbGri/osservatorio-criminalita-italia"
METHODOLOGY_URL = f"{GITHUB_URL}/blob/main/docs/methodology.md"
