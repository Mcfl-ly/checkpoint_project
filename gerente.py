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
        func_ja_cadastrado = False
        func_cadastrado = False

        for i in self.listar_funcionarios():
            if nome.title() in i:
                func_cadastrado = True
            else:
                func_cadastrado = False
        if func_ja_cadastrado:
            print("Funcionário já cadastrado.")

        if func_cadastrado is not True:
            cursor.execute(
                f"INSERT INTO funcionarios(nome, cargo, salario, carga_horaria) VALUES ('{nome.title()}', '{cargo}', {salario}, {carga_horaria})")
            db.commit()
            print("Funcionário cadastrado com sucesso.")
        else:
            print("funcionário já cadastrado")

    def listar_funcionarios(self):
        cursor.execute("SELECT * FROM funcionarios")
        funcionarios = cursor.fetchall()
        return funcionarios

    def consultar_funcionario(self, nome):
        for i in self.listar_funcionarios():
            # print(i)
            if nome.title() in i:
                cursor.execute(f"SELECT * FROM funcionarios WHERE nome = '{nome.title()}'")
                funcionario = cursor.fetchall()
                print(funcionario)
                return funcionario
        else:
            print("Funcionário não encontrado no banco de dados.")

    def excluir_funcionario(self, nome):
        confirm = input(f"Gostaria de excluir o funcionário {nome.title()}? (S/N) ").upper()
        if confirm == "s".upper():
            if nome.title() in self.listar_funcionarios():
                cursor.execute(f"DELETE FROM funcionarios WHERE nome = '{nome.title()}'")
                db.commit()
                print("funcionário excluido com sucesso")
            else:
                print("Funcionário não encontrado no banco de dados.")
        else:
            pass
c1 = ControleGerente()
c1.cadastrar('Calum', 'qualquer', 5000, 8)
# c1.consultar_funcionario("gabriel")
# c1.excluir_funcionario("gabriel")
# print(c1.listar_funcionarios())