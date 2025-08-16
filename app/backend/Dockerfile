# Usa un'immagine base Python leggera basata su Alpine
FROM python:3.10-alpine

# Aggiorna l'elenco dei pacchetti e installa le dipendenze di sistema necessarie
RUN apk update && \
    apk add --no-cache \
      gcc \
      musl-dev \
      mariadb-connector-c-dev

# Imposta la directory di lavoro a /backend (usando il percorso assoluto)
WORKDIR /app

# Copia il file di requirements e installa le dipendenze Python
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia il codice sorgente all'interno del container
COPY src/ ./src/

# Espone la porta configurata per FastAPI
EXPOSE 8003

# Comando per avviare l'applicazione con Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8003"]
