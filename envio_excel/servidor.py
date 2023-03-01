import pandas as pd
import sqlalchemy

#variaveis usadas para a conexão do banco
db_name = 'work_LUIZFSF'
schema = 'excel'
db_server = 'SDH-DIE-BD'
driver = 'SQL+Server+Native+Client+11.0'
constring = 'mssql+pyodbc://{}/{}?driver={}'.format(db_server, db_name, driver)

#função para a conexao do banco
def getDbEngine():
    db_engine = sqlalchemy.create_engine(constring, fast_executemany=True, connect_args={'connect_timeout': 10},  echo=True)
    return db_engine

#lendo o arquivo e separando ele por colunas
df = pd.read_csv(r"C:\Users\luizfsf\Desktop\cgu\cgu.csv", sep=';', dtype=str)

#função para a criação da tabela e verificação se existe conteudo nessa tabela
df.to_sql(con=getDbEngine(), schema=schema, name='BolsaCapixaba', if_exists='replace', index=False, chunksize=1000)

chamada = 'SELECT tabela_bolsa.cpf AS cpf_bolsa FROM  work_LUIZFSF.excel.BolsaCapixaba AS Tabela_Bolsa LEFT JOIN db_cpf.dbo.CPF AS tabela_cpf ON tabela_cpf.CPF = Tabela_Bolsa.CPF'

join = pd.read_sql_query(chamada,getDbEngine())

join.head(5)

print(join['CPF'])