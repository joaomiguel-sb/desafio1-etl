import pandas as pd
from utils.models1 import Base, FinancialImpact
from utils.session import engine
from sqlalchemy import text

def carregar_csv_rapido():
    print("Iniciando carregamento")
    
    # 1. Deletar tabela antiga
    print("Deletando tabela antiga")
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS financial_impact CASCADE"))
        conn.commit()
    
    # 2. Criar tabela com SQLAlchemy (com coluna id)
    print("Criando tabela")
    Base.metadata.create_all(engine)
    print("Tabela criada!")
    
    # 3. Ler CSV
    print("Carregando CSV")
    df = pd.read_csv('df/financial_impact.csv')
    
    # 4. IMPORTANTE: Pandas to_sql com if_exists='append'
    # (append não recria tabela, só adiciona dados)
    df.to_sql('financial_impact', engine, if_exists='append', index=False)
    print(f"{len(df)} registros inseridos!")
    
    print("Concluído")

if __name__ == "__main__":
    carregar_csv_rapido()