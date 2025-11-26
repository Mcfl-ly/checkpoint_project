import csv
from datetime import datetime
import os
import sqlite3


class ControleDePonto:
    def __init__(self):
        self.hora = datetime.time(datetime.now()).strftime('%H:%M:%S')
        self.day = datetime.now().strftime('%d-%m-%Y')
        self.db = sqlite3.connect('control.db')
        self.cursor = self.db.cursor()

        self.cab = [
            ["Nome", "Entrada", "Saida"],
        ]
        if not os.path.exists(f'{self.day}.csv'):
            with open(f'{self.day}.csv', 'w', newline='') as arq_csv:
                writer = csv.writer(arq_csv)
                writer.writerows(self.cab)
        else:
            pass

    def entrada(self, nome):
        self.cursor.execute("SELECT * FROM funcionarios")
        funcionarios = self.cursor.fetchall()
        # print(funcionarios)

        dados = []
        with open(f'{self.day}.csv', 'r') as arq_read:
            reader = csv.reader(arq_read)
            for n, linha in enumerate(reader):
                dados.append(linha)
                if nome in linha:
                    print("Funcionário já marcou entrada.")
                    return
        funci_existe = False
        for i in funcionarios:
            if nome in i:
                dd = [nome, self.hora, 'x']
                with open(f'{self.day}.csv', 'a', newline='', encoding='utf-8') as arq:
                    writer = csv.writer(arq)
                    writer.writerow(dd)
                funci_existe = True

        if funci_existe is False:
            print("Funcionário não encontrado.")

    def saida(self, nome):
        dados = []
        indice = None
        funci_existe = False
        with open(f'{self.day}.csv', 'r') as arq_read:
            reader = csv.reader(arq_read)
            for n,linha in enumerate(reader):
                dados.append(linha)
                if nome in linha:
                    indice = n
                    funci_existe = True

        if funci_existe:
            dados[indice][2] = self.hora #esquerda linha, direita coluna
            with open(f'{self.day}.csv', 'w', newline='') as arq:
                writer = csv.writer(arq)
                writer.writerows(dados)
        elif not funci_existe:
            print("Funcionário sem entrada.")
            return False