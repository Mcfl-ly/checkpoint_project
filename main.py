from gerente import ControleGerente
import os
import sqlite3
from ponto import ControleDePonto


db = sqlite3.connect("control.db")
cursor = db.cursor()
cursor.execute(
            "CREATE TABLE IF NOT EXISTS funcionarios(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,nome VARCHAR(30) NOT NULL,cargo VARCHAR(30) NOT NULL,salario FLOAT NOT NULL,carga_horaria FLOAT NOT NULL)")


while True:
    print("Modo de acesso:\n1 - GERENTE\n2 - FUNCIONÁRIO\n3 - SAIR\n")
    iniciar = int(input('\n'))
    print()
    if iniciar == 1:
        os.system('cls')
        pswd = str(input("Insira a senha: "))
        gerente = ControleGerente()
        checar_login = gerente.checar_login(pswd)
        while checar_login:
            os.system('cls')
            action = int(input("Ações GERENTE:\n"
                            "1 - Cadastrar Funcionário\n"
                           "2 - Listar Funcionários\n"
                           "3 - Consultar Funcionário\n"
                           "4 - Excluir Funcionário\n"
                            "5 - Consultar Horários\n"
                            "6 - Sair\n"))

            if action == 1:
                nome = str(input('Nome: '))
                cargo = str(input('Cargo: '))
                salario = float(input('Salario: '))
                carga_horaria = float(input('Carga Horária: '))
                os.system('cls')
                confirmar = int(input(f"Adicionar os seguintes dados a base de dados?\n{nome.title()}, {cargo.title()}, {salario}, {carga_horaria}\n1 - Sim\n2 - Não\n"))
                if confirmar == 1:
                    gerente.cadastrar(nome, cargo, salario, carga_horaria)
                    restart1 = int(input("Deseja continuar?\n1 - Sim\n2 - Não\n"))
                    if restart1 == 1:
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        break
                elif confirmar == 2:
                    continue

            elif action == 2:
                os.system('cls')
                funcionarios = gerente.listar_funcionarios()
                for i in funcionarios:
                    print(i)
                restart2 = int(input("Deseja continuar?\n1 - Sim\n2 - Não\n"))
                if restart2 == 1:
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    break

            elif action == 3:
                os.system('cls')
                func = input("Digite o nome do funcionário que deseja consultar: ")
                func2 = gerente.consultar_funcionario(func)
                if bool(func2) is True:
                    print(f'ID: {func2[0][0]}\nNome: {func2[0][1]}\nCargo: {func2[0][2]}\nSalário: {func2[0][3]}\nCarga Horária: {func2[0][4]}')
                    restart3 = int(input("Deseja continuar?\n1 - Sim\n2 - Não\n"))
                    if restart3 == 1:
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        break
                else:
                    restart3 = int(input("Deseja continuar?\n1 - Sim\n2 - Não\n"))
                    if restart3 == 1:
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        break
            elif action == 4:
                os.system('cls')
                del_emp = str(input("Digite o nome do funcionário que deseja excluir: "))
                gerente.excluir_funcionario(del_emp)
                restart4 = int(input("Deseja continuar?\n1 - Sim\n2 - Não\n"))
                if restart4 == 1:
                    os.system('cls')
                    continue
                else:
                    os.system('cls')
                    break
            elif action == 5:
                gerente.consultar_horarios()
                input('Enter para prosseguir...')
            elif action == 6:
                break
        else:
            os.system('cls')
            print("Senha incorreta.")
            continue
    elif iniciar == 2:
        os.system('cls')
        c1 = ControleGerente()
        all_func = c1.listar_funcionarios()
        pode_entrar = False

        nome_funcionario = str(input('Nome: '))

        for i in all_func:
            if nome_funcionario.title() in i:
                pode_entrar = True
        if pode_entrar:
            os.system('cls')
            entrada_saida = int(input("Nivel de acesso: FUNCIONÁRIO\n1 - Entrada\n2 - Saida\n"))
            ponto = ControleDePonto()
            if entrada_saida == 1:
                os.system('cls')
                ponto.entrada(nome_funcionario.title())
                print(f"{nome_funcionario.title()}Entrada registrada com sucesso às {ponto.hora}")
                pos_entrada = input("Gostaria de finalizar? S/N\n").upper()
                if pos_entrada == 's':
                    os.system('cls')
                    print("Finalizando...")
                    break

                elif pos_entrada == 'n':
                    os.system('cls')
                    continue

            elif entrada_saida == 2:
                os.system('cls')
                ponto.saida(nome_funcionario.title())
                input("Enter para continuar...")
            else:
                print("Escolha uma opção válida.")
        else:
            os.system('cls')
            print("Funcionário não encontrado.")
    elif iniciar == 3:
        break