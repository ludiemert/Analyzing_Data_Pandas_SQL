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
