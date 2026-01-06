# Stato Progetto - Ultimo aggiornamento: 2026-01-06

## Fase Corrente
**Fase 1: MVP Dashboard Base - Inizio**

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
- [x] Rimozione file privati da GitHub (PROMPT.md, roadmap.md, SETUP_WINDOWS.md)
- [x] Deploy Streamlit Cloud (criminalita-italia.streamlit.app)
- [x] Documentazione methodology.md (380 parole)
- [x] Decisione GO/NO-GO: GO Fase 1

## In corso

### Fase 1: MVP Dashboard Base
- [ ] Grafico 1: Migliorare trend con normalizzazione popolazione
- [ ] Download dati popolazione ISTAT 2014-2023

## Prossimi step
- Acquisizione dati popolazione ISTAT
- Calcolo tasso delitti per 1000 abitanti
- Box giallo avviso limiti dati
- Evidenziare periodo COVID nel grafico

## Problemi aperti
Nessuno

## Note tecniche
- Environment: `osservatorio` (Python 3.11)
- Librerie: streamlit 1.41.1, plotly 5.24.1, pandas 2.2.3, numpy 2.2.1, jupyter 1.1.1
- Repository: https://github.com/AlbGri/osservatorio-criminalita-italia
- Deploy: https://criminalita-italia.streamlit.app
- Dataset: delitti_2014_2023_istat.csv (18MB, 74.236 righe)
- Dataset pulito: delitti_totale_italia_2014_2023.csv (10 righe, 2014-2023)

## Ore dedicate
Giorno 1 (2026-01-05): ~2.5 ore (setup iniziale)
Giorno 2 (2026-01-06): ~6 ore (Settimana 1-3 roadmap, deploy, methodology)

**Totale Fase 0: ~8.5 ore su 30 previste (72% sotto stima)**

## Retrospettiva stime Fase 0
**Roadmap vs Realtà:**
- Settimana 1 prevista: 10 ore → Reale: ~2 ore
- Settimana 2 prevista: 10 ore → Reale: ~2 ore  
- Settimana 3 prevista: 10 ore → Reale: ~4.5 ore
- **Totale Fase 0: 30 ore previste vs 8.5 ore reali**

**Fattori velocità:**
- Curve apprendimento Streamlit/Plotly più rapide
- Dati ISTAT facilmente accessibili
- Competenze pregresse pandas/python
- Setup tecnico senza intoppi

**Conclusione Fase 0:**
Validazione fattibilità superata con successo. App funzionante online con dati reali. Proseguimento con Fase 1 approvato.

**Azione per Fase 1:**
Monitorare velocità task Fase 1 prima di rivalutare stime complete. Approccio incrementale step-by-step.