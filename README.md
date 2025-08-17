Modulo per la consegna del progetto finale BASE, non usare per la consegna del progetto personalizzato. Vi prego di leggere con attenzione le istruzioni. 

Dovete inviare un solo form per ogni gruppo.

Dovete consegnare un unico file .zip chiamato matricola1_matricola2_matricola3_lab_prog_prova_finale.zip
che contiene tutto il vostro codice e tutto il necessario per l'esecuzione e dovete scrivere nome cognome e matricola di tutti i partecipanti nel file pdf del report.

Se siete solo in due: matricola1_matricola2_lab_prog_prova_finale.zip

Ricordate di testare il progetto all'interno di un dual boot Ubuntu o di una macchina virtuale Ubuntu con le seguenti versioni software:

(base) riccardo@riccardo-Aspire-A317-51G:~$ lsb_release -a
No LSB modules are available.
Distributor ID:    Ubuntu
Description:    Ubuntu 22.04.5 LTS
Release:    22.04
Codename:    jammy
(base) riccardo@riccardo-Aspire-A317-51G:~$ python3 --version
Python 3.8.8
(base) riccardo@riccardo-Aspire-A317-51G:~$ docker --version
Docker version 28.0.4, build b8034c0
(base) riccardo@riccardo-Aspire-A317-51G:~$ docker compose version
Docker Compose version v2.34.0

(Notate lo spazio tra "docker" e "compose")

Se anche avete sviluppato tutto il vostro progetto in Ubuntu, e se anche lo avete sviluppato interamente con le versioni software che vedete sopra, vi chiedo in ogni caso di munirvi di un dual boot del tutto nuovo o di una macchina virtuale del tutto nuova per il test finale, questo vi darà la certezza che il test funzionerà anche sul mio PC evitando problemi strani come ad esempio path assoluti o variabili d'ambiente o configurazioni di Docker peculiari del vostro sistema.

NON potete fare il test finale in MacOS né con WSL (Windows Subsystem for Linux) dato che questi potrebbero essere incompatibili con Ubuntu.

Ricordate che prima di eseguire il test finale non potete effettuare update del software se non quelle richieste per l'installazione della versione di Docker richiesta, non potete toccare la UI di Docker Desktop, non potete effettuare comandi che non siano il processo di installazione di Docker e Docker compose e non potete modificare le variabili d'ambiente, dato che questo romperebbe la riproducibilità.

Ponete quindi il vostro progetto nel nuovo dual boot Ubuntu o nella nuova macchina virtuale ed eseguite  il comando "sudo chmod 0777 -R ." da dentro la cartella del vostro progetto, allo stesso livello del file di configurazione del docker compose, assicurandovi che la cartella "mariadb_data" abbia acquisito i permessi corretti (altrimenti avete messo la cartella "mariadb_data" nel posto sbagliato), ed eseguite "sudo docker compose up --build" aspettate il tempo necessario per l'avvio completo ed eseguite lo script di testing ufficiale (usando python3) con il numero giusto di componenti del gruppo come argomento da linea di comando prima di consegnare e includete il vostro report.pdf nella cartella zip insieme al vostro codice tutto il necessario per l'esecuzione. Vi chiedo per gentilezza (non necessario) di esporre il frontend sulla porta 8004

Ricordate che il test automatico modifica il database quando si esegue, quindi dovete consegnare la cartella con il database così come era prima dell'esecuzione del test.

Per motivi di limitazioni di spazio di archiviazione non potete superare 1 GB, quindi, se necessario, testate che il vostro progetto funzioni scaricando i modelli da internet in modo automatico al momento dell'avvio. Il progetto quindi deve funzionare così com'è al momento della consegna senza richiedere che i modelli Large Language Model vengano scaricati a mano.

Una volta inviato il form, la consegna è finale e non può essere cambiata. Ricontrollate che il file sia quello corretto e che il database sia nello stato corretto (per esempio ricordate che eseguire il test automatico modifica il database). Le scadenze per le rispettive sessioni sono riportate su Google Classroom, tutte alle ore 23:59
