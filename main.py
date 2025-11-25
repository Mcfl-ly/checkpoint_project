from gerente import ControleGerente
import os
import sqlite3
db = sqlite3.connect("control.db")
cursor = db.cursor()
cursor.execute(
            "CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome VARCHAR(30) NOT NULL,cargo VARCHAR(30) NOT NULL,salario FLOAT NOT NULL,carga_horaria FLOAT NOT NULL)")


print("Modo de acesso:\n1 - GERENTE\n2 - FUNCIONÁRIO\n3 - SAIR\n")
iniciar = int(input('\n'))
print()
if iniciar == 1:
    os.system('cls')
    pswd = str(input("Insira a senha: "))
    gerente = ControleGerente()
    checar_login = gerente.checar_login(pswd)
    if checar_login:
        os.system('cls')
        action = int(input("Ações GERENTE:\n"
                        "1 - Cadastrar Funcionário\n"
                       "2 - Listar Funcionários\n"
                       "3 - Consultar Funcionário\n"
                       "4 - Excluir Funcionário\n"))
        if action == 1:
            nome = str(input('Nome: '))
            cargo = str(input('Cargo: '))
            salario = float(input('Salario: '))
            carga_horaria = float(input('Carga Horária: '))
            os.system('cls')
            gerente.cadastrar(nome, cargo, salario, carga_horaria)

        elif action == 2:
            os.system('cls')
            funcionarios = gerente.listar_funcionarios()
            for i in funcionarios:
                print(i)

        elif action == 3:
            os.system('cls')
            func = input("Digite o nome do funcionário que deseja consultar: ")
            func2 = gerente.consultar_funcionario(func)
            if bool(func2) is True:
                print(f'ID: {func2[0][0]}\nNome: {func2[0][1]}\nCargo: {func2[0][2]}\nSalário: {func2[0][3]}\nCarga Horária: {func2[0][4]}')

        elif action == 4:
            os.system('cls')
            del_emp = str(input("Digite o nome do funcionário que deseja excluir: "))
            gerente.excluir_funcionario(del_emp)

