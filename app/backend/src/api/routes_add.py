from fastapi import APIRouter, HTTPException
from src.models.schema import AddLine
from src.core.db import get_connection
import mariadb  

router = APIRouter()

@router.post("/add")
def add_data(entry: AddLine):
    fields = entry.data_line.split(",")
    if len(fields) != 7:
        raise HTTPException(
            status_code=422,
            detail="Formato non valido. Attesi 7 campi separati da virgola."
        )

    titolo, regista, eta_autore_str, anno_str, genere, piattaforma_1, piattaforma_2 = fields

    # ✅ Validazione numerica
    try:
        eta_autore = int(eta_autore_str)
        anno = int(anno_str)
    except ValueError:
        raise HTTPException(
            status_code=422,
            detail="eta_autore e anno devono essere numeri interi."
        )


    if not titolo.strip() or not regista.strip() or not genere.strip():
        raise HTTPException(
            status_code=422,
            detail="Campi obbligatori vuoti: titolo, regista e genere non possono essere vuoti."
        )

    try:
        conn = get_connection()
        cur = conn.cursor()
        query = """
            INSERT INTO movies (titolo, regista, eta_autore, anno, genere, piattaforma_1, piattaforma_2)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(query, (titolo, regista, eta_autore, anno, genere, piattaforma_1, piattaforma_2))
        conn.commit()
        cur.close()
        conn.close()
        return {"status": "ok"}

    except mariadb.DataError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Errore di formato nei dati: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
