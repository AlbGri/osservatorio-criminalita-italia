================================================================================
PROGETTO: OSSERVATORIO CRIMINALITA ITALIA
Scaletta Operativa - Versione Completa e Definitiva
================================================================================

Versione: 2.0
Data: 2026-01-05
Stato: Living Document
Licenza: CC BY 4.0


================================================================================
SEZIONE 0: PRINCIPI FONDATIVI DEL PROGETTO
================================================================================

OBIETTIVO RIFORMULATO
----------------------
Creare una piattaforma open source che permetta di ESPLORARE i dati ufficiali
sulla criminalita in Italia in modo trasparente, contestualizzato e 
metodologicamente rigoroso, facilitando la comprensione del divario tra 
percezione pubblica e dati registrati.

NON e: uno strumento per dimostrare una tesi precostituita
E: un facilitatore di comprensione basato su dati pubblici verificabili


PRINCIPI GUIDA OPERATIVI CON IMPLEMENTAZIONE CONCRETA
------------------------------------------------------

1. Trasparenza metodologica
   IMPLEMENTAZIONE: Ogni dataset ha file metadata.json con fonte URL, data
   download, trasformazioni applicate, script usato
   
2. Neutralita comunicativa
   IMPLEMENTAZIONE: Revisione titoli grafici con checklist che evita termini
   come drammatico, allarme, finalmente, smentisce. Utilizzare: trend,
   variazione, confronto
   
3. Onesta sui limiti
   IMPLEMENTAZIONE: Box giallo prominente sopra ogni grafico con testo:
   Questi dati mostrano [cosa mostrano] e NON mostrano [cosa non mostrano]
   
4. Design anti-cherry-picking
   IMPLEMENTAZIONE CONCRETA:
   - Homepage mostra tutti i grafici insieme, no deep link a singoli
   - Watermark su grafici: Fonte [progetto] - Vedi contesto completo
   - Download grafico singolo disabilitato, solo Condividi dashboard completa
   - Se tecnicamente impossibile: dichiarare limite e monitorare uso improprio
   
5. Etica della visualizzazione
   IMPLEMENTAZIONE: Scale colori pre-approvate ColorBrewer sequential diverging,
   mai rosso per peggio. Regola: nessun dato sotto livello provinciale
   Compromesso documentato: utilita versus stigmatizzazione


BUDGET REALISTICO
-----------------
Fase 1-2: 0 euro con Streamlit Cloud free, 1 app, limiti accettabili
Fase 3: 10-15 euro mensili con Render Starter o Railway Hobby per performance
Dominio: 10-15 euro annui, opzionale, rinviabile
TOTALE ANNO 1: 120-180 euro
Se non sostenibile: rimanere su free tier, accettare limitazioni performance


================================================================================
SEZIONE 1: ARCHITETTURA DEL PROGETTO
================================================================================

1.1 STACK TECNICO FINALE
-------------------------
Frontend e Dashboard: Streamlit per tutte le fasi
Visualizzazioni: Plotly
Data processing: pandas, numpy
Automazione dati: richieste HTTP dirette API ISTAT ed Eurostat, no librerie terze
Versioning: Git e GitHub con branch main e develop
Hosting: Streamlit Cloud per Fase 1-2, valutare Render per Fase 3 se necessario
Documentazione: README piu cartella docs piu inline comments
CI CD: GitHub Actions solo da Fase 3, ora e prematura
Accessibilita: Streamlit built-in piu contrasto WCAG AA manuale


1.2 STRUTTURA REPOSITORY
-------------------------
osservatorio-criminalita-italia/
  data/
    raw/
      istat_2024_provisional/
      istat_2024_final/
    processed/
    metadata/
      [dataset].json
  src/
    data_acquisition/
    data_cleaning/
    visualizations/
    app.py
  docs/
    methodology.md
    interpretation_guide.md
    data_sources.md
    development_diary.md
    known_issues.md
    testing_protocol.md
  tests/
    data_validation.py
  .github/
    workflows/
      data_validation.yml
  PRIVACY_POLICY.md
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md
  requirements.txt


GESTIONE DATI CRITICO
----------------------
Git LFS: NO. Limite 1GB free totale, insufficiente

Soluzione Fase 1-2: dati raw in repository, CSV compressi minori di 50MB

Soluzione Fase 3: dati raw su Google Drive pubblico linkato con script download
automatico locale. Repository contiene solo processed aggregati leggeri

Fallback: Zenodo, repository dati scientifici, free fino 50GB per dataset


================================================================================
SEZIONE 2: ROADMAP INCREMENTALE REALISTICA
================================================================================

TIMELINE ONESTA
---------------
Ipotesi: 10 ore settimanali dedicate
Fase 0: 3 settimane, 30 ore
Fase 1: 10-12 settimane, 100-120 ore
Fase 2: 8-10 settimane, 80-100 ore
Fase 3: 12-16 settimane, 120-160 ore
TOTALE: 33-41 settimane equivalenti a 8-10 MESI, non 6


QUICK WINS PER MOTIVAZIONE
---------------------------
Dopamina programmata ogni 2-3 settimane:
Settimana 2: primo grafico statico in Jupyter
Settimana 3: deploy Streamlit Hello World
Settimana 6: MVP con 2 grafici online, condiviso con 3 amici
Settimana 10: Fase 1 completa, post Reddit
Settimana 18: prima mappa regionale funzionante
Settimana 25: Fase 2 completa, richiesta feedback esperti
Settimana 35: Fase 3 completa, considerare paper o blog


-------------------------------------------------------------------------------
FASE 0: VALIDAZIONE FATTIBILITA
-------------------------------------------------------------------------------
Durata: 3 settimane, 30 ore
OBIETTIVO: Capire se proseguire PRIMA di investire 300 ore


Settimana 1, 10 ore:
4 ore: tutorial Streamlit con app.py base, st.line_chart, deploy
3 ore: tutorial Plotly con line, bar, layout
3 ore: esplorazione portale dati.istat.it, individuare dataset Delitti denunciati


Settimana 2, 10 ore:
5 ore: download manuale CSV ISTAT Delitti denunciati 2014-2024 nazionale
3 ore: pulizia in Jupyter con pandas, gestire missing, formato date, normalizzazione popolazione
2 ore: grafico Plotly trend nazionale, export PNG


Settimana 3, 10 ore:
4 ore: Streamlit app.py con grafico Settimana 2 integrato
2 ore: deploy Streamlit Cloud, test funzionamento
2 ore: bozza docs/methodology.md, 300 parole su cosa sono denunce versus crimini
2 ore: decisione GO o NO-GO piu planning Fase 1 dettagliato


CRITERI GO:
Deploy funzionante
Grafico leggibile
Dati ISTAT accessibili anche manualmente
Motivazione ancora alta


CRITERI NO-GO:
Frustrazione tecnica eccessiva, oltre 15 ore bloccato su 1 problema
Dati ISTAT irreperibili o troppo frammentati
Realizzazione: non mi interessa piu


OUTPUT FASE 0:
App Streamlit online con 1 grafico piu metodologia 300 parole
Repository GitHub inizializzato
Decision log: proseguire o pivot


-------------------------------------------------------------------------------
FASE 1: MVP - DASHBOARD BASE
-------------------------------------------------------------------------------
Durata: 10-12 settimane, 100-120 ore
OBIETTIVO: Dashboard minima pubblicabile con credibilita scientifica


SCOPE RIDOTTO rispetto a scaletta originale:
3 grafici, non 4: rimuovo Numero Oscuro da Fase 1, troppo complesso comunicativamente. 
Diventa box testuale con infografica statica in Fase 2
1 sola fonte: solo ISTAT nazionale, no Eurostat, no Ministero Interno
Periodo: 2014-2024, 10 anni sufficienti per trend lungo periodo


1.1 DATI
--------
Dataset ISTAT prioritari:
1. Delitti denunciati all autorita giudiziaria per tipo, serie storica nazionale
2. Percezione di sicurezza delle famiglie, indagine multiscopo


PROCESSO ACQUISIZIONE:
Tentativo 1: API REST ISTAT diretta, documentazione sdmx.istat.it
Tentativo 2: download manuale da dati.istat.it piu script parsing
Logging: docs/data_acquisition_log.md con date, problemi, soluzioni


GESTIONE VERSIONING DATI:
Dati ISTAT provvisori 2024: cartella data/raw/istat_2024_provisional/
Quando escono definitivi: nuova cartella data/raw/istat_2024_final/
Processed usa sempre ultimi disponibili
metadata.json traccia quale versione usata per ogni grafico


1.2 VISUALIZZAZIONI CORE 3 GRAFICI
-----------------------------------

