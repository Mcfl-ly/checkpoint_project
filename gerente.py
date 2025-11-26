import os
import sqlite3
import csv
import dotenv
from datetime import datetime
dotenv.load_dotenv()




class ControleGerente:
    def __init__(self):
        self.db = sqlite3.connect("control.db")
        self.cursor = self.db.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome VARCHAR(30) NOT NULL,cargo VARCHAR(30) NOT NULL,salario FLOAT NOT NULL,carga_horaria FLOAT NOT NULL)")
        self.pswd__ = os.getenv("PASSWORD")
        self.day = datetime.now().strftime('%d-%m-%Y')

    def checar_login(self, senha):
        if senha == self.pswd__:
            return True
        else:
            return False

    def cadastrar(self, nome, cargo, salario, carga):
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
            self.cursor.execute(
                f"INSERT INTO funcionarios(nome, cargo, salario, carga_horaria) VALUES ('{nome.title()}', '{cargo}', {salario}, {carga})")
            self.db.commit()
            print("Funcionário cadastrado com sucesso.")
        else:
            print("funcionário já cadastrado")

    def listar_funcionarios(self):
        self.cursor.execute("SELECT * FROM funcionarios")
        funcionarios = self.cursor.fetchall()
        return funcionarios

    def consultar_funcionario(self, nome):
        for i in self.listar_funcionarios():
            # print(i)
            if nome.title() in i:
                self.cursor.execute(f"SELECT * FROM funcionarios WHERE nome = '{nome.title()}'")
                funcionario = self.cursor.fetchall()

                return funcionario
        else:
            print("Funcionário não encontrado no banco de dados.")

    def excluir_funcionario(self, nome):
        continuar = False
        for i in self.listar_funcionarios():
            if nome.title() in i:
                continuar = True
        if continuar is True:
            confirm = input(f"Gostaria de excluir o funcionário {nome.title()}? (S/N) ").upper()
            if confirm == "s".upper():
                for i in self.listar_funcionarios():
                    if nome.title() in i:
                        self.cursor.execute(f"DELETE FROM funcionarios WHERE nome = '{nome.title()}'")
                        self.db.commit()
                        print("funcionário excluido com sucesso")

            else:
                pass
        else:
            print("Funcionário não encontrado no banco de dados.")

    def consultar_horarios(self):
        dados = []
        with open(f'{self.day}.csv', 'r') as arq_read:
            reader = csv.reader(arq_read)
            for n, linha in enumerate(reader):
                dados.append(linha)
        for d in dados:
            print(d)