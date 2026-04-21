from utils.models1 import Base
from utils.session import engine
from tratamento import carregar_financial
from sqlalchemy import text

def carregar_csv_rapido():
    print("Iniciando carregamento")

    print("Deletando tabela antiga")
    with engine.connect() as conn:
        conn.execute(text("DROP TABLE IF EXISTS financial_impact CASCADE"))
        conn.commit()

    print("Criando tabela")
    Base.metadata.create_all(engine)
    print("Tabela criada!")

    print("Carregando e tratando CSV")
    df = carregar_financial()

    df.to_sql('financial_impact', engine, if_exists='append', index=False)
    print(f"{len(df)} registros inseridos!")

    print("Concluído")

if __name__ == "__main__":
    carregar_csv_rapido()