GRAFICO 1: Trend Nazionale Criminalita Registrata
Tipo: Line chart Plotly
Dati: Totale delitti per 1000 abitanti, 2014-2024
Implementazione:
  Normalizzazione: delitti diviso popolazione moltiplicato 1000, ISTAT demo annuale
  Evidenziare COVID: linea tratteggiata 2020-2021, annotazione Periodo lockdown
  Box giallo sopra: Questi dati mostrano DENUNCE registrate, non crimini
  effettivamente commessi. Alcuni reati non vengono denunciati come violenze
  domestiche, altri hanno alta propensione come furti auto
  Footer grafico: Fonte ISTAT Delitti denunciati. Ultimo aggiornamento [data]
Domanda risposta: E vero che la criminalita e aumentata negli ultimi 10 anni


GRAFICO 2: Percezione versus Dati Registrati
Tipo: Dual-axis line chart
Dati: 
  Serie 1: percentuale famiglie percepiscono rischio criminalita zona, ISTAT Multiscopo
  Serie 2: Tasso delitti per 1000 abitanti, stesso Grafico 1
Implementazione:
  Due assi Y per scale diverse
  Evidenziare divergenza con area ombreggiata
  Box giallo: La percezione di insicurezza non e sbagliata. Risponde a fattori
  legittimi: copertura mediatica, degrado urbano, sfiducia istituzionale, 
  esperienza personale. Questi dati mostrano che percezione e criminalita
  registrata seguono dinamiche diverse
Domanda risposta: Quanto e grande il gap tra percezione e dati


GRAFICO 3: Tipologie di Reato nel Tempo
Tipo: Stacked area chart o small multiples, testare usabilita
Dati: Breakdown per macro-categoria: furti, rapine, violenze, truffe, droga
Implementazione:
  Normalizzazione per popolazione
  Evidenziare pattern: aumento truffe post-digitale, calo furti abitazioni
  Annotazione: 2018 modifica normativa, specifica se rilevante
  Box giallo: Aumenti in specifiche categorie possono riflettere cambiamenti
  sociali come piu truffe online senza necessariamente indicare piu criminalita
  complessiva. Le categorie riflettono classificazioni penali, non percezione comune
Domanda risposta: Cosa e cambiato negli ultimi 10 anni


1.3 STRUTTURA APPLICAZIONE STREAMLIT
-------------------------------------

app.py struttura:

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(
    page_title="Osservatorio Criminalita Italia",
    page_icon="grafico",
    layout="wide",
    initial_sidebar_state="expanded"
)

page = st.sidebar.radio(
    "Navigazione",
    ["Dashboard", "Metodologia", "Guida Interpretazione", "Limitazioni", "Dati e Codice"]
)

if page == "Dashboard":
    render_dashboard()
elif page == "Metodologia":
    render_methodology()
elif page == "Guida Interpretazione":
    render_interpretation_guide()
elif page == "Limitazioni":
    render_limitations()
else:
    render_data_code()

render_footer()


HOMEPAGE DASHBOARD:
Titolo: Osservatorio Criminalita Italia - Dati Aperti
Sottotitolo 2 righe: Questa dashboard visualizza dati ufficiali ISTAT
sulla criminalita registrata in Italia. Obiettivo: facilitare la comprensione
di trend spesso diversi dalla percezione pubblica, con trasparenza metodologica
Alert prominente: Ultimo aggiornamento dati [data]. Dati provvisori o definitivi
3 grafici core impilati verticalmente
Ogni grafico: box giallo contestuale sopra piu footer fonte sotto
Bottone: Scarica dati aggregati CSV, no screenshot singoli grafici


PAGINA METODOLOGIA:
Sezioni obbligatorie:

1. Cosa misurano questi dati
   Denunce registrate alle forze di polizia diverso da crimini effettivamente commessi.
   Questi dati misurano la criminalita EMERSA, non quella totale

2. Il fenomeno del numero oscuro
   Spiegazione con esempi concreti:
   Furti auto: circa 90 percento denunciati per necessita assicurativa
   Violenze domestiche: circa 80 percento NON denunciati per paura, vergogna, dipendenza
   Truffe piccole: circa 40 percento denunciati per rassegnazione
   Fonte stime: ISTAT Indagine Vittimizzazione [anno]

3. Perche le denunce possono variare senza variazioni criminalita reale
   Campagne sensibilizzazione come MeToo portano a piu denunce violenze,
   NON necessariamente piu violenze
   Cambiamenti normativi: nuovi reati digitali appaiono nelle statistiche
   Fiducia forze ordine: se aumenta, aumentano denunce
   Crisi economica: calo furti auto per meno macchine di valore

4. Limiti confronti temporali
   GDPR 2018: blocco pubblicazione dati disaggregati per mesi
   COVID 2020-2021: outlier per lockdown
   Riforme penali: depenalizzazioni o inasprimenti cambiano classificazioni

5. Fonti dati esatte
   ISTAT Delitti denunciati con link diretto dataset
   ISTAT Sicurezza cittadini con link
   Popolazione: ISTAT Demo con link
   Licenze: CC BY 3.0 IT ISTAT

6. Elaborazioni applicate
   Dati grezzi: conteggi assoluti per anno
   Elaborazioni: normalizzazione per popolazione per 1000 abitanti, aggregazioni
   macro-categorie secondo classificazione ISTAT
   Nessun smoothing, interpolazione, o modellazione predittiva applicata

7. Data ultimo aggiornamento: [data]

8. Codice sorgente: link GitHub con istruzioni replicare analisi


PAGINA GUIDA INTERPRETAZIONE NUOVA:
Come leggere questi grafici

1. Cosa significa per 1000 abitanti
   Se leggi 45 delitti per 1000 abitanti, significa: in una citta di 100000
   persone, ci sono stati circa 4500 delitti denunciati in un anno. NON significa
   che il 4.5 percento della popolazione ha subito un reato perche alcuni ne 
   subiscono piu di uno, molti zero

2. Come interpretare trend
   Pendenza linea: velocita cambiamento
   Confrontare sempre periodi lunghi 5-10 anni, non anno-anno
   Attenzione outlier COVID

3. Cosa NON si puo concludere dai grafici
   Territorio X e piu sicuro di Y, propensione denuncia varia
   Criminalita e colpa di gruppo demografico, dati non mostrano autori
   Non devo preoccuparmi, percezione rischio e legittima e personale

4. Domande comuni
   Q: Perche alcuni reati aumentano ma totale cala
   A: Composizione cambia. Esempio: meno furti meno 20 percento ma piu truffe
   piu 50 percento, se furti erano 80 percento e truffe 5 percento, totale puo calare
   
   Q: Posso usare questi dati per decidere dove vivere
   A: Con cautela. Dati provinciali mascherano variabilita interna enorme.
   Milano provincia include sia zone centrali dense che comuni rurali


PAGINA LIMITAZIONI NOTE:
Lista trasparente, bullet points accettabili qui:

COSA QUESTO PROGETTO NON PUO DIRE:
Se un territorio specifico e sicuro o pericoloso, dati provinciali troppo
aggregati, numero oscuro varia localmente
Se specifici gruppi demografici sono piu criminali, dati non disaggregano
autori, esistono bias registrazione
Previsioni future, no modellazione predittiva
Criminalita reale totale, solo quella registrata

BIAS NOTI NON CORREGGIBILI:
Under-reporting sistematico alcuni reati come violenze genere, domestiche
Over-reporting altri come furti con necessita assicurative
Variabilita territoriale propensione denuncia, Nord diverso da Sud
Effetti copertura mediatica su denunce, caso mediatico provoca picco temporaneo

COMPROMESSI DESIGN:
Livello minimo provincia, sacrifica utilita locale per evitare stigmatizzazione
No dati anteriori a 2014 per qualita e comparabilita dubbia
No dati real-time, ISTAT ha ritardo 12-18 mesi fisiologico

COSA FARE SE TROVI ERRORI:
Link GitHub Issues piu email contatto


PAGINA DATI E CODICE:
Link repository GitHub
Istruzioni: clone, install requirements, run locale
Download CSV aggregati, non raw per dimensioni
Licenze: MIT codice, CC BY 4.0 documentazione
Attribuzione: Dati ISTAT elaborati da [progetto]


FOOTER TUTTE PAGINE:
Progetto open source. Non sostituisce analisi criminologiche professionali
Link: GitHub - Metodologia - Segnala Errore - Privacy Policy
Realizzato da [nome]. Ultima build [data commit]


1.4 ACCESSIBILITA WCAG AA
--------------------------
Checklist implementazione:

Contrasto colori:
  Testo su sfondo: minimo 4.5 a 1, Streamlit default OK
  Grafici: palette ColorBrewer come Blues o Viridis per linee multiple
  Testare con WebAIM Contrast Checker

Navigazione tastiera:
  Streamlit sidebar navigabile con Tab
  Grafici Plotly: skip navigation con Shift Tab

Screen reader:
  Titoli semantici st.title, st.header
  Alt text immagini se usate
  Grafici Plotly: aria-label con descrizione testuale trend

