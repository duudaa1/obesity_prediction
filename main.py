from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
import joblib
import pandas as pd

# Inicializa o app FastAPI
app = FastAPI()

# Permitir chamadas do frontend (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Carrega modelo treinado e colunas esperadas
try:
    modelo = joblib.load("modelo_rf")
    colunas_treinadas = joblib.load("colunas_treinadas.pkl")
except Exception as e:
    raise RuntimeError("Erro ao carregar modelo ou colunas: {}".format(e))

# Classe com os dados esperados
class DadosEntrada(BaseModel):
    Gender: str
    Age: int
    Height: float
    Weight: float
    family_history: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str

@app.post("/prever", response_model=Dict[str, str])
def prever_obesidade(dados: DadosEntrada):
    if dados.Height <= 0 or dados.Weight <= 0:
        raise HTTPException(status_code=400, detail="Altura e peso devem ser maiores que zero.")

    # Converte dados para DataFrame
    df = pd.DataFrame([dados.dict()])

    # Prepara dados para modelo
    df = pd.get_dummies(df)
    df = df.reindex(columns=colunas_treinadas, fill_value=0)

    # Realiza predição
    resultado = modelo.predict(df)

    return {
        "classificacao_obesidade": resultado[0],
        "modelo": "RandomForest v1.0"
    }
