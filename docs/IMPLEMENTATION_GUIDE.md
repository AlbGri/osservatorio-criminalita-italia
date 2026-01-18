# Guida Implementativa - Istruzioni per AI Assistant

**Data**: 2026-01-18
**Contesto**: Questo documento contiene istruzioni operative dettagliate per implementare le prossime fasi del progetto. Per filosofia, principi e ragionamento strategico, riferirsi a `docs/roadmap.md`.

---

## Tempistiche Ricalibrate

Le stime originali in roadmap.md erano pre-AI assistance. Ecco la ricalibrazione basata su velocità effettiva:

| Fase | Stima Originale | Effettivo/Ricalibrato |
|------|-----------------|----------------------|
| Fase 0 | 30h | 8.5h (effettivo) |
| Fase 1 | 100-120h | 14h (effettivo) |
| Fase 1.5 | - | 3-5h (nuova) |
| Fase 2 | 80-100h | 15-25h |
| Fase 3 | 120-160h | 20-35h |

**Pattern scoperto**: ~4-6h per grafico completo end-to-end con AI assistance.

---

## Fase 1.5: Quick Wins (3-5h)

**Obiettivo**: Refactoring codebase per facilitare scaling Fase 2

### Sessione 1: Refactoring app.py (2-3h)

#### Step 1.1 - Creare struttura cartelle

```
src/
├── app.py                    # Entry point snello (~50 righe)
├── config.py                 # Costanti, colori, settings
├── data_loader.py            # Funzioni caricamento CSV
├── components/
│   ├── __init__.py
│   ├── header.py             # Titolo, intro
│   ├── footer.py             # Footer, disclaimer, link
│   └── warnings.py           # Box gialli riutilizzabili
├── charts/
│   ├── __init__.py
│   ├── base.py               # Funzioni comuni (es. highlight COVID)
│   ├── trend_nazionale.py    # Grafico 1
│   ├── percezione_vs_dati.py # Grafico 2
│   └── tipologie_reato.py    # Grafico 3
└── utils/
    ├── __init__.py
    └── formatting.py         # Formattazione numeri, percentuali
```

#### Step 1.2 - Creare config.py

```python
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
```

#### Step 1.3 - Creare data_loader.py

```python
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
```

#### Step 1.4 - Creare charts/base.py

```python
"""Funzioni comuni per tutti i grafici."""
import plotly.graph_objects as go
from config import COVID_PERIOD, TEMPLATE


def add_covid_highlight(fig: go.Figure, position: str = 'top') -> None:
    """Aggiunge evidenziazione periodo COVID al grafico."""
    fig.add_vrect(
        x0=COVID_PERIOD['start'],
        x1=COVID_PERIOD['end'],
        fillcolor=COVID_PERIOD['color'],
        layer='below',
        line_width=0,
        annotation_text=COVID_PERIOD['label'],
        annotation_position=position,
        annotation=dict(font_size=9, font_color='gray')
    )


def apply_base_layout(fig: go.Figure, title: str, height: int = 550) -> None:
    """Applica layout base comune a tutti i grafici."""
    fig.update_layout(
        title=title,
        hovermode='x unified',
        template=TEMPLATE,
        height=height
    )
```

#### Step 1.5 - Creare charts/trend_nazionale.py

```python
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
```

#### Step 1.6 - Creare charts/percezione_vs_dati.py

Estrarre da app.py attuale (righe 94-186) la logica del Grafico 2, seguendo stesso pattern di trend_nazionale.py:
- Funzione `render(df)` principale
- Funzione `_render_metrics(df)` privata
- Usa `add_covid_highlight()` e `apply_base_layout()` da base.py
- Colori da `config.COLORS`

#### Step 1.7 - Creare charts/tipologie_reato.py

Estrarre da app.py attuale (righe 190-347) la logica del Grafico 3:
- Funzione `render(df_categorie, df_allarme)` principale
- Due sotto-funzioni: `_render_categorie(df)` e `_render_allarme(df)`
- Gestisce layout 2 colonne internamente
- Colori da `config.COLORS`

#### Step 1.8 - Creare components/header.py

```python
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
```

#### Step 1.9 - Creare components/footer.py

```python
"""Footer della dashboard."""
import streamlit as st
from config import GITHUB_URL, METHODOLOGY_URL


def render() -> None:
    """Renderizza footer con warning finale e link."""

    # Box critico limiti strutturali
    st.warning(f"""
    **Limite strutturale dei dati italiani**

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
```

#### Step 1.10 - Creare components/warnings.py

```python
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
```

#### Step 1.11 - Creare __init__.py

Per `components/__init__.py`:
```python
from . import header, footer, warnings
```

Per `charts/__init__.py`:
```python
from . import base, trend_nazionale, percezione_vs_dati, tipologie_reato
```

Per `utils/__init__.py`:
```python
# Vuoto per ora
```

#### Step 1.12 - Riscrivere app.py