Responsive:
  Testare su smartphone, grafici Plotly possono essere piccoli
  Font size minimo 14px
  No scroll orizzontale

Note: Streamlit limita controllo granulare HTML CSS. Fare il possibile con
tool disponibile, documentare limiti in known_issues.md


1.5 TEST USABILITA STRUTTURATO
-------------------------------
PROTOCOLLO in docs/testing_protocol.md:

Reclutamento:
  6-8 partecipanti: mix background, 2 tecnici, 2 non-tecnici, 2 anziani, 2 giovani
  NO amici stretti per evitare bias positivo
  Compenso: caffe o birra o niente, specificare volontariato
  Consenso informato: Testiamo il sito, non te. Feedback onesti benvenuti

Task:
1. Trova informazione: la criminalita in Italia negli ultimi 10 anni e
   aumentata, diminuita, o stabile
2. Spiega con parole tue cosa significa numero oscuro
3. C e qualcosa che ti ha confuso, cosa

Metodo:
  Think-aloud: partecipante verbalizza pensieri mentre naviga
  Osservatore prende note, NO interruzioni durante task
  Intervista post-task: domande aperte su chiarezza, neutralita, fiducia

Metriche:
  Task 1-2: successo SI o NO
  Tempo completamento task
  Feedback qualitativo su comprensibilita, percezione bias, utilita

Red flags:
  Oltre 50 percento fallisce task 1: grafici poco chiari
  Qualcuno dice sembra voler convincermi di qualcosa: framing non neutro
  Confusione su fonte dati: metodologia carente

IMPORTANTE: NO test con vittime reati in Fase 1. Troppo rischioso senza
competenze psicologiche. Rinviare a Fase 3 con supporto professionista
o associazione vittime


1.6 PRIVACY E ANALYTICS
-----------------------
OBBLIGATORIO: PRIVACY_POLICY.md

Se usi analytics come Streamlit built-in, Plausible, o niente:

NESSUN ANALYTICS, opzione consigliata Fase 1:
  Privacy policy semplice: Questo sito non raccoglie dati personali.
  Nessun cookie, nessun tracking
  Vantaggio: zero complicazioni GDPR

CON ANALYTICS MINIMALI Fase 2 piu:
  Tool: Plausible GDPR-friendly, no cookie
  Dati: solo pageviews aggregate, no IP, no fingerprinting
  Privacy policy: Usiamo Plausible per contare visite con dati aggregati, 
  nessuna identificazione utente. Dati non venduti o condivisi
  Cookie banner: non necessario con Plausible

ANALYTICS DETTAGLIATI sconsigliato:
  Se proprio vuoi Google Analytics: cookie banner obbligatorio, privacy
  policy complessa, gestione consenso. Non ne vale la pena per progetto personale


1.7 RILASCIO FASE 1
-------------------
CHECKLIST PRE-LANCIO:

Contenuti:
  Tutti grafici titoli neutri, test con checklist evita drammatico, allarme
  Box gialli contestuali sopra ogni grafico
  Metodologia completa e leggibile da non-statistico
  Guida interpretazione presente
  Limitazioni note esplicite e oneste
  Footer con disclaimer piu link GitHub

Tecnica:
  Repository GitHub pubblico
  README completo: screenshot, istruzioni install, licenze
  requirements.txt testato in virtualenv pulito
  .gitignore no .env, no dati sensibili se presenti
  Licenze dichiarate: MIT codice, CC BY 4.0 docs
  Deploy Streamlit Cloud funzionante
  Test 3 browser: Chrome, Firefox, Safari o Edge
  Test mobile almeno navigabile
  Performance minore di 5 secondi caricamento homepage

Etica:
  Scale colori neutre, no rosso uguale pericolo
  Nessuna stigmatizzazione territoriale nel testo
  Test usabilita 6-8 persone completato
  Feedback integrato

Governance:
  CONTRIBUTING.md
  CODE_OF_CONDUCT.md con Contributor Covenant template
  Issue templates GitHub: bug, feature, domanda
  Email contatto pubblico per segnalazioni

Legale:
  PRIVACY_POLICY.md
  Disclaimer footer

OUTPUT FASE 1:
  URL dashboard online
  Repository GitHub con documentazione
  6-8 feedback usabilita positivi su comprensibilita
  Decision log: proseguire Fase 2 o fermarsi qui, accettabile


LANCIO COMUNICAZIONE:
Post LinkedIn Mastodon Twitter: Ho creato dashboard open source per esplorare
dati ISTAT criminalita Italia. Obiettivo: trasparenza e contesto. Feedback
Submit: r/dataisbeautiful con screenshot, r/italy con cautela, Hacker News
Show HN: Open source crime data dashboard for Italy
EVITARE Fase 1: contatto giornalisti proattivo per rischio framing incontrollabile


GESTIONE ATTENZIONE MEDIATICA NON RICHIESTA:
Se giornalista contatta:
  Risposta template: Progetto visualizza dati pubblici ISTAT in modo trasparente.
  Non supporta conclusioni specifiche, obiettivo e facilitare comprensione.
  Prego citare URL completa dashboard non screenshot singoli per contesto
  Se intervista: enfatizzare limiti dati, neutralita, invitare a leggere metodologia
  Se framing sensazionalistico: tweet correzione piu documentare su GitHub


-------------------------------------------------------------------------------
FASE 2: ESPANSIONE TERRITORIALE
-------------------------------------------------------------------------------
Durata: 8-10 settimane, 80-100 ore
OBIETTIVO: Aggiungere dimensione geografica mantenendo rigore


2.1 NUOVI DATI
--------------
ISTAT Delitti denunciati disaggregato regionale e provinciale 2014-2024
ISTAT Demo popolazione regionale e provinciale per normalizzazione
ISTAT Percezione sicurezza disaggregato regionale se disponibile

ATTENZIONE: Controllo qualita dati provinciali piu complesso. Alcune province
piccole hanno conteggi bassi che causano alta variabilita anno-anno. Soglia minima:
province con meno di 100000 abitanti aggregare con vicine o flag dati instabili


2.2 NUOVE VISUALIZZAZIONI
--------------------------

GRAFICO 4: Il Numero Oscuro, recupero da Fase 1
Tipo: Infografica statica Plotly, no interattivita
Dati: Stime ISTAT indagine vittimizzazione per macro-categoria
Implementazione:
  Iceberg chart: parte emersa denunce, sommersa non denunciate
  Percentuali per tipo reato
  Box giallo: Stime basate su survey ISTAT vittimizzazione [anno]. Margine
  errore piu o meno X percento. Numero oscuro varia molto tra reati e territori
Domanda risposta: Cosa NON vediamo in questi dati


GRAFICO 5: Geografia Criminalita Registrata - Regioni
Tipo: Mappa coropletica Italia
Dati: Tasso delitti per 1000 abitanti per regione, anno selezionabile con slider
Implementazione:
  Palette: ColorBrewer Blues, chiaro uguale basso, scuro uguale alto, MAI rosso
  Slider anno: 2014-2024
  Tooltip regione: tasso, popolazione, confronto versus media nazionale
  Box giallo: Regioni con alto turismo o pendolarismo hanno piu denunce per
  effetto popolazione temporanea. Confronti diretti problematici. Dati mostrano
  criminalita REGISTRATA, propensione denuncia varia, Nord generalmente piu
  alta che Sud
  Footer: Fonte ISTAT. Dati provinciali disponibili sotto

DESIGN ETICO CRITICO:
  NO zoom province nella mappa, troppo dettaglio, rischio stigmatizzazione
  NO classifiche regioni piu sicure in titolo o UI
  Se utente chiede ranking: mostrare ma con warning prominente limitazioni


GRAFICO 6: Esplora Province Tabella Interattiva
Tipo: DataTable Streamlit con sort e filter
Dati: Provincia, tasso 2024, variazione 2014-2024, popolazione
Implementazione:
  Ordinabile per colonna
  Filtro per regione
  NO colori semaforici verde uguale bene, rosso uguale male
  Click provincia espande con small line chart trend 10 anni
  Box giallo: Dati provinciali NON indicano sicurezza specifica quartieri o comuni.
  Variabilita interna province molto alta. Propensione denuncia influenza ranking

ALTERNATIVA GRAFICO 6: Comparatore Provinciale
Se tabella troppo tecnica:
  Dropdown multi-select: scegli 2-4 province
  Line chart sovrapposti trend temporali
  Piu accessibile per utenti non-tecnici


2.3 FEATURE TECNICA: INTERATTIVITA
-----------------------------------
Sidebar filter: range anni con slider 2014-2024
Dropdown: tipo reato, totale, furti, rapine, violenze, truffe
Grafici si aggiornano dinamicamente
Caching Streamlit con st.cache_data per performance

