import sqlite3 as sql

# Conecta ao SQLite (cria o banco de dados 'notes_db.db' se não existir)
con = sql.connect('notes_db.db')

# Cria um cursor
cur = con.cursor()

# Apaga a tabela 'notes' se já existir
cur.execute("DROP TABLE IF EXISTS notes")

# Cria a tabela 'notes' no banco de dados 'notes_db'
sql_create_table = '''CREATE TABLE "notes" (
    "id"    INTEGER PRIMARY KEY AUTOINCREMENT,
    "titulo"    TEXT,
    "detalhes"  TEXT,
    "data_criacao"  TEXT,
    "data_modificacao"  TEXT,
    "pensamentos"  TEXT,
    "pensamentos_rapidos"  TEXT
)'''
cur.execute(sql_create_table)

# Commita (salva) as mudanças
con.commit()

# Fecha a conexão
con.close()

print("Tabela 'notes' criada com sucesso em 'notes_db.db'")