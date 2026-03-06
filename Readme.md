# 💰 Financial Impact API

API REST para análise de impacto financeiro de incidentes de cibersegurança.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-blue.svg)](https://www.postgresql.org/)

---

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Carregando Dados](#carregando-dados)
- [Executando a API](#executando-a-api)
- [Documentação da API](#documentação-da-api)
- [Endpoints](#endpoints)
- [Exemplos de Uso](#exemplos-de-uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Deploy](#deploy)
- [Troubleshooting](#troubleshooting)

---

## 📖 Sobre o Projeto

Esta API permite gerenciar e analisar dados de impacto financeiro causado por incidentes de cibersegurança, incluindo:

- 💸 Perdas financeiras diretas
- 🔐 Resgates demandados e pagos
- ⚖️ Custos legais e multas regulatórias
- 🛡️ Pagamentos de seguros
- 📊 Análises de maiores perdas

---

## 🚀 Tecnologias

- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido
- **[PostgreSQL](https://www.postgresql.org/)** - Banco de dados relacional
- **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM Python
- **[Pydantic](https://docs.pydantic.dev/)** - Validação de dados
- **[Pandas](https://pandas.pydata.org/)** - Processamento de dados
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.8+** ([Download](https://www.python.org/downloads/))
- **PostgreSQL 13+** ([Download](https://www.postgresql.org/download/))
- **pip** (gerenciador de pacotes Python)
- **Git** (opcional, para clonar o repositório)

### Verificar instalações:

```bash
python --version
# Python 3.10.0 (ou superior)

psql --version
# psql (PostgreSQL) 13.0 (ou superior)

pip --version
# pip 21.0 (ou superior)
```

---

## ⚙️ Instalação

### 1. Clone o repositório (ou baixe os arquivos)

```bash
git clone https://github.com/seu-usuario/financial-impact-api.git
cd financial-impact-api
```

### 2. Crie um ambiente virtual (recomendado)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 🔧 Configuração

### 1. Criar banco de dados PostgreSQL

**Opção A - Local:**

```bash
# Conecte ao PostgreSQL
psql -U postgres

# Crie o banco
CREATE DATABASE financial_db;

# Saia
\q
```

**Opção B - Render (Cloud):**

1. Acesse [render.com](https://render.com)
2. Crie uma conta (grátis)
3. New → PostgreSQL
4. Name: `financial-impact-db`
5. Database: `financial_db`
6. Region: escolha o mais próximo
7. Plan: **Free**
8. Create Database
9. Copie a **External Database URL**

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

**Para banco local:**
```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/financial_db
```

**Para Render:**
```env
DATABASE_URL=postgres://usuario:senha@host.render.com/financial_db
```

⚠️ **Importante:** Substitua `SUA_SENHA`, `usuario`, `senha`, e `host` pelos seus valores reais!

### 3. Estrutura de pastas

Certifique-se de que seu projeto está assim:

```
financial-impact-api/
├── df/
│   └── financial_impact.csv    # Seus dados
├── utils/
│   ├── __init__.py
│   ├── models1.py               # Modelos SQLAlchemy
│   └── session.py               # Conexão com banco
├── .env                         # Variáveis de ambiente
├── main.py                      # API FastAPI
├── carregar_dados.py            # Script ETL
├── requirements.txt             # Dependências
└── README.md                    # Este arquivo
```

---

## 📊 Carregando Dados

### 1. Coloque seu arquivo CSV

Coloque o arquivo `financial_impact.csv` na pasta `df/`

### 2. Execute o script de carregamento

```bash
python carregar_dados.py
```

**Saída esperada:**
```
🚀 Iniciando carregamento...
📋 Criando tabela com SQLAlchemy...
   ✅ Tabela criada com coluna ID!
📊 Lendo financial_impact.csv...
   📄 150 linhas encontradas
💾 Inserindo dados...
   ⏳ 50 registros inseridos...
   ⏳ 100 registros inseridos...
   ⏳ 150 registros inseridos...
   ✅ 150 registros inseridos com sucesso!
✅ Carregamento concluído!
```

---

## 🚀 Executando a API

### Iniciar o servidor

```bash
uvicorn main:app --reload
```

**Parâmetros:**
- `--reload` - Reinicia automaticamente ao editar código (dev only)
- `--host 0.0.0.0` - Aceita conexões externas
- `--port 8000` - Porta customizada

### Verificar se está rodando

Você deve ver:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using WatchFiles
INFO:     Started server process [67890]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

✅ **API rodando!** Acesse: http://127.0.0.1:8000

---

## 📖 Documentação da API

A API possui documentação interativa automática:

### Swagger UI (Recomendado)
```
http://127.0.0.1:8000/docs
```

### ReDoc (Alternativo)
```
http://127.0.0.1:8000/redoc
```

---

## 🛠️ Endpoints

### Resumo

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Página inicial |
| GET | `/financial/` | Listar todos os incidentes |
| GET | `/financial/{incident_id}` | Buscar incidente por ID |
| POST | `/financial/` | Criar novo incidente |
| PUT | `/financial/{incident_id}` | Atualizar incidente |
| DELETE | `/financial/{incident_id}` | Deletar incidente |
| GET | `/financial/loss/top` | Top N maiores perdas |

---

### Detalhamento

#### 1. Listar todos os incidentes

```http
GET /financial/
```

**Query Parameters:**
- `skip` (int, opcional): Número de registros para pular (default: 0)
- `limit` (int, opcional): Máximo de registros a retornar (default: 100)

**Exemplo:**
```bash
curl http://127.0.0.1:8000/financial/?skip=0&limit=10
```

**Resposta (200 OK):**
```json
[
  {
    "id": 1,
    "incident_id": "2021-0508-001",
    "direct_loss_usd": 12600000.0,
    "total_loss_usd": 24642595.67
  },
  ...
]
```

---

#### 2. Buscar incidente por ID

```http
GET /financial/{incident_id}
```

**Exemplo:**
```bash
curl http://127.0.0.1:8000/financial/2021-0508-001
```

**Resposta (200 OK):**
```json
{
  "id": 1,
  "incident_id": "2021-0508-001",
  "direct_loss_usd": 12600000.0,
  "total_loss_usd": 24642595.67
}
```

**Erro (404 Not Found):**
```json
{
  "detail": "Incident not found"
}
```

---

#### 3. Criar novo incidente

```http
POST /financial/
```

**Request Body:**
```json
{
  "incident_id": "2026-TEST-001",
  "direct_loss_usd": 1000000.0,
  "ransom_demanded_usd": 500000.0,
  "total_loss_usd": 1500000.0,
  "notes": "Teste de criação"
}
```

**Exemplo:**
```bash
curl -X POST http://127.0.0.1:8000/financial/ \
  -H "Content-Type: application/json" \
  -d '{
    "incident_id": "2026-TEST-001",
    "total_loss_usd": 1000000.0
  }'
```

**Resposta (201 Created):**
```json
{
  "id": 151,
  "incident_id": "2026-TEST-001",
  "direct_loss_usd": null,
  "total_loss_usd": 1000000.0
}
```

**Erro (400 Bad Request):**
```json
{
  "detail": "Incident ID '2026-TEST-001' já existe!"
}
```

---

#### 4. Atualizar incidente

```http
PUT /financial/{incident_id}
```

**Request Body:**
```json
{
  "incident_id": "2026-TEST-001",
  "direct_loss_usd": 2000000.0,
  "notes": "Atualizado - perda maior"
}
```

**Exemplo:**
```bash
curl -X PUT http://127.0.0.1:8000/financial/2026-TEST-001 \
  -H "Content-Type: application/json" \
  -d '{
    "incident_id": "2026-TEST-001",
    "direct_loss_usd": 2000000.0
  }'
```

**Resposta (200 OK):**
```json
{
  "id": 151,
  "incident_id": "2026-TEST-001",
  "direct_loss_usd": 2000000.0,
  "total_loss_usd": 1000000.0
}
```

---

#### 5. Deletar incidente

```http
DELETE /financial/{incident_id}
```

**Exemplo:**
```bash
curl -X DELETE http://127.0.0.1:8000/financial/2026-TEST-001
```

**Resposta (200 OK):**
```json
{
  "message": "Incident 2026-TEST-001 deleted successfully"
}
```

---

#### 6. Top maiores perdas

```http
GET /financial/loss/top
```

**Query Parameters:**
- `limit` (int, opcional): Número de resultados (default: 10)

**Exemplo:**
```bash
curl http://127.0.0.1:8000/financial/loss/top?limit=5
```

**Resposta (200 OK):**
```json
[
  {
    "id": 3,
    "incident_id": "2023-0115-001",
    "total_loss_usd": 71616414.97
  },
  {
    "id": 1,
    "incident_id": "2021-0508-001",
    "total_loss_usd": 24642595.67
  },
  ...
]
```

---

## 💻 Exemplos de Uso

### Python (requests)

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

# Listar todos
response = requests.get(f"{BASE_URL}/financial/")
incidents = response.json()
print(f"Total: {len(incidents)}")

# Criar novo
novo = {
    "incident_id": "2026-EXEMPLO-001",
    "total_loss_usd": 5000000.0
}
response = requests.post(f"{BASE_URL}/financial/", json=novo)
print(response.status_code)  # 201

# Buscar por ID
response = requests.get(f"{BASE_URL}/financial/2026-EXEMPLO-001")
incidente = response.json()
print(incidente)

# Atualizar
atualizado = {
    "incident_id": "2026-EXEMPLO-001",
    "notes": "Atualizado via Python"
}
response = requests.put(f"{BASE_URL}/financial/2026-EXEMPLO-001", json=atualizado)

# Deletar
response = requests.delete(f"{BASE_URL}/financial/2026-EXEMPLO-001")
print(response.json())  # {"message": "...deleted successfully"}
```

### JavaScript (fetch)

```javascript
const BASE_URL = "http://127.0.0.1:8000";

// Listar todos
fetch(`${BASE_URL}/financial/`)
  .then(res => res.json())
  .then(data => console.log(data));

// Criar novo
fetch(`${BASE_URL}/financial/`, {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({
    incident_id: "2026-JS-001",
    total_loss_usd: 3000000.0
  })
})
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## 📁 Estrutura do Projeto

```
financial-impact-api/
├── df/
│   └── financial_impact.csv        # Dados brutos (CSV)
│
├── utils/
│   ├── __init__.py                 # Marca pasta como módulo Python
│   ├── models1.py                  # Modelos SQLAlchemy (tabelas)
│   └── session.py                  # Conexão com PostgreSQL
│
├── .env                            # Variáveis de ambiente (NÃO COMMITAR!)
├── .gitignore                      # Arquivos ignorados pelo Git
├── carregar_dados.py               # Script ETL (CSV → PostgreSQL)
├── main.py                         # API FastAPI
├── README.md                       # Documentação do projeto
└── requirements.txt                # Dependências Python
```

---

## 🌐 Deploy

### Deploy no Render (Grátis)

1. **Crie conta no Render:** https://render.com

2. **Configure PostgreSQL:** (já feito na seção Configuração)

3. **Deploy da API:**
   - New → Web Service
   - Connect GitHub repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Add Environment Variable: `DATABASE_URL` (copie do PostgreSQL)

4. **Acesse sua API:**
   ```
   https://seu-app.onrender.com/docs
   ```

---

## 🐛 Troubleshooting

### Problema: `ModuleNotFoundError: No module named 'fastapi'`

**Solução:**
```bash
pip install -r requirements.txt
```

---

### Problema: `DATABASE_URL não encontrada`

**Solução:**
- Verifique se criou o arquivo `.env`
- Verifique se a URL está correta
- Certifique-se de estar na pasta do projeto

---

### Problema: `column financial_impact.id does not exist`

**Solução:**
```bash
# Recarregue os dados corretamente
python carregar_dados.py
```

---

### Problema: API não abre no navegador

**Solução:**
```bash
# Tente outra porta
uvicorn main:app --reload --port 5000

# Acesse: http://127.0.0.1:5000/docs
```

---

### Problema: Erro de conexão com Render

**Solução:**
- Verifique se copiou a **External Database URL**
- Adicione `?sslmode=require` no final da URL se necessário

---

## 📄 Licença

Este projeto é de código aberto para fins educacionais.

---

## 👤 Autor

Desenvolvido como projeto de aprendizado em FastAPI e PostgreSQL.

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se livre para:

1. Fork o projeto
2. Criar uma branch (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abrir um Pull Request

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique a seção [Troubleshooting](#troubleshooting)
2. Consulte a [documentação do FastAPI](https://fastapi.tiangolo.com/)
3. Abra uma issue no repositório

---

**🎉 Pronto! Sua API está funcionando!**

Acesse http://127.0.0.1:8000/docs e comece a testar! 🚀