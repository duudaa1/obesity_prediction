# Obesity Prediction Web App

Este projeto é uma aplicação web que realiza a predição do nível de obesidade de um indivíduo com base em hábitos alimentares, atividades físicas e características pessoais. O modelo utilizado foi treinado com Random Forest e exposto via API FastAPI. O frontend HTML envia os dados para a API e exibe a classificação prevista.

## 🔧 Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** para a API backend
- **Joblib** para carregar o modelo treinado
- **HTML + JavaScript** puro no frontend
- **CSS** para estilização (opcional)

## 📁 Estrutura do Projeto

obesit-predict/
├── app.py # Servidor FastAPI
├── modelo_rf # Modelo treinado (joblib)
├── colunas_treinadas.pkl # Lista de colunas esperadas pelo modelo
├── templates/
│ ├── css/
│ │ └── style.css # Estilo (opcional)
│ ├── js/
│ │ └── script.js # JS para consumir a API
│ └── forms.html # Formulário de entrada
└── README.md # Este arquivo

## ▶️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone <url-do-repo>
cd obesit-predict
```
### 2. Instale as dependências
bash
Copiar
Editar
pip install fastapi uvicorn pandas joblib
### 3. Inicie o servidor backend
bash
Copiar
Editar
uvicorn app:app --reload
Servidor rodando em: http://127.0.0.1:8000

### 4. Acesse o frontend
Abra o arquivo forms.html no navegador (clicando 2x ou via Live Server do VS Code).

📬 Endpoint da API
POST /prever
Recebe os dados de entrada e retorna a classificação prevista:

Corpo da requisição (JSON):
json
Copiar
Editar
{
  "Gender": "Male",
  "Age": 23,
  "Height": 1.75,
  "Weight": 80,
  "family_history": "yes",
  "FAVC": "yes",
  "FCVC": 2,
  "NCP": 3,
  "CAEC": "Sometimes",
  "SMOKE": "no",
  "CH2O": 2,
  "SCC": "no",
  "FAF": 1,
  "TUE": 2,
  "CALC": "Sometimes",
  "MTRANS": "Public_Transportation"
}
Resposta esperada:
json
Copiar
Editar
{
  "classificacao_obesidade": "Overweight_Level_I"
}
💡 Observações
Certifique-se de que o modelo (modelo_rf) e a lista de colunas (colunas_treinadas.pkl) estão salvos corretamente.

Os campos devem ter exatamente os nomes esperados pela API (case-sensitive).

A transformação get_dummies usada na predição deve ser igual à utilizada durante o treinamento do modelo.

📄 Licença
Este projeto é educacional e livre para uso acadêmico.

Desenvolvido por Equipe 06 — IA e DataScience 🧠

yaml
Copiar
Editar

---

Se quiser, posso gerar esse `README.md` como um arquivo `.md` real e te entregar compactado com os demais arquivos do projeto. Deseja isso?