WARNING TECNICO: Dataset provinciali circa 107 province per 10 anni per N categorie
uguale grosso. Testare memoria Streamlit Cloud. Se supera limiti free 1GB:
  Ottimizzazione 1: Parquet invece CSV per compressione migliore
  Ottimizzazione 2: Aggregazioni pre-calcolate, no calcolo on-the-fly
  Ultima risorsa: passare a Render 15 euro mensili ma piu memoria


2.4 AGGIORNAMENTO METODOLOGIA
------------------------------
Aggiungere sezione: Confronti territoriali: limiti e cautele

1. Effetto popolazione temporanea
   Citta metropolitane Roma, Milano, Firenze hanno milioni turisti e pendolari
   giornalieri non conteggiati in popolazione residente. Tassi per 1000 abitanti
   sovrastimano criminalita relativa. Esempio: Roma 30-50k turisti al giorno, Milano
   simile. Tasso reale probabilmente 20-30 percento piu basso se normalizzato per
   popolazione effettiva giornaliera

2. Propensione denuncia territoriale
   Studi mostrano: Nord Italia propensione denuncia mediamente 15-20 percento piu alta
   che Sud con fonte ISTAT Vittimizzazione. Differenze attribuibili a:
   Fiducia forze ordine
   Presenza criminalita organizzata con omerta
   Necessita assicurative, piu auto di valore al Nord
   Ranking territoriali riflettono MIX tra criminalita reale e propensione

3. Variabilita piccoli territori
   Province minori di 200k abitanti: conteggi bassi causano alta variabilita casuale anno-anno.
   Variazione piu 30 percento in provincia piccola puo essere 50 reati in piu, non significativo,
   stessa percentuale in metropoli uguale 5000 reati, significativo. Guardare trend pluriennali


2.5 TEST E FEEDBACK SPECIALISTICO
----------------------------------
Fase 2 e momento giusto per feedback esperti

Target:
  2-3 ricercatori criminologia come Transcrime, ISI Foundation, universita
  1-2 data journalists specializzati
  1 statistico ISTAT o accademico per validazione metodologica

Approccio:
  Email fredda: Progetto open source visualizzazione dati criminalita ISTAT.
  Gradirei feedback metodologico o comunicativo da esperto. 20 minuti call
  Videocall: mostrare dashboard, chiedere red flags
  Integrare feedback credibili citando: Grazie a [nome] per revisione metodologica

Gestione feedback contrastanti:
  Se esperto dice dovresti mostrare X: valutare ma non vincolo
  Se dice Y e errore metodologico grave: correggere subito
  Documentare dibattiti aperti in docs/known_issues.md

OUTPUT FASE 2:
  Dashboard con 6 grafici, 3 nuovi territoriali
  Metodologia aggiornata con sezione confronti territoriali
  Feedback positivi da almeno 2 esperti
  Performance accettabile con dati provinciali
  Decision log: proseguire Fase 3 o dichiarare progetto completo v1.0

MILESTONE MOTIVAZIONALE:
Prima mappa Italia funzionante uguale dopamina alta. Celebrare


-------------------------------------------------------------------------------
FASE 3: CONTESTO EUROPEO E MATURITA PROGETTO
-------------------------------------------------------------------------------
Durata: 12-16 settimane, 120-160 ore
OBIETTIVO: Contestualizzare Italia in Europa, finalizzare sostenibilita


3.1 NUOVI DATI E GESTIONE COMPLESSITA
--------------------------------------

SELEZIONE PAESI con razionale esplicito:
Francia: paese comparabile per popolazione, economia, sistema giudiziario
Germania: standard Eurostat alto, dati affidabili
Spagna: simile Italia culturalmente e geograficamente
UK: escluso per Brexit, dati non piu Eurostat integrati
Polonia: Europa Est per diversita, trend interessanti
Svezia: Nordici, tassi bassi, contrasto istruttivo

CRITERI SELEZIONE:
1. Disponibilita dati Eurostat 2014-2024 continui
2. Metodologia comparabile, almeno categorie armonizzate
3. Popolazione maggiore di 10M per evitare micro-stati con outlier
4. Mix geografico e culturale UE


CRITICITA METODOLOGICA MAGGIORE: COMPARABILITA

Eurostat fornisce dati armonizzati MA:
Robbery UK include scippo in strada, IT no, diversa categoria
Burglary include tentativi in alcuni paesi, solo successi in altri
Propensione denuncia varia enormemente: Nordici 70-80 percento, Sud Europa 40-50 percento

SOLUZIONE OBBLIGATORIA:
  Usare SOLO categorie Eurostat Livello 1, macro aggregate, meno ambigue
  Creare docs/eurostat_comparability.md con tabella:
  Categoria - IT definizione - FR def - DE def - ES def - PL def - SE def
  Robbery - ... - ... - ... - ... - ... - ...
  Link metadati nazionali Eurostat per ogni paese
  Disclaimer prominente OGNI grafico internazionale:
  Confronti approssimativi. Metodologie nazionali variano. Vedi Metodologia


3.2 NUOVE VISUALIZZAZIONI
--------------------------

GRAFICO 7: Italia nel Contesto Europeo
Tipo: Small multiples, 6 line charts, 1 per paese
Dati: Trend totale criminalita 2014-2024, normalizzato per 1000 abitanti
Implementazione:
  Italia evidenziata con linea piu spessa, colore diverso
  Altri paesi grigio chiaro
  Stesso range Y per comparabilita
  Titolo: Trend Criminalita Registrata - Confronto Europeo
  NON Italia versus Europa che implica giudizio
  Box giallo: Confronti influenzati da propensione denuncia nazionale.
  Paesi Nordici denunciano piu frequentemente 70-80 percento reati versus Sud Europa
  40-50 percento. Dati mostrano criminalita REGISTRATA, non reale totale


GRAFICO 8: Posizionamento Italia - Anno Selezionato
Tipo: Bar chart orizzontale ordinato
Dati: Tasso criminalita 2024 per 6 paesi piu Italia
Implementazione:
  Ordinamento crescente, basso a sinistra, alto a destra
  Italia barra colore diverso, non rosso o verde
  NO titolo Classifica sicurezza o Paesi piu pericolosi
  Titolo: Criminalita Registrata per Paese - Anno 2024
  Annotazioni: flag paesi con note metodologiche come Svezia include tentativi
  Box giallo: Ranking NON indica sicurezza oggettiva. Influenzato da
  propensione denuncia, definizioni legali nazionali, efficienza registrazione.
  Paesi con sistemi piu efficienti possono apparire peggio per migliore rilevazione


3.3 GESTIONE DATI: SOLUZIONE STORAGE
-------------------------------------

PROBLEMA: Dati Eurostat multi-paese superano limiti repository GitHub 100MB

SOLUZIONE IMPLEMENTATA:
1. Dati raw su Zenodo, repository dati scientifici, DOI permanente, free 50GB
   Upload: dataset completo Eurostat estratto, documentato, versionato
   DOI Zenodo in README e docs/data_sources.md
   
2. Repository GitHub contiene:
   Script download Zenodo in src/data_acquisition/download_zenodo.py
   Dati processed aggregati leggeri minori di 10MB
   Metadata completi
   
3. Utente che clona repository:
   Opzione 1: usa dati processed sufficienti per visualizzazioni
   Opzione 2: run script download Zenodo se vuole raw per ricercatori

ALTERNATIVE VALUTATE:
Google Drive: no DOI, meno scientifico
Git LFS: limiti free insufficienti
Figshare: valida, ma Zenodo preferito per integrazione ricerca EU


3.4 AUTOMAZIONE E MONITORING FINALMENTE
----------------------------------------

ORA e il momento per GitHub Actions perche progetto maturo, vale la pena

.github/workflows/data_validation.yml
Trigger: ogni lunedi mattina con cron 0 6 asterisco asterisco 1
Job:
1. Check calendario ISTAT: nuovi dati pubblicati con scraping pagina ISTAT news
2. Se si: crea Issue GitHub Nuovi dati ISTAT [anno] disponibili - Aggiornamento necessario
3. Download dati ISTAT con script src/data_acquisition
4. Run test validazione: data/tests/validate_schema.py
   Colonne attese presenti
   Range valori plausibili come tasso minore di 1000 per 1000 abitanti
   No missing critici
5. Se test falliscono: Issue GitHub ALERT Validazione dati fallita
6. Se test passano e dati nuovi: commit automatico dati processed, ping maintainer

MONITORING UPTIME:
Tool: UptimeRobot free, 50 monitor, check ogni 5 minuti
Alert se dashboard down: email

MONITORING ERRORI:
Streamlit ha logging built-in
Se errori ripetuti: check logs Streamlit Cloud dashboard

SOSTENIBILITA:
Script automatico riduce carico manuale a review dati nuovi 30 minuti annui
versus precedente check manuale mensile 6 ore annue. Vale investimento


3.5 PARTNERSHIP E ISTITUZIONALIZZAZIONE
----------------------------------------

A questo punto progetto e maturo. Valutare se cercare supporto istituzionale

