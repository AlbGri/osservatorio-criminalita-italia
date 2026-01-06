# Stato Progetto - Ultimo aggiornamento: 2026-01-06

## Fase Corrente
**Fase 1: MVP Dashboard Base - Grafico 1 completato**

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

### Fase 1: MVP Dashboard Base (IN CORSO)
- [x] Grafico 1: Trend nazionale normalizzato
  - [x] Download dati popolazione ISTAT (ricostruzione 2002-2019 + POSAS 2020-2023)
  - [x] Integrazione popolazione nel notebook
  - [x] Calcolo tasso per 1000 abitanti
  - [x] Dataset normalizzato salvato
  - [x] Aggiornamento app.py con tasso normalizzato
  - [x] Box giallo warning limiti dati
  - [x] Evidenziazione periodo COVID 2020-2021
  - [x] Deploy online aggiornato

## In corso
- [ ] Grafico 2: Percezione vs Dati (non iniziato)
- [ ] Grafico 3: Tipologie reato nel tempo (non iniziato)

## Prossimi step
- Acquisizione dati percezione sicurezza ISTAT
- Implementazione Grafico 2 (dual-axis)
- Implementazione Grafico 3 (breakdown tipologie)

## Problemi aperti
Nessuno

## Note tecniche
- Environment: `osservatorio` (Python 3.11)
- Librerie: streamlit 1.41.1, plotly 5.24.1, pandas 2.2.3, numpy 2.2.1, jupyter 1.1.1
- Repository: https://github.com/AlbGri/osservatorio-criminalita-italia
- Deploy: https://criminalita-italia.streamlit.app
- Dataset delitti: delitti_2014_2023_istat.csv (18MB, 74.236 righe)
- Dataset popolazione: ricostruzione 2002-2019 + POSAS 2020-2023
- Dataset processati:
  - delitti_totale_italia_2014_2023.csv (10 righe)
  - delitti_italia_normalizzato_2014_2023.csv (10 righe, include tasso per 1000 abitanti)

## Ore dedicate
Giorno 1 (2026-01-05): ~2.5 ore (setup iniziale)
Giorno 2 (2026-01-06): ~10 ore (Fase 0 completa + Grafico 1 Fase 1)

**Totale progetto: ~12.5 ore**
- Fase 0: ~8.5 ore (30 previste)
- Fase 1 parziale: ~4 ore

## Retrospettiva stime
**Fase 0:**
- Previste: 30 ore
- Reali: 8.5 ore
- Differenza: -72%

**Fase 1 (parziale - solo Grafico 1):**
- Roadmap non aveva stima per singolo grafico
- Grafico 1 completato in ~4 ore (include acquisizione dati popolazione, normalizzazione, implementazione)

**Osservazioni:**
- Velocità mantenuta anche in Fase 1
- Acquisizione dati popolazione ISTAT più laboriosa del previsto (formati diversi, necessità concatenazione)
- Normalizzazione per popolazione fondamentale per analisi corretta