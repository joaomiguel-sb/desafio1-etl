#  Financial Impact API

## 📖 Sobre o Projeto

Esta API permite gerenciar e analisar dados de impacto financeiro causado por incidentes de cibersegurança, incluindo:

- Perdas financeiras diretas
- Resgates demandados e pagos
- Custos legais e multas regulatórias
- Pagamentos de seguros
- Análises de maiores perdas

---

## Instalação

### Clone o repositório (ou baixe os arquivos)

```bash
git clone https://github.com/seu-usuario/financial-impact-api.git
cd financial-impact-api
```

### Crie um ambiente virtual (recomendado)

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

### Instale as dependências

```bash
pip install -r requirements.txt
```

---

### Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:
```env
DATABASE_URL=postgresql://postgres:SUA_SENHA@localhost:5432/financial_db

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

## Carregando Dados

### 1. Coloque seu arquivo CSV

Coloque o arquivo `financial_impact.csv` na pasta `df/`

### 2. Execute o script de carregamento

```bash
python carregar_dados.py
```

---

## Executando a API

### Iniciar o servidor

```bash
uvicorn main:app --reload
```
Acesse: http://127.0.0.1:8000

---

## 📖 Documentação da API

A API possui documentação interativa automática:

### Swagger UI (Recomendado)
```
http://127.0.0.1:8000/docs
```