CRITERI E MOMENTO DI CERCARE PARTNERSHIP:
Dashboard ha oltre 1000 utenti mensili stimato da word-of-mouth
Almeno 5 issue o PR da contributori esterni
Citato in almeno 2 articoli accademici o media qualita
Feedback esperti positivi e contributivi
Motivazione personale ancora alta

POTENZIALI PARTNER:
ISI Foundation Torino: ricerca reti complesse, dati criminalita
Transcrime Universita Cattolica: osservatorio criminalita
ISTAT: collaborazione formalizzata, wishful thinking, difficile
Associazioni giornalismo dati come Ondata

APPROCCIO:
Email fredda: Progetto open source criminalita raggiunto maturita. Interesse
collaborazione. Potrebbe beneficiare visibilita e credibilita versus io mantengo
autonomia decisionale
Proposta: partnership leggera con hosting istituzionale, co-branding, non
assorbimento totale
Red flag: se vogliono controllo editoriale completo, declinare

ALTERNATIVA: Articolo Scientifico
Submit a journal open access come PLOS ONE, Scientific Data, Frontiers
Titolo: Open Data Dashboard for Italian Crime Statistics: Design, Implementation,
and Lessons for Transparency in Sensitive Data Visualization
Sezioni: metodologia, scelte design etico, risultati feedback utenti
Citazione dashboard aumenta credibilita


3.6 GESTIONE COMUNITARIA MATURA
--------------------------------

Progetto ora ha visibilita, serve governance chiara

CONTRIBUTING.md aggiornato:
Contributi benvenuti in: correzioni bug, nuove fonti dati, miglioramenti UX
NON accettiamo: feature che compromettono neutralita, visualizzazioni sensazionalistiche,
disaggregazioni sotto livello provinciale
Decisioni finali: maintainer [nome], discussioni aperte su issue

ROADMAP PUBBLICA con GitHub Projects:
Backlog: feature nice to have come export PDF report, API dati
In Progress: cosa stai lavorando ora
Done: rilasci passati
Trasparenza decisionale: perche X si, Y no

COMUNICAZIONI:
Release notes per ogni aggiornamento dati
Changelog semantico: MAJOR.MINOR.PATCH come v2.0.0 uguale Fase 3 completa
Newsletter opzionale con Substack free per utenti interessati

OUTPUT FASE 3:
Dashboard con dati europei, 9 grafici totali
Automazione aggiornamenti piu monitoring
Dati raw su Zenodo con DOI
Partnership istituzionale o paper scientifico submitted
Roadmap pubblica con governance chiara
Progetto sostenibile 15 euro mensili piu 30 minuti annui manutenzione


================================================================================
SEZIONE 3: METRICHE DI SUCCESSO REALISTICHE
================================================================================

NON MISURARE:
Visite assolute, vanity metric
Condivisioni social, incentiva sensazionalismo

MISURARE INVECE:

FASE 1:
6 piu feedback usabilita positivi su chiarezza
0 feedback sembra di parte
Almeno 1 contributore esterno con issue o PR GitHub

FASE 2:
Feedback positivi da 2 piu esperti criminologia o statistica
Almeno 3 riutilizzi: fork GitHub, citazione blog, uso didattico

FASE 3:
Citazione in 1 piu articolo accademico o report istituzionale
5 piu contributori esterni attivi
Partnership istituzionale o paper pubblicato

OBIETTIVO QUALITATIVO A 18 MESI:
Progetto riconosciuto come esempio metodologico rigoroso visualizzazione dati
sensibili. Utilizzato in almeno 5 contesti educativi o divulgativi. Codice e dati
riutilizzati da altri progetti simili come altri paesi


================================================================================
SEZIONE 4: GESTIONE RISCHI E PIANI B
================================================================================

RISCHIO: Complessita tecnica eccessiva Fase 0
SEGNALE: Oltre 30 ore su Fase 0, frustrazione continua
PIANO B: Pivot a Dataset curato ISTAT criminalita, repo solo dati puliti piu notebook
analisi. Valore alto per community, meno ambizioso
TRIGGER: Fine settimana 3 Fase 0


RISCHIO: Dati ISTAT inaccessibili con paywall o GDPR permanente
SEGNALE: Download impossibile dopo 3 tentativi diversi metodi
PIANO B: Basarsi solo su dati Ministero Interno, meno granulari ma pubblici
TRIGGER: Settimana 2 Fase 1


RISCHIO: Strumentalizzazione politica incontrollabile
SEGNALE: Citato in contesti polarizzanti, attacchi personali, perdita controllo narrativo
PIANO B: Statement pubblico su homepage piu GitHub: Progetto nato con intento scientifico
educativo. Strumentalizzazioni recenti contraddicono principi. Archivio repository
con snapshot finale, codice e dati disponibili ma sviluppo sospeso
TRIGGER: Valutazione caso per caso, priorita benessere personale


RISCHIO: Demotivazione fisiologica dopo 4-6 mesi
SEGNALE: 2 piu settimane senza aprire progetto, pensieri dovrei lavorarci ma non ho voglia
PIANO B: Pausa ufficiale 1-3 mesi. Issue GitHub: Pausa sviluppo, torno [data].
Se dopo pausa motivazione non torna: dichiarare v1.0 completa, no Fase 3
TRIGGER: Auto-onesta su motivazione


RISCHIO: Successo eccessivo, troppa attenzione, richieste, pressione
SEGNALE: Oltre 20 email settimanali, richieste personalizzazioni specifiche, aspettative eccessive
PIANO B: Cercare co-maintainer con issue Help Wanted Co-maintainer o partner istituzionale
che assorba carico. Ultimissima risorsa: archiviare con spiegazione onesta
TRIGGER: Burnout imminente


RISCHIO: Cambiamento normativo dati, ISTAT blocca pubblicazioni, GDPR 2.0
SEGNALE: Dati non piu disponibili per mesi
PIANO B: Documentare problema governance dati Italia, pivot a solo Eurostat o Ministero
Interno. Advocacy pubblica per dati aperti con blog post, petizioni
TRIGGER: 6 piu mesi senza nuovi dati ISTAT


================================================================================
SEZIONE 5: RISORSE E RIFERIMENTI
================================================================================

TUTORIAL TECNICI:
Streamlit: https://docs.streamlit.io/get-started
Plotly Python: https://plotly.com/python/
Pandas: https://pandas.pydata.org/docs/user_guide/
API ISTAT REST: https://developers.italia.it/it/api/istat-rest.html
Eurostat API: https://wikis.ec.europa.eu/display/EUROSTATHELP/API+Statistics

DATI:
ISTAT dati.istat.it nuovo portale versus I.Stat
ISTAT Metadati: https://www.istat.it/it/metodi-e-strumenti/metadati
Eurostat Crime Statistics: https://ec.europa.eu/eurostat/web/crime/database
Ministero Interno: https://www.interno.gov.it/it/stampa-e-comunicazione/dati-e-statistiche

METODOLOGIA:
ISTAT Indagine Vittimizzazione per numero oscuro: cerca ultimo report disponibile
Eurostat Crime Statistics Explained: metodologia confronti internazionali
UN Office on Drugs and Crime: standard internazionali dati criminalita

ETICA VISUALIZZAZIONE:
Data Feminism di D'Ignazio e Klein: capitolo su potere e visualizzazione
How Charts Lie di Alberto Cairo: bias cognitivi grafici
ColorBrewer: https://colorbrewer2.org/ palette accessibili

COMMUNITY:
r/dataisbeautiful: feedback visualizzazioni
Streamlit Community: https://discuss.streamlit.io/
Open Data Italia: forum o Slack per supporto

HOSTING:
Streamlit Cloud: https://streamlit.io/cloud
  Free tier: 1 app pubblica, 1GB RAM, Community support
  Sufficiente: Fase 1-2
  Limiti: sleep dopo inattivita con risveglio circa 30 secondi, no custom domain free

Render: https://render.com
  Free tier: 750 ore mensili, 512MB RAM, sleep dopo 15 minuti inattivita
  Starter: 7 dollari mensili, no sleep, 512MB RAM, custom domain
  Raccomandato: Fase 3 se Streamlit Cloud insufficiente

Railway: https://railway.app
  Hobby: 5 dollari mensili base piu usage, 512MB RAM, 5 dollari credito incluso
  Alternativa: valida a Render, UI piu moderna

Zenodo: https://zenodo.org/ per dati


================================================================================
SEZIONE 6: CHECKLIST PRE-LANCIO COMPLETA
================================================================================

Prima di annunciare pubblicamente dashboard a fine Fase 1, verificare:

CONTENUTI E COMUNICAZIONE
--------------------------
Grafici:
  Tutti titoli neutri: nessun drammatico, allarme, finalmente, smentisce
  Box gialli contestuali sopra ogni grafico presenti e chiari
  Footer fonte sotto ogni grafico con data aggiornamento
  Watermark su grafici: Fonte Osservatorio Criminalita Italia con URL effettivo

