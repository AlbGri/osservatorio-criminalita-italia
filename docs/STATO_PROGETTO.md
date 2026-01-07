# Stato Progetto - Ultimo aggiornamento: 2026-01-08

## Fase Corrente
**Fase 1: MVP Dashboard Base - Grafico 2 completato**

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

## In corso
- [ ] Grafico 3: Tipologie reato nel tempo (non iniziato)

## Prossimi step
- Implementazione Grafico 3 (breakdown tipologie: stacked area chart o small multiples)
- Acquisizione dati breakdown per categoria reato (furti, rapine, truffe, violenze, droga)
- Normalizzazione per popolazione per categoria
- Eventuale annotazione cambiamenti normativi rilevanti

## Problemi aperti
Nessuno

## Note tecniche
- Environment: `osservatorio` (Python 3.11)
- Librerie: streamlit 1.41.1, plotly 5.24.1, pandas 2.2.3, numpy 2.2.1, jupyter 1.1.1
- Repository: https://github.com/AlbGri/osservatorio-criminalita-italia
- Deploy: https://criminalita-italia.streamlit.app
- Dataset raw:
  - delitti_2014_2023_istat.csv (18MB, 74.236 righe)
  - percezione_criminalita_2014_2023_istat.csv (10 righe)
  - popolazione ISTAT: ricostruzione 2002-2019 + POSAS 2020-2023
- Dataset processati:
  - delitti_totale_italia_2014_2023.csv (10 righe)
  - delitti_italia_normalizzato_2014_2023.csv (10 righe, include tasso per 1000 abitanti)
  - percezione_vs_dati_2014_2023.csv (10 righe, include percezione + tasso + popolazione)

## Ore dedicate
Giorno 1 (2026-01-05): ~2.5 ore (setup iniziale)
Giorno 2 (2026-01-06): ~10 ore (Fase 0 completa + Grafico 1 Fase 1)
Giorno 3 (2026-01-08): ~4 ore (Grafico 2 completo: acquisizione dati, processing, implementazione, deploy, fix gitignore)

**Totale progetto: ~16.5 ore**
- Fase 0: ~8.5 ore (30 previste)
- Fase 1 parziale: ~8 ore (Grafico 1 + Grafico 2)

## Retrospettiva stime
**Fase 0:**
- Previste: 30 ore
- Reali: 8.5 ore
- Differenza: -72%

**Fase 1 (parziale - Grafico 1 + Grafico 2):**
- Roadmap non aveva stima per singolo grafico
- Grafico 1 completato in ~4 ore (acquisizione popolazione, normalizzazione, implementazione)
- Grafico 2 completato in ~4 ore (acquisizione percezione, merge dataset, dual-axis chart)

**Osservazioni:**
- Velocità mantenuta costante (~4 ore per grafico completo)
- Pattern ripetibile: download dati → pulizia notebook → merge → implementazione → deploy
- ISTAT data discovery più veloce dopo esperienza Grafico 1
- Dual-axis chart più complesso di line chart singolo ma documentazione Plotly chiara
- Fix gitignore e troubleshooting deploy: ~30 minuti extra

## Blocchi risolti
**Streamlit Cloud non aggiorna dopo push:**
- Causa: nuovi file CSV richiedono ricostruzione ambiente
- Soluzione: usare "Reboot" invece di "Rerun" dalle settings app
- Tempo perso: ~15 minuti
- Lesson learned: Reboot per nuovi file, Rerun per solo codice