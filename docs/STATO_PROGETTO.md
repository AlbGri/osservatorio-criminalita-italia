# Stato Progetto - Ultimo aggiornamento: 2026-01-08

## Fase Corrente
**Fase 1: MVP Dashboard Base - COMPLETATA ✓**

## Completato

### Fase 0: Validazione Fattibilità (COMPLETATA)
- [x] Setup ambiente sviluppo (VS Code, Miniconda, Git)
- [x] Creato environment `osservatorio` (Python 3.11)
- [x] Configurato repository GitHub
- [x] Installato librerie base (streamlit, plotly, pandas, numpy, jupyter)
- [x] Struttura cartelle progetto creata
- [x] Documentazione setup Windows
- [x] Tutorial Streamlit - app.py base funzionante
- [x] Tutorial Plotly - line chart e bar chart integrati
- [x] Esplorazione portale dati.istat.it
- [x] Download manuale CSV ISTAT Delitti 2014-2023 (18MB)
- [x] Pulizia dati con pandas in Jupyter notebook
- [x] Primo grafico Plotly con dati reali
- [x] Integrazione dati reali in app Streamlit
- [x] App funzionante con grafico trend nazionale 2014-2023
- [x] Dataset pulito salvato in data/processed/
- [x] Rimozione file privati da GitHub
- [x] Deploy Streamlit Cloud (criminalita-italia.streamlit.app)
- [x] Documentazione methodology.md (380 parole)
- [x] Decisione GO/NO-GO: GO Fase 1

### Fase 1: MVP Dashboard Base (COMPLETATA ✓)
- [x] Grafico 1: Trend nazionale normalizzato
  - [x] Download dati popolazione ISTAT (ricostruzione 2002-2019 + POSAS 2020-2023)
  - [x] Integrazione popolazione nel notebook
  - [x] Calcolo tasso per 1000 abitanti
  - [x] Dataset normalizzato salvato
  - [x] Aggiornamento app.py con tasso normalizzato
  - [x] Box giallo warning limiti dati
  - [x] Evidenziazione periodo COVID 2020-2021
  - [x] Deploy online aggiornato

- [x] Grafico 2: Percezione vs Dati
  - [x] Esplorazione portale ISTAT per dati percezione
  - [x] Download CSV "Altri problemi" (percezione rischio criminalità 2014-2023)
  - [x] Pulizia dati percezione in notebook
  - [x] Merge percezione + delitti normalizzati
  - [x] Dataset combinato salvato (percezione_vs_dati_2014_2023.csv)
  - [x] Implementazione dual-axis chart in app.py
  - [x] Box giallo avviso divario percezione-dati
  - [x] Evidenziazione periodo COVID
  - [x] Metriche chiave (delta percezione, delta tasso, anno gap massimo)
  - [x] Deploy online aggiornato

- [x] Grafico 3: Tipologie reato nel tempo
  - [x] Esplorazione 56 tipologie dettaglio dataset ISTAT
  - [x] Definizione schema aggregazione (6 macro-categorie)
  - [x] Implementazione categorizzazione automatica
  - [x] Aggregazione per anno e categoria
  - [x] Normalizzazione per popolazione
  - [x] Dataset categorie salvato (delitti_categorie_normalizzato_2014_2023.csv)
  - [x] Identificazione reati "alto allarme sociale" (6 tipologie dettaglio)
  - [x] Dataset reati allarme salvato (reati_allarme_sociale_2014_2023.csv)
  - [x] Layout a 2 colonne (generale + focus mediatico)
  - [x] Implementazione grafici con colori distinti per categoria
  - [x] Box info reati rari ma alto impatto
  - [x] Metriche variazioni furti/truffe e omicidi/violenze sessuali
  - [x] Pulizia layout (rimozione emoji, header aggiornato, footer unico)
  - [x] Deploy online aggiornato

## Prossimi step
**Fase 2: Dashboard Avanzata** (opzionale, da decidere)
- Visualizzazioni regionali con mappe interattive
- Filtri dinamici per territorio e periodo
- Confronti internazionali (Eurostat)
- Sezione "Numero Oscuro" con infografiche

**Prima di Fase 2:**
- Aggiornamento methodology.md (sezione percezione + categorie reati)
- Eventuale refactoring codice (modularizzazione)
- Raccolta feedback utenti reali

## Problemi aperti
Nessuno

## Note tecniche
- Environment: `osservatorio` (Python 3.11)
- Librerie: streamlit 1.41.1, plotly 5.24.1, pandas 2.2.3, numpy 2.2.1, jupyter 1.1.1
- Repository: https://github.com/AlbGri/osservatorio-criminalita-italia
- Deploy: https://criminalita-italia.streamlit.app
- Dataset raw:
  - delitti_2014_2023_istat.csv (18MB, 74.236 righe, 56 tipologie)
  - percezione_criminalita_2014_2023_istat.csv (10 righe)
  - popolazione ISTAT: ricostruzione 2002-2019 + POSAS 2020-2023
- Dataset processati:
  - delitti_totale_italia_2014_2023.csv (10 righe)
  - delitti_italia_normalizzato_2014_2023.csv (10 righe, tasso per 1000 abitanti)
  - percezione_vs_dati_2014_2023.csv (10 righe, percezione + tasso + popolazione)
  - delitti_categorie_normalizzato_2014_2023.csv (60 righe, 6 categorie x 10 anni)
  - reati_allarme_sociale_2014_2023.csv (60 righe, 6 reati x 10 anni, tasso per 100k)

## Ore dedicate
Giorno 1 (2026-01-05): ~2.5 ore
Giorno 2 (2026-01-06): ~10 ore
Giorno 3 (2026-01-08): ~4 ore
Giorno 4 (2026-01-08): ~6 ore

**Totale progetto: ~22.5 ore**
- Fase 0: ~8.5 ore (30 previste, -72%)
- Fase 1: ~14 ore (100-120 previste, -86%)

## Retrospettiva stime

**Fase 1 completata in 14 ore vs 100-120 previste**
- Grafico 1: ~4 ore
- Grafico 2: ~4 ore  
- Grafico 3: ~6 ore

**Velocità mantenuta:** ~4-6 ore per grafico completo end-to-end

**Lezioni apprese:**
- Pattern ripetibile: esplorazione → pulizia → aggregazione → implementazione → deploy
- Decisioni design richiedono discussione iterativa (+30-45 min)
- Git workflow e deploy ormai automatizzati (<10 min)

## Milestone: MVP Dashboard Funzionante ✓
- [x] Dashboard online con 3 grafici interattivi
- [x] Dati ufficiali ISTAT 2014-2023
- [x] Normalizzazione popolazione corretta
- [x] Percezione vs realtà visualizzata
- [x] Focus reati mediatici vs trend generale
- [x] Metodologia trasparente documentata
- [x] Deploy automatico GitHub → Streamlit Cloud
- [x] Repository pubblico e riproducibile

**Stato: PRODUCTION-READY per uso pubblico**