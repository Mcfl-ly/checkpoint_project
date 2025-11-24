import csv
from datetime import datetime
import os
import sqlite3
hora = datetime.time(datetime.now()).strftime('%H:%M:%S')
day = datetime.now().strftime('%d-%m-%Y')

class ControleDePonto:

    def __init__(self):
        self.db = sqlite3.connect('control.db')
        self.cursor = self.db.cursor()

        self.cab = [
            ["Nome", "Entrada", "Saida"],
        ]
        if not os.path.exists(f'{day}.csv'):
            with open(f'{day}.csv', 'w', newline='') as arq_csv:
                writer = csv.writer(arq_csv)
                writer.writerows(self.cab)
        else:
            pass

    def entrada(self, nome, h_entrada):
        self.cursor.execute("SELECT * FROM funcionarios")
        funcionarios = self.cursor.fetchall()
        # print(funcionarios)

        dados = []
        with open(f'{day}.csv', 'r') as arq_read:
            reader = csv.reader(arq_read)
            for n, linha in enumerate(reader):
                dados.append(linha)
                if nome in linha:
                    return "Funcionário já marcou entrada"

        funci_existe = False
        for i in funcionarios:
            if nome in i:
                dd = [nome, h_entrada, 'x']
                with open(f'{day}.csv', 'a', newline='', encoding='utf-8') as arq:
                    writer = csv.writer(arq)
                    writer.writerow(dd)
                funci_existe = True

        if funci_existe is False:
            return "Funcionário não encontrado"

    def saida(self, nome, h_saida):
        dados = []
        indice = None
        funci_existe = False
        with open(f'{day}.csv', 'r') as arq_read:
            reader = csv.reader(arq_read)
            for n,linha in enumerate(reader):
                dados.append(linha)
                print(linha)
                if nome in linha:
                    indice = n
                    funci_existe = True

        if funci_existe is True:
            dados[indice][2] = h_saida #esquerda linha, direita coluna
            with open(f'{day}.csv', 'w', newline='') as arq:
                writer = csv.writer(arq)
                writer.writerows(dados)
        else:
            return "Funcionário sem entrada"
