from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Dict
import joblib
import pandas as pd

# Inicializa o app FastAPI
app = FastAPI()

# CORS para permitir comunicação entre frontend e backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, troque por domínio específico
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta diretórios estáticos (CSS, JS, imagens)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define onde estão os templates HTML
templates = Jinja2Templates(directory="templates")

# Rota da página inicial
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home/home.html", {"request": request})

# Rota do formulário de previsão
@app.get("/formulario", response_class=HTMLResponse)
async def formulario(request: Request):
    return templates.TemplateResponse("forms/forms.html", {"request": request})

# Carrega modelo e colunas treinadas
try:
    modelo = joblib.load("modelo_rf.pkl")
    colunas_treinadas = joblib.load("colunas_treinadas.pkl")
except Exception as e:
    raise RuntimeError(f"Erro ao carregar modelo ou colunas: {e}")

# Define os dados esperados pela API
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

# Endpoint para predição
@app.post("/prever", response_model=Dict[str, str])
async def prever_obesidade(dados: DadosEntrada):
    if dados.Height <= 0 or dados.Weight <= 0:
        raise HTTPException(status_code=400, detail="Altura e peso devem ser maiores que zero.")

    df = pd.DataFrame([dados.dict()])
    df = pd.get_dummies(df)
    df = df.reindex(columns=colunas_treinadas, fill_value=0)

    resultado = modelo.predict(df)

    return {
        "classificacao_obesidade": resultado[0],
        "modelo": "RandomForest v1.0"
    }
