# Stato Progetto - Ultimo aggiornamento: 2026-01-06

## Fase Corrente
**Fase 0: Validazione Fattibilità - Settimana 1-2 completate**

## Completato
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

## In corso
- [ ] Commit e push progressi su GitHub
- [ ] Deploy Streamlit Cloud
- [ ] Bozza methodology.md (300 parole)

## Prossimi step (Settimana 3)
- Deploy Streamlit Cloud (app online)
- Documentazione methodology.md
- Decisione GO/NO-GO Fase 0

## Problemi aperti
Nessuno

## Note tecniche
- Environment: `osservatorio` (Python 3.11)
- Librerie: streamlit 1.41.1, plotly 5.24.1, pandas 2.2.3, numpy 2.2.1, jupyter 1.1.1
- Repository: https://github.com/AlbGri/osservatorio-criminalita-italia
- Dataset: delitti_2014_2023_istat.csv (18MB, 74.236 righe)
- Dataset pulito: delitti_totale_italia_2014_2023.csv (10 righe, 2014-2023)

## Ore dedicate
Giorno 1 (2026-01-05): ~2.5 ore (setup iniziale)
Giorno 2 (2026-01-06): ~4 ore (Settimana 1-2 roadmap)

**Totale Fase 0 finora: ~6.5 ore**

## Retrospettiva stime
**Roadmap vs Realtà:**
- Settimana 1 prevista: 10 ore → Reale: ~2 ore
- Settimana 2 prevista: 10 ore → Reale: ~2 ore
- **Totale Settimana 1-2: 20 ore previste vs 4 ore reali**

**Fattori:**
- Streamlit/Plotly: curve apprendimento più rapide del previsto
- ISTAT: dati accessibili facilmente
- Pandas: competenze pregresse probabilmente superiori a quelle assunte

**Azione:** Proseguire con Settimana 3. Rivalutare stime complete a fine Fase 0.