Testi:
  Leggere ad alta voce tutte pagine: suonano neutre o di parte
  Test con tool: hemingwayapp.com per leggibilita con target grado 8-10
  Controllo refusi: Grammarly o equivalente

Documentazione:
  docs/methodology.md completa: tutte 8 sezioni presenti
  docs/interpretation_guide.md: FAQ comprensibili a non-statistico
  docs/known_issues.md: onesta su limiti, no nascondere problemi
  README.md: screenshot dashboard, istruzioni install chiare, badge licenze

Link e riferimenti:
  Tutti link fonti ISTAT ed Eurostat funzionanti, verificare manualmente
  Link metadati nazionali Eurostat per ogni paese in Fase 3
  Email contatto funzionante e monitorata

TECNICA
-------
Repository:
  .gitignore configurato: .env, __pycache__, .DS_Store, asterisco.pyc, venv/
  requirements.txt: versioni pinnate come streamlit==1.32.0 non streamlit>=1.0
  Motivo: evitare breaking changes futuri
  Licenze dichiarate: LICENSE file MIT piu docs/LICENSE CC BY 4.0
  CONTRIBUTING.md presente
  CODE_OF_CONDUCT.md presente usa template Contributor Covenant
  Issue templates: .github/ISSUE_TEMPLATE/bug_report.md piu feature_request.md

Codice:
  Commenti inline per logiche complesse, non ovvieta
  Funzioni docstring per riutilizzo
  No credenziali hardcoded anche se dati pubblici, buona pratica
  Logging errori: try except con st.error messaggi user-friendly

Testing:
  Run in virtualenv pulito: pip install -r requirements.txt poi streamlit run src/app.py
  Test 3 browser: Chrome o Chromium, Firefox, Safari o Edge
  Test mobile: almeno iPhone Safari piu Android Chrome, emulatori browser OK
  Performance: homepage carica minore di 5 secondi con connessione media, test WebPageTest
  Accessibilita: contrast checker WCAG AA con webaim.org/resources/contrastchecker/

Deploy:
  App Streamlit Cloud deployata e raggiungibile
  URL personalizzato se possibile come osservatorio-criminalita.streamlit.app
  Secrets configurati se necessari, no secrets in Fase 1 probabilmente
  Logs Streamlit Cloud senza errori critici

ETICA E DESIGN
--------------
Visualizzazioni:
  Scale colori: palette ColorBrewer, nessun rosso uguale pericolo
  Range assi Y: partono da 0 o giustificati se no con annotazione
  Nessuna manipolazione percettiva come assi troncati per esagerare trend

Privacy territoriale:
  Livello minimo: provincia, nessun dato comunale o quartiere
  Mappa: max zoom provincia, no drill-down sotto

Linguaggio:
  Nessuna stigmatizzazione territoriale: Provincia X ha tasso Y OK
  Provincia X e pericolosa NO
  Nessuna inferenza causale: Tasso aumenta OK, Tasso aumenta per colpa Z NO
  Nessuna predizione: no criminalita continuera a...

Test usabilita:
  Completato con 6-8 partecipanti
  Feedback integrato
  Red flags risolti, oltre 50 percento fallisce task uguale problema grave

GOVERNANCE E LEGALE
-------------------
Policy:
  PRIVACY_POLICY.md presente anche se no analytics: Nessun dato raccolto
  Disclaimer footer: Dashboard a scopo informativo ed educativo. Non sostituisce
  analisi criminologiche professionali, consulenza legale, o valutazioni assicurative.
  Dati mostrano criminalita registrata, non totale reale

Licenze dati:
  Attribuzione ISTAT: Dati ISTAT CC BY 3.0 IT elaborati da [progetto]
  Se usi Eurostat: Dati Eurostat CC BY 4.0 elaborati da [progetto]

Contatti:
  Email pubblica funzionante per segnalazioni: osservatorio.criminalita@gmail.com
  o equivalente
  Tempo risposta target: 48-72 ore, dichiararlo

COMUNICAZIONE LANCIO
--------------------
Post annuncio bozza da personalizzare:
Ho creato una dashboard open source per esplorare i dati ufficiali ISTAT sulla
criminalita in Italia. Obiettivo: facilitare comprensione di trend spesso diversi
dalla percezione pubblica, con trasparenza metodologica completa.

Cosa trovi:
3 visualizzazioni interattive con trend nazionale, percezione versus dati, tipologie reato
Documentazione metodologica dettagliata
Codice e dati aperti su GitHub

Cosa NON e:
Uno strumento per dimostrare tesi preconcette
Una classifica sicurezza territori

Feedback costruttivi molto benvenuti, soprattutto su chiarezza e neutralita.

Link: [URL dashboard]
GitHub: [URL repo]

hashtag opendata hashtag dataviz hashtag italia hashtag criminalita hashtag trasparenza

Canali:
  LinkedIn professionale, rete estesa
  Mastodon o Twitter tech community
  Reddit: r/dataisbeautiful con screenshot migliore grafico, r/italy con cautela
  Hacker News: Show HN: Open source crime data dashboard for Italy
  Forum tematici: ondata.it, forum statistici italiani

EVITARE Fase 1:
  Contatto proattivo giornalisti per rischio framing incontrollabile
  Post gruppi Facebook generici per alto rischio flame war
  Claim sensazionalistici tipo La verita sulla criminalita, controproducente


================================================================================
SEZIONE 7: PROSSIMI PASSI IMMEDIATI
================================================================================

OGGI O DOMANI 2 ore
--------------------
1. Decidere nome progetto definitivo
   Opzioni valutate:
   Osservatorio Criminalita Italia neutro, istituzionale
   DatiCrimine Italia diretto, mnemonico
   Italia Crime Data internazionale
   Sconsigliato: Non avere paura, Criminalita Reale, Contro l Allarmismo
   tutti implicano tesi precostituita
   
2. Verificare disponibilita dominio opzionale Fase 1, rinviabile:
   osservatorio-criminalita.it circa 12 euro annui
   daticrimine.it
   Check: https://www.nic.it registro .it

3. Creare repository GitHub:
   Nome repo: coerente con nome progetto lowercase-con-trattini
   Descrizione: Open source dashboard visualizing official crime statistics
   for Italy with methodological transparency
   Inizializzare con: README.md, LICENSE MIT, .gitignore Python template


ENTRO 3 GIORNI 4 ore
---------------------
1. Struttura repository:
   mkdir -p data/{raw,processed,metadata} src/{data_acquisition,data_cleaning,visualizations} docs tests
   touch src/app.py requirements.txt
   touch docs/{methodology.md,interpretation_guide.md,data_sources.md,known_issues.md}

2. README.md iniziale bozza, si espande dopo:
   Titolo progetto
   Descrizione 2-3 righe
   Status: Work in Progress - Fase 0 Prototipazione
   Roadmap: link a questa scaletta copia in docs/roadmap.md
   License: MIT
   Contact: email

3. requirements.txt base:
   streamlit==1.32.0
   plotly==5.18.0
   pandas==2.1.4
   numpy==1.26.3
   requests==2.31.0

4. First commit:
   git init
   git add .
   git commit -m "Initial commit: project structure"
   git branch -M main
   git remote add origin https://github.com/[username]/[repo-name].git
   git push -u origin main


ENTRO 1 SETTIMANA 10 ore totali incluse ore precedenti
-------------------------------------------------------
1. Tutorial Streamlit 3-4 ore:
   Seguire: https://docs.streamlit.io/get-started/tutorials/create-an-app
   Creare app.py Hello World con almeno st.title, st.write, st.line_chart
   Deploy test su Streamlit Cloud: collegare GitHub repo, deploy src/app.py
   Verificare: app raggiungibile pubblicamente

2. Tutorial Plotly 3 ore:
   Seguire: https://plotly.com/python/getting-started/
   Creare in Jupyter Notebook:
     Line chart con dati fittizi
     Bar chart
     Customizzare: titoli, assi, colori, hover tooltips
   Esportare grafici come variabili Python riutilizzabili

3. Esplorazione dati ISTAT 3 ore:
   Navigare: https://dati.istat.it o https://esploradati.istat.it
   Cercare: Delitti denunciati o Justice and Security
   Identificare dataset esatto: codice, nome, anni disponibili
   Download manuale CSV non automatizzare ora: ultimi 10-15 anni, nazionale
   Ispezionare in Excel o LibreOffice: colonne, missing values, formato date
   Documentare in docs/data_sources.md: URL, data download, note


MILESTONE SETTIMANA 1:
Repository GitHub pubblico con struttura
App Streamlit Hello World deployata
Dataset ISTAT identificato e scaricato
Decision: proseguire Fase 0 completa, se si planning dettagliato prossimi 2 settimane


