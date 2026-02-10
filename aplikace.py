from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI(title="Maturitní Toolbox", version="1.0")

# --- DATOVÉ MODELY (Pydantic) ---

# Definujeme, jak má vypadat JSON, který nám přijde (Validace dat)

class StudentData(BaseModel):
    jmeno: str
    prijmeni: str
    znamky: List[int]
    absence_hodiny: int = 0 # Výchozí hodnota je 0

# --- ENDPOINTY (Funkce API) ---

@app.get("/")
def home():
    """Základní test funkčnosti."""
    return {"status": "running", "docs_url": "/docs"}

# ÚLOHA A: Faktoriál (Maturitní okruh 6 - Cykly)

@app.get("/math/factorial/{cislo}")
def vypocet_faktorialu(cislo: int):
    """
    Vypočítá faktoriál zadaného čísla.
    Validace: Číslo nesmí být záporné a větší než 20 (aby server nespadl).
    """
    if cislo < 0:
        raise HTTPException(status_code=400, detail="Faktoriál nelze počítat ze záporných čísel.")
    if cislo > 20:
        raise HTTPException(status_code=400, detail="Číslo je příliš velké.")
    vysledek = 1
    for i in range(1, cislo + 1):
        vysledek *= i
    return {"vstup": cislo, "vysledek": vysledek}

# ÚLOHA B: Analýza prospěchu (Maturitní okruh 12 - Podmínky a 18 - JSON)
@app.post("/school/analyze")
def analyza_studenta(student: StudentData):
    """
    Přijme JSON se studentem, vypočítá průměr a rozhodne, zda prospěl.
    """
    if not student.znamky:
        return {"chyba": "Student nemá žádné známky"}

    prumer = sum(student.znamky) / len(student.znamky)
    prospel = prumer <= 4.4 and 5 not in student.znamky

    return {
        "student": f"{student.jmeno} {student.prijmeni}",
        "prumer": round(prumer, 2),
        "prospel": prospel,
        "absence_problem": student.absence_hodiny > 100
    }

# Spuštění (pouze pro lokální debug):

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)