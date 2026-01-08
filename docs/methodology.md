# Metodologia

## Fonti dei dati

I dati provengono dal portale ufficiale ISTAT (dati.istat.it), sezione "Giustizia e sicurezza":

1. **Delitti denunciati dalle forze di polizia all'autorità giudiziaria** (periodo 2014-2023)
   - 56 tipologie di reato dettagliate
   - Dato nazionale aggregato per anno
   
2. **Percezione di sicurezza delle famiglie** - Indagine Multiscopo ISTAT (2014-2023)
   - Indicatore: "Famiglie per presenza di alcuni problemi nella zona in cui abitano: rischio di criminalità: molto e abbastanza"
   - Espresso in percentuale di famiglie che percepiscono rischio

3. **Popolazione residente** - ISTAT
   - Ricostruzione intercensuaria 2002-2019
   - POSAS (Popolazione residente al 1° gennaio) 2020-2023

## Cosa rappresentano i dati

### Denunce vs Crimini

I numeri mostrati rappresentano le **denunce** registrate dalle forze di polizia (Polizia di Stato, Carabinieri, Guardia di Finanza, ecc.) e trasmesse all'autorità giudiziaria. Una denuncia viene registrata quando:

- Una persona si presenta per denunciare un reato
- Le forze dell'ordine rilevano direttamente un reato (es. durante controlli)
- Emerge un reato da indagini in corso

### Percezione di sicurezza

Il dato sulla percezione proviene da indagine campionaria ISTAT Multiscopo su famiglie italiane. Misura la **percezione soggettiva** di insicurezza nella zona di residenza, non l'esperienza diretta di vittimizzazione.

## Cosa NON rappresentano

I dati NON mostrano:

- **Crimini realmente commessi**: molti reati non vengono denunciati (es. furti minori, violenze domestiche). Il tasso di denuncia varia per tipo di reato.
- **Crimini accertati**: una denuncia non implica che il reato sia confermato o che ci sia un colpevole.
- **Condanne**: il dato è indipendente dall'esito processuale.
- **Sicurezza oggettiva**: la percezione di insicurezza risponde a fattori molteplici (copertura mediatica, degrado urbano, fiducia istituzionale) non sempre correlati con i dati registrati.

## Limiti metodologici

### Numero oscuro

La differenza tra reati commessi e reati denunciati (il "numero oscuro") varia significativamente:

- **Furti auto**: ~90% denunciati (necessità assicurativa)
- **Violenze domestiche**: ~80% NON denunciati (paura, vergogna, dipendenza economica)
- **Truffe minori**: ~60% NON denunciati (rassegnazione, cifre basse)

Il numero oscuro varia nel tempo: un aumento delle denunce può indicare maggiore propensione a denunciare (positivo), non necessariamente più reati.

### Cambiamenti normativi

Nuove leggi possono modificare:
- Cosa costituisce reato (es. reati informatici emersi con digitalizzazione)
- Modalità di registrazione (es. GDPR 2018 limita pubblicazione dati disaggregati)
- Pene (es. depenalizzazioni modificano classificazione)

### Propensione a denunciare

La propensione a denunciare varia per:
- **Fattori culturali**: stigma sociale (es. violenze sessuali)
- **Fiducia nelle istituzioni**: campagne sensibilizzazione aumentano denunce
- **Gravità del reato**: crimini gravi più probabilmente denunciati
- **Utilità pratica**: denunce per assicurazione vs rassegnazione per piccoli furti

**Esempio critico**: l'aumento delle denunce per violenze sessuali (+49.7% dal 2014 al 2023) riflette principalmente l'effetto di campagne come #MeToo e maggiore fiducia nelle autorità, NON necessariamente un aumento delle violenze reali. Questo è un risultato positivo: il numero oscuro si sta riducendo.

### Anno di riferimento

È l'anno della denuncia, non necessariamente dell'evento criminoso. Reati scoperti anni dopo (es. truffe complesse) vengono registrati nell'anno della denuncia.

## Normalizzazione per popolazione

Tutti i tassi sono calcolati per abitanti per permettere confronti temporali corretti:

- **Tasso per 1000 abitanti**: usato per categorie frequenti (furti, totale delitti)
- **Tasso per 100.000 abitanti**: usato per reati rari (omicidi, violenze sessuali)

Formula: `Tasso = (Numero delitti / Popolazione) × 1000 (o 100.000)`

La normalizzazione è essenziale perché la popolazione italiana è diminuita da 60.3 milioni (2014) a 59.0 milioni (2023).

## Categorie di reato

### Aggregazione in macro-categorie

I 56 tipi di delitto ISTAT sono stati aggregati in 6 macro-categorie per leggibilità:

1. **Furti**: tutti i furti (con strappo, destrezza, abitazioni, auto, moto, esercizi commerciali, ecc.)
2. **Rapine**: rapine in abitazione, banca, uffici postali, esercizi commerciali, pubblica via
3. **Violenze contro la persona**: omicidi (tutti i tipi), tentati omicidi, percosse, lesioni, minacce, sequestri, ingiurie, violenze sessuali, atti con minori, sfruttamento prostituzione
4. **Truffe e Frodi**: truffe informatiche, delitti informatici, contraffazione marchi, violazione proprietà intellettuale
5. **Droga**: normativa stupefacenti
6. **Altro**: danneggiamenti, incendi, criminalità organizzata (mafia, riciclaggio, usura, estorsioni), ricettazione, contrabbando

### Reati ad alto allarme sociale

Per il focus su reati mediatici, sono stati selezionati 6 tipi specifici (non aggregati):

- Omicidi volontari consumati
- Tentati omicidi
- Violenze sessuali
- Atti sessuali con minorenne
- Rapine in abitazione
- Sequestri di persona

Questi reati rappresentano <2% dei delitti totali ma dominano percezione pubblica e copertura mediatica.

## Indicatore di sicurezza percepita vs oggettiva

I delitti denunciati sono più un indicatore dell'**attività delle forze dell'ordine** e della **propensione a denunciare** che della criminalità effettiva. Un aumento delle denunce può riflettere:

- Maggiore efficienza nel rilevare reati
- Maggiore fiducia dei cittadini
- Reale aumento della criminalità

Non è possibile distinguere tra queste cause senza analisi aggiuntive.

Il **divario tra percezione e dati registrati** è documentato e normale. La percezione di insicurezza risponde a:

- Copertura mediatica (focus su crimini violenti anche se rari)
- Degrado urbano visibile (indipendente da crimini denunciati)
- Sfiducia istituzionale generale
- Esperienza personale o di conoscenti
- Narrazioni politiche

Questi fattori sono legittimi e non rendono la percezione "sbagliata". Il progetto mira a visualizzare questa differenza senza giudizi di valore.

## Trasparenza

Questo progetto non afferma di mostrare "la criminalità in Italia", ma solo i dati ufficiali sulle denunce e sulla percezione, con piena consapevolezza dei limiti. L'obiettivo è facilitare la comprensione del divario tra percezione pubblica e dati registrati, non di dimostrare una tesi precostituita.

Tutti i dati raw, script di elaborazione e codice sorgente della dashboard sono disponibili pubblicamente su GitHub: https://github.com/AlbGri/osservatorio-criminalita-italia