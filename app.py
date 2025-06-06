from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

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

# Carregar modelo treinado e colunas esperadas
modelo = joblib.load("modelo_rf")
colunas_treinadas = joblib.load("colunas_treinadas.pkl")

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

@app.post("/prever")
def prever_obesidade(dados: DadosEntrada):
    df = pd.DataFrame([dados.dict()])
    df = pd.get_dummies(df)
    df = df.reindex(columns=colunas_treinadas, fill_value=0)
    resultado = modelo.predict(df)
    return {"classificacao_obesidade": resultado[0]}
