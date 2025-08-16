import requests

OLLAMA_URL = "http://ollama:11434/api/chat"

def ask_ollama(model: str, prompt: str) -> str:
    """
    Invia una richiesta al modello Ollama tramite l'API REST /api/chat
    e restituisce il contenuto della risposta.

    Args:
        model: il nome del modello Ollama (es. "gemma3:1b-it-qat")
        prompt: il testo in linguaggio naturale da convertire in SQL

    Returns:
        Una stringa contenente la risposta generata dal modello.

    Raises:
        ValueError se la risposta è vuota.
        HTTPError se la richiesta fallisce.
    """
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=60)
        response.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Errore nella comunicazione con Ollama: {e}")

    data = response.json()
    content = data.get("message", {}).get("content", "").strip()

    if not content:
        raise ValueError("Risposta vuota da Ollama")

    return content