ENTRO 2 SETTIMANE 20 ore totali uguale piu 10 ore questa settimana
--------------------------------------------------------------------
Fase 0 completa come da sezione 2 scaletta:
Grafico Plotly trend nazionale integrato in app.py
Deploy Streamlit con grafico funzionante
docs/methodology.md bozza 300-500 parole
DECISIONE GO o NO-GO Fase 1

Criteri GO:
  Deploy funziona stabilmente
  Grafico leggibile e corretto
  Dati ISTAT accessibili anche se manualmente
  Motivazione ancora alta scala 1-10 almeno 7
  Tempo impiegato accettabile minore di 25 ore per Fase 0

Criteri NO-GO:
  Frustrazione tecnica insostenibile bloccato oltre 10 ore su singolo problema
  Dati ISTAT irreperibili o qualita troppo bassa
  Grafico risultato poco chiaro anche dopo iterazioni
  Motivazione calata minore di 5 su 10
  Realizzazione non e per me o tempo meglio investito altrove

Se NO-GO: nessuna vergogna. Documentare apprendimenti, archiviare repo con README
onesto: Prototipo esplorativo, sviluppo non proseguito. Apprendimenti [lista].
Valore comunque acquisito: tutorial, esperienza deployment, comprensione dati ISTAT

Se GO: celebrare uscita, cena, reward personale, planning dettagliato Fase 1
con Gantt chart settimanale Google Sheets o Notion


================================================================================
SEZIONE 8: DOCUMENT MANAGEMENT META
================================================================================

QUESTA SCALETTA
---------------
File: docs/roadmap.md nel repository
Versioning: committare ogni volta che modifichi dopo decisioni importanti
Formato: Markdown plain text questo file

Update schedule:
  Fine ogni Fase: sezione Lessons Learned con cosa ha funzionato, cosa no
  Ogni 3 mesi: review completa, aggiornare stime temporali se necessario
  Quando cambi scope: documentare razionale come Rimosso feature X perche Y


CHANGELOG PROGETTO
------------------
File: CHANGELOG_PROJECT.md diverso da CHANGELOG.md codice
Formato esempio:

hashtag Changelog Progetto Osservatorio Criminalita Italia

doppio hashtag [Data] - Decisione: Nome Progetto
Scelta finale: [nome]
Razionale: [perche]
Alternative scartate: [lista]

doppio hashtag [Data] - Fase 0 Completata
Ore effettive: X stimate Y
Problemi incontrati: [lista]
Soluzioni trovate: [lista]
Decisione: GO Fase 1

doppio hashtag [Data] - Feedback Esperto [Nome]
Suggerimenti ricevuti: [sintesi]
Integrati: [quali]
Rinviati: [quali, perche]


DECISION LOG
------------
Per decisioni architetturali importanti:
File: docs/decisions/YYYY-MM-DD-titolo-decisione.md

Template ADR Architecture Decision Record:

hashtag [Numero]. [Titolo Decisione]

Data: YYYY-MM-DD
Status: Proposta o Accettata o Deprecata

doppio hashtag Contesto
[Perche dobbiamo decidere]

doppio hashtag Opzioni Valutate
1. Opzione A: [pro contro]
2. Opzione B: [pro contro]

doppio hashtag Decisione
Scelta: [quale]
Razionale: [perche]

doppio hashtag Conseguenze
Positive: [lista]
Negative: [lista]
Rischi: [lista]


Esempio concreto:

hashtag 001. Stack Visualizzazione: Plotly versus Altair

Data: 2026-01-15
Status: Accettata

Contesto: Serve libreria viz per grafici interattivi Streamlit

Opzioni:
1. Plotly: piu features, curva apprendimento media, grande community
2. Altair: dichiarativo, curva bassa, meno features avanzate

Decisione: Plotly
Razionale: Serve customizzazione avanzata tooltips e layout per accessibilita,
Altair limitato. Community Plotly piu Streamlit molto attiva

Conseguenze:
Positivo: Massima flessibilita design
Negativo: Codice piu verboso versus Altair
Rischi: Breaking changes updates Plotly mitigato con pinning versions


BACKUP E CONTINUITA
-------------------
GitHub e backup primario cloud, versionato

Backup locale addizionale:
  Ogni fine settimana: zip completo repository inclusi .git
  Storage: Google Drive o Dropbox personale
  Retention: ultimi 4 backup settimanali

Se succede qualcosa a te incidente, malattia, altro:
  Repository pubblico: chiunque puo forkare e continuare
  Contatto emergenza: dichiarare in README opzionale, personale
  Se inattivo oltre 6 mesi senza avvisi, progetto considerato abbandonato.
  Fork benvenuti, mantenere licenza MIT


================================================================================
SEZIONE 9: FILOSOFIA E MOTIVAZIONE PROMEMORIA PERSONALE
================================================================================

PERCHE QUESTO PROGETTO VALE 8-10 MESI DEL TUO TEMPO
----------------------------------------------------

1. IMPATTO SOCIALE
   Dibattito criminalita in Italia e polarizzato, emotivo, spesso slegato da dati.
   Questo progetto non risolve il problema, ma offre uno spazio neutro dove
   dati parlano senza gridare. Anche se cambia percezione di 100 persone, vale

2. COMPETENZE TECNICHE
   Fine progetto avrai padronanza:
   Streamlit portfolio-ready
   Plotly visualizzazioni professionali
   Pandas data wrangling skill trasferibile
   Git e GitHub workflow collaborativo standard industria
   Deploy e monitoring applicazioni web
   Competenze monetizzabili: data analyst, data journalist, civic tech

3. COMPETENZE TRASVERSALI piu preziose delle tecniche
   Comunicare dati sensibili con neutralita raro, prezioso
   Project management realistico stimare tempi, gestire scope
   Gestire feedback contrastanti stakeholder diversi, prioritizzare
   Documentare per pubblico non-tecnico underrated skill

4. NETWORK E REPUTAZIONE
   Progetto open source ben fatto attira:
   Collaboratori con interessi simili
   Offerte lavoro data journalism, civic tech, PA digitale
   Inviti conferenze se diventa caso studio
   Contatti ricercatori criminologia e statistica interdisciplinare

5. PORTFOLIO
   Questo e portfolio piece che dimostra:
   Technical: fullstack data app
   Domain: comprensione dati complessi, contesto sociale
   Ethics: design responsabile dati sensibili
   Communication: docs chiare, multi-audience
   Mostrabile a: recruiter, clienti freelance, ammissioni master o PhD


QUANDO DUBITARE fisiologico, capita a tutti
--------------------------------------------

Settimana 8: Ho passato 3 ore su un bug stupido, serve davvero
RISPOSTA: Si. Debugging e 50 percento programmazione reale. Pausa caffe, torna dopo

Mese 4: Ho visto progetto simile online, il mio e inutile
RISPOSTA: Il tuo ha focus Italia, metodologia tua, documentazione tua. Non e gara

Mese 6: Nessuno usa dashboard, visualizzazioni basse
RISPOSTA: Metriche vanity. Se 10 persone capiscono meglio dati grazie a te, WIN

Mese 8: Voglio mollare, non finiro mai
RISPOSTA: Opzione 1: pausa 1 mese pianificata, guilt-free
          Opzione 2: dichiarare v0.9 feature complete, v1.0 simbolico
          Opzione 3: trovare co-maintainer issue Help Wanted
          Tutte e tre OK. Meglio progetto 90 percento fatto che 0 percento per perfezionismo


COMPROMESSI ACCETTABILI per finire, non abbandonare
----------------------------------------------------

Se tempi si allungano troppo oltre 12 mesi:
  Saltare Fase 3 Eurostat: v1.0 solo Italia e gia valore enorme
  Ridurre test usabilita: 4 persone invece 8, meglio 4 che 0
  Metodologia good enough: 80 percento rigorosita e sufficiente per progetto civico

Se motivazione cala ma vuoi finire:
  Ridurre frequenza: 5 ore settimanali invece 10, raddoppia tempi ma OK
  Pair programming: coinvolgere amico o amica per sessioni social accountability
  Gamification personale: reward ogni milestone cena fuori, giorno libero


SUCCESSO NON E SOLO FINIRE
---------------------------

Anche se fermi a Fase 1:
  Hai imparato stack completo data app
  Hai pubblicato codice open source
  Hai documentato processo utile ad altri
  Hai capito sfide comunicare dati sensibili

Se arrivi a Fase 3:
  Hai progetto portfolio-quality
  Hai competenze rare etica data viz piu tech
  Hai contribuito dibattito pubblico italiano


IMPATTO A LUNGO TERMINE speculativo ma possibile
-------------------------------------------------

Anno 2: Progetto citato in tesi laurea studente criminologia
Anno 3: Fork per criminalita Spagna o Francia tua arch riutilizzata
Anno 5: Collaborazione con ente ricerca, tuo contributo in paper accademico
Anno 10: Qualcuno ricorda quel sito dati criminalita fatto bene e ti contatta