```python
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
```

#### Step 1.13 - Verificare funzionamento

```bash
cd c:\Alberto\Coding\osservatorio_criminalita_italia
streamlit run src/app.py
```

La dashboard deve funzionare **identica** a prima del refactoring.

---

### Sessione 2: Dev Tools (30min-1h)

#### Step 2.1 - Creare requirements-dev.txt

```
# Development dependencies
black==24.1.0
isort==5.13.0
flake8==7.0.0
pre-commit==3.6.0
pytest==8.0.0
```

#### Step 2.2 - Creare .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.0
    hooks:
      - id: black
        language_version: python3.11

  - repo: https://github.com/pycqa/isort
    rev: 5.13.0
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: ["--max-line-length", "100", "--ignore", "E501,W503"]
```

#### Step 2.3 - Creare pyproject.toml

```toml
[tool.black]
line-length = 100
target-version = ['py311']

[tool.isort]
profile = "black"
line_length = 100
```

---

### Sessione 3: README (30min)

#### Step 3.1 - Aggiungere badge a README.md (inizio file)

```markdown
![Python](https://img.shields.io/badge/python-3.11-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.41.1-FF4B4B)
![License](https://img.shields.io/badge/license-MIT-green)
![Deploy](https://img.shields.io/badge/deploy-Streamlit%20Cloud-FF4B4B)
```

#### Step 3.2 - Aggiungere sezione struttura

Dopo sezione "Documentazione":

```markdown
## Struttura Progetto

```
osservatorio-criminalita-italia/
├── src/
│   ├── app.py              # Entry point dashboard
│   ├── config.py           # Configurazione centralizzata
│   ├── data_loader.py      # Caricamento dati
│   ├── components/         # Componenti UI riutilizzabili
│   └── charts/             # Moduli grafici
├── data/
│   ├── raw/                # Dati ISTAT originali
│   └── processed/          # Dati elaborati per dashboard
├── notebooks/              # Analisi esplorative
├── docs/                   # Documentazione
└── tests/                  # Test (futuro)
```
```

---

## Fase 2: Espansione Territoriale

### Prerequisiti (da fare manualmente)

Scaricare da dati.istat.it:

1. **Delitti per regione** (2014-2023)
   - Percorso: Giustizia e sicurezza → Delitti denunciati
   - Filtro: Territorio = Regioni
   - Salvare: `data/raw/regionali/delitti_regionali_2014_2023.csv`

2. **Delitti per provincia** (2014-2023)
   - Stesso percorso, filtro Province
   - Salvare: `data/raw/provinciali/delitti_provinciali_2014_2023.csv`

3. **Popolazione regionale/provinciale** (2014-2023)
   - Da demo.istat.it
   - Salvare: `data/raw/popolazione/`

4. **GeoJSON Italia**
   - ISTAT confini amministrativi
   - Salvare: `data/geo/regioni.geojson` e `data/geo/province.geojson`

### Grafici da implementare

| Grafico | Stima | File da creare |
|---------|-------|----------------|
| Numero Oscuro | 3-4h | `charts/numero_oscuro.py` |
| Mappa Regioni | 5-6h | `charts/mappa_regionale.py` |
| Tabella Province | 4-5h | `charts/tabella_province.py` |

### Notebook elaborazione

Creare `notebooks/02_analisi_territoriale.ipynb`:
- Pulizia dati regionali/provinciali
- Normalizzazione per popolazione
- Export in `data/processed/`

---

## Checkpoint

### Fase 1.5 Completata quando:
- [ ] Struttura cartelle src/ creata
- [ ] config.py funzionante
- [ ] data_loader.py funzionante
- [ ] charts/ con 3 moduli separati
- [ ] components/ con header, footer, warnings
- [ ] app.py snello (~50 righe)
- [ ] Dashboard funziona identica a prima
- [ ] requirements-dev.txt creato
- [ ] .pre-commit-config.yaml creato
- [ ] README aggiornato

### Fase 2 Completata quando:
- [ ] Dati territoriali scaricati
- [ ] Notebook 02 con elaborazione
- [ ] 3 nuovi grafici implementati
- [ ] Metodologia aggiornata
- [ ] Dashboard con 6 grafici
- [ ] Deploy aggiornato

---

## Come usare questo documento

**Per Sonnet - Fase 1.5 Sessione 1:**
> "Leggi docs/IMPLEMENTATION_GUIDE.md e implementa la Sessione 1 del refactoring, creando tutti i file descritti negli step 1.1-1.13"

**Per Sonnet - Fase 1.5 Sessione 2:**
> "Leggi docs/IMPLEMENTATION_GUIDE.md sezione Sessione 2 e crea i file dev tools"

**Per Sonnet - Fase 2:**
> "Ho scaricato i dati ISTAT. Leggi docs/IMPLEMENTATION_GUIDE.md sezione Fase 2 e procedi"
