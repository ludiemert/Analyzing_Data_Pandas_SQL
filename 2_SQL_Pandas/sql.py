# vamos usar o SQLite
# %%
import sqlite3

# %%
import pandas as pd

# %%
conn = sqlite3.connect("web.bd")  # cria o BD => web.bd

# %%
df_data = pd.read_csv("bd_data.csv", index_col=0)  # ler a tabela
# %%
df_data.index.name = "index_name"  # alterar o nome do index

# %%
df_data.to_sql(
    "data", conn, index_label="index_name"
)  # exportar meus dados para a base de dados sql (to_sql => exportacao de dados)
# exportar os dados para a base de dados

# %%
# para executar comandos sql preciso criar ponteiros na Base de dados
# fazer o PY conversar com o BD
# instanciar a conecxao
c = conn.cursor()

# %%
# para passar comandos SQL comando execute
c.execute("CREATE TABLE products(product_id, product_name, price)")
conn.commit()

# %%
# deletar a tabela
c.execute("DROP TABLE products")

# %%
# deletar a tabela
c.execute("DROP TABLE data")

# %%
# tipagem no BD cada tipo de BD tem sua tipagem
c.execute(
    "CREATE TABLE products([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)"
)
# conn.commit()
# a tipagem eh importante pq o BD ja vai alocar as informacoes, ele aloca melhor o BD
# se nao tipar ele aloca muito espaco, se tipar ele prepara melhor os espacos

# %% INSERT => inserir inf em uma tab ja existente (''') permite que trab em varias linhas
# inserir dados no PY com PD and SQL
# passo me tupla separados por , => (1, 'Computer', 800),
c.execute(
    """INSERT INTO products(product_id, product_name, price)
    VALUES
    (1, 'Computer', 800),
    (2, 'Printer', 200),
    (3, 'Table', 300)
"""
)
conn.commit()

# %% # Criar com o PANDAS
# gerar novamente a tabela de 2 em 2 de tras para frente
# criar uma nova tabela

df_data2 = df_data.iloc[::-2]  # gerar novamente a tabela de 2 em 2 de tras para frente
## nao esquecer o conn => conecxao

# %% # inserir valores ja existentes, usando if_exists and append => melhor que insert esse method eh com o PANDAS
df_data2.to_sql("data", conn, if_exists="append")

# %% # LER INF NA BASE DE DADOS
# SELECT => selecionar dados de uma base, sempre sera SELECT de colunas, com * eu puxo tudo
c.execute("SELECT * FROM data")
c.fetchone()  # mostra uma tupla com uma execucao

# %% # retorna uma lista dentro de uma Tuplas
c.execute("SELECT * FROM data")
c.fetchall()

# %% # retorna uma lista dentro de uma Tuplas
c.execute("SELECT * FROM products")
print(c.fetchall())


# %% # leitura de dados e organizar os dados, nao eh uma boa pratica
df = pd.DataFrame(c.fetchall())

# %%
df

# %%
# pegar as informacoes qdo a coluna 2 for maior que 200
c.execute("SELECT * FROM data WHERE 2 > 200")
df = pd.DataFrame(c.fetchall())


# %%
c.execute("SELECT * FROM data WHERE A > 200")
df = pd.DataFrame(c.fetchall())
df

# %% # usando a condicional
# qdo A for + q 200 e B + 100
c.execute("SELECT * FROM data WHERE A > 200 AND B > 100")
df = pd.DataFrame(c.fetchall())
df

# %% # escolher a coluna
c.execute("SELECT A, B, C FROM data WHERE A > 200 AND B > 100")
df = pd.DataFrame(c.fetchall())
df


# %%
# selecionando colunas e condicionais
# Cria uma variavel query
query = "SELECT * FROM data"
df = pd.read_sql(query, con=conn, index_col="index_name")
df

# %% # FAZER DENTRO DO PANDAS
# Cria uma variavel query
query = "SELECT * FROM data"
# df = pd.read_sql(query, con=conn)
# desse jeito o indice nao volta certo => df = pd.read_sql(query, con=conn)
# organizado sem logica adicional
df = pd.read_sql("SELECT A, B, C FROM data WHERE A > 200 AND B > 100", con=conn)

# %%
df

# %% # ver dados da tabela products
for row in c.execute("SELECT * FROM products"):
    print(row)

# %% # FAZER DENTRO DO PANDAS
# Cria uma variavel query
query = "SELECT * FROM data"
df = pd.read_sql("SELECT A, B, C FROM data WHERE A > 200 AND B > 100", con=conn)
# %%
df


# %%
c.execute("PRAGMA table_info(products)")  # comando para visualizar as colunas da tabela
print(c.fetchall())

# %% le a tabela no DF
df = pd.read_sql_query("SELECT * FROM products", conn)
print(df)

# %% UPDATE => Value
# Comandos UPDATE and DELETE, update table products or table data
c.execute("UPDATE products SET price = 1200 WHERE product_name = 'Computer'")
conn.commit()

# %%
for row in c.execute("SELECT * FROM products"):
    print(row)


# %%