Non puoi pianificare serendipia, ma puoi creare condizioni: lavoro pubblico,
ben documentato, licenza aperta. Resto e fortuna piu tempo


ULTIMA RIFLESSIONE: ONESTA E FORZA NON DEBOLEZZA
-------------------------------------------------

Questo progetto scommette su idea contro-intuitiva:
Dire Questi dati mostrano X, ma NON mostrano Y, Z. Limiti sono [lista]
e percepito come PIU credibile, non meno

Pubblico e abituato a:
  Media: sensazionalismo, cherry-picking
  Politica: dati usati come armi retoriche
  Advocacy: enfasi solo dati favorevoli a tesi

Tu fai opposto:
Ecco dati. Ecco cosa significano. Ecco cosa NON significano. Ecco limiti.
Decidete voi

E raro. E prezioso. E difficile da strumentalizzare tentano, ma hai
documentazione che smaschera

Questo approccio richiede umilta intellettuale ammettere incertezza e
fiducia nel pubblico trattarli da adulti, non da bambini da proteggere

Non e per tutti. Se lo fai bene, distingue te da 95 percento progetti simili


================================================================================
SEZIONE 10: CONCLUSIONE E COMMITMENT
================================================================================

Hai davanti una scaletta di 8-10 mesi, 330-410 ore totali circa 1 ora al giorno se
distribuita uniformemente, realisticamente piu concentrata weekend o serate

COMMITMENT MINIMO per provare seriamente:
  Fase 0 completa 3 settimane, 30 ore
  Decisione GO o NO-GO onesta basata su criteri definiti
  Se GO: commitment Fase 1 altri 3 mesi, 100-120 ore
  Rivalutazione fine Fase 1: continuare o v1.0 completa

NON commitment:
  Finire tutto a tutti costi burnout garantito
  Perfezione metodologica assoluta impossibile
  Piacere a tutti impossibile al quadrato


FIRMA SIMBOLICA opzionale, per te
----------------------------------
Io [nome] mi impegno a:
  Dedicare tempo onesto a Fase 0 minimo 25 ore in 3 settimane
  Valutare risultati con criteri oggettivi, non emotivi
  Se proseguo, comunicare pubblicamente con trasparenza
  Se abbandono, documentare perche utile ad altri
  Chiedere aiuto quando bloccato community, esperti, forum
  Celebrare milestone, non solo focus su mancanze

Non mi impegno a:
  Finire a tutti costi
  Accontentare critici irragionevoli
  Sacrificare benessere per progetto

Data: [oggi]


PRIMA AZIONE CONCRETA: ORA
---------------------------
Chiudi questo documento
Apri browser
Vai su GitHub
Click New repository
Nome: [scegli ora, 30 secondi]
Inizializza con README
Click Create repository

Primo commit fatto. Progetto iniziato
Resto e Fase 0, hai roadmap

Buon lavoro


================================================================================
APPENDICE: TEMPLATE DECISIONI RICORRENTI
================================================================================

Durante sviluppo affronterai decisioni ricorrenti. Ecco template decision-making

DECISIONE: Aggiungere feature X
DOMANDE:
1. Migliora comprensione dati o e figo ma inutile
2. Compromette neutralita o semplicita
3. Tempo sviluppo stimato versus valore aggiunto
4. Manutenibilita futura quanto complica codebase
5. Richiesta utenti reali o mia supposizione
AZIONE: Se 3 piu risposte negative NO. Se 4 piu positive SI. Altrimenti MAYBE backlog


DECISIONE: Accettare contributo esterno PR
DOMANDE:
1. Codice pulito e testato
2. Documentato adeguatamente
3. Allineato con principi progetto neutralita, trasparenza
4. Contributor ha firmato Code of Conduct
5. Sono disposto a manutenere questa feature long-term
AZIONE: Tutti SI merge. Anche 1 NO richiedi modifiche o declina educatamente


DECISIONE: Rispondere a critica o polemica pubblica
DOMANDE:
1. Critica costruttiva o troll
2. Errore metodologico reale o fraintendimento
3. Rispondere migliora progetto o alimenta flame war
4. Ho energie emotive per gestire thread
AZIONE: Se errore reale ammetti, correggi, ringrazia. Se troll ignora.
         Se fraintendimento singola risposta educata poi disengage


DECISIONE: Cambiare scope progetto come aggiungere dati salute
DOMANDE:
1. Sono ancora appassionato tema criminalita o sto fuggendo da difficolta
2. Nuovo scope ha senso o e scope creep
3. Risorse tempo e competenze sufficienti per gestire entrambi
AZIONE: Se fuga da difficolta NO, affronta problema originale.
        Se genuino interesse piu risorse valutare spin-off separato


================================================================================
APPENDICE: GESTIONE EMOZIONI E BURNOUT
================================================================================

Progetto lungo 8-10 mesi uguale rischio burnout. Strategia prevenzione

SEGNALI PRECOCI BURNOUT:
  Procrastinazione: Lavoro sul progetto piu tardi ripetuto per giorni
  Perdita gioia: task che prima piacevano ora pesano
  Perfezionismo paralizzante: non rilasci nulla perche non e abbastanza buono
  Irritabilita: feedback costruttivi ti infastidiscono
  Pensieri negativi ricorrenti: E inutile, non importa a nessuno

CONTROMISURE IMMEDIATE:
1. PAUSA OBBLIGATORIA: 1-2 settimane zero lavoro progetto. Non opzionale
2. Ridimensionare scope: Fase 2 puo essere completo anche senza Fase 3
3. Condividere peso: cercare co-maintainer o mentorship
4. Rileggere development diary: perche hai iniziato
5. Celebrare vittorie: hai fatto X, e già un successo

PREVENZIONE SISTEMICA:
  1 giorno settimanale ZERO progetto come sabato off sempre
  Ogni 4 settimane: 1 settimana solo manutenzione leggera no nuove feature
  Target realistico: 10 ore settimanali, non 20 ore
  Dire NO a feature creep: backlog diverso da obbligo

REGOLA FINALE: Il progetto serve TE, non viceversa. Se smette di essere
soddisfacente, e ok fermarsi. Hai già imparato e creato valore nel processo.
Meglio progetto incompleto con dignita che burnout totale


================================================================================
NOTA FINALE IMPORTANTE
================================================================================

Questa scaletta e documento VIVO, non comandamenti scolpiti nella pietra

ASPETTATIVE REALISTICHE:
  Almeno 30 percento dei task prendera piu tempo del previsto buffer implicito
  Incontrerai ostacoli non previsti API cambiano, dati mancano, bug strani
  Motivazione oscillera normale, non significa fallimento
  Alcune idee iniziali si riveleranno cattive va bene, impari iterando

USA QUESTA SCALETTA COME:
  Guida generale direction, non checklist rigida
  Reference quando bloccato: Cosa suggerisce scaletta per questo
  Validazione decisioni: E allineato con principi Sezione 0

NON USARLA COME:
  Misura di successo o fallimento arrivare a Fase 1 e già successo
  Obbligo morale devo fare tutto perche l ho scritto
  Bastone per auto-flagellarti sono in ritardo sulla timeline

AGGIORNAMENTI SCALETTA:
Ogni volta che:
  Scopri che stima era completamente sbagliata aggiorna
  Cambi approccio tecnico significativo documenta in scaletta
  Impari lesson importante aggiungi a sezione risorse o retrospettiva
  Ti accorgi di punto critico mancante integra

Crea file docs/SCALETTA_CHANGELOG.md per tracciare modifiche alla scaletta stessa

LIBERTA DI DIVERGERE:
Hai pieno permesso da te stesso di:
  Saltare Fase 3 e dichiarare v1.0 completo dopo Fase 2
  Aggiungere Fase 2.5 non prevista se ha senso
  Cambiare stack tecnico se scopri Streamlit non funziona
  Fermarti dopo Fase 0 se capisci che non fa per te

Non vergognarti di decisioni pragmatiche. Dashboard base ben fatta ha piu valore
di dashboard complessa abbandonata al 60 percento

ULTIMO CONSIGLIO:
Stampa questa scaletta o salva PDF e rileggila ogni 4 settimane. Noterai cose
che al primo passaggio non avevi colto. Sara tua bussola nei momenti di confusione

Quando avrai completato qualunque fase tu ritenga completa, fai retrospettiva
finale e poi considera scrivere blog post o paper su Lessons learned building
sensitive data dashboard alone. Aiuterai altri che vorranno fare percorsi simili


================================================================================
FINE DOCUMENTO
================================================================================

Versione: 2.0 Completa
Data: 2026-01-05
Autore: AI assistant basato su discussione con utente
Licenza: CC BY 4.0 puoi modificare, condividere, attribuendo fonte

Questo documento vivra in docs/roadmap.md del tuo progetto
Aggiornalo. Miglioralo. Fallo tuo

Prossima revisione pianificata: dopo completamento Fase 0