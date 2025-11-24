import os
import sqlite3
import csv

db = sqlite3.connect("control.db")
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome VARCHAR(30) NOT NULL,cargo VARCHAR(30) NOT NULL,salario FLOAT NOT NULL,carga_horaria FLOAT NOT NULL)")


class ControleGerente:
    def __init__(self):
        print("Nivel de Acesso: GERENTE")

    def cadastrar(self, nome, cargo, salario, carga_horaria):
        cursor.execute(f"INSERT INTO funcionarios(nome, cargo, salario, carga_horaria) VALUES ('{nome}', '{cargo}', {salario}, {carga_horaria})")
        db.commit()
        print("Funcionário cadastrado com sucesso")

    def listar_funcionarios(self):
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()
        return funcionarios

c1 = ControleGerente()
c1.cadastrar("Flavio", "promotor", 2100, 6)
print(c1.listar_funcionarios())