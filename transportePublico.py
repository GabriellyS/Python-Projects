precoPassagem = 6.00
saldo = 0.00
senhaAdmin = 1234

while True:
    print("---------------------------------------------------------\n\nBem vindo ao sistema de transporte, qual seu tipo de usuario? \n")
    menuUm = int(input("1 - Usuario Converncional \n2 - Usuario Admin\n3 - Sair\n\n"))

    import os
    os.system('clear')

    if menuUm == 1:
        while True:
            print(f"Bem vindo ao sistema de transporte\n\nSeu saldo é de: {saldo}\nPreço da passagem: {precoPassagem}\n")
            menuDois = int(input("Qual opção deseja?\n1 - Comprar passagem\n2 - Carregar créditos\n3 - Sair\n\n"))

            if menuDois == 1:
                import os
                os.system('clear')

                if saldo >= precoPassagem:
                    saldo -= precoPassagem
                    print(f"Seu saldo ficou: {saldo}")
                else:
                    print("Seu saldo é insuficiente\n")

            elif menuDois == 2:
                recarga = float(input("\nDigite o valor da recarga: "))

                if recarga > 0:  
                    saldo +=recarga
                    print(f"\nSeu saldo é de: {saldo}")
                else:
                    print("\nSua recarda é invalida\n")
            elif menuDois == 3:
                break
            else:
                print(f"Digite uma opçao válida")


    elif menuUm == 2:
        senha = int(input("Digite a senha: "))

        import os
        os.system('clear')

        if senha == senhaAdmin:
            while True:
                print(f"Bem vindo ao menu Admin\n\nO saldo do cartao é de {saldo}\nPreço da passagem: {precoPassagem}\n")
                menuTreis = int(input("Qual opção deseja?\n1 - Alterar valor da passagem\n2 - Alterar Senha\n3 - Sair\n\n"))

                if menuTreis == 1:
                    import os
                    os.system('clear')
                    alteraçao = float(input("Digite o novo valor da passagem: "))

                    if alteraçao < 0:
                        print("Digite um valor valido\n")
                    else:
                        precoPassagem = alteraçao

                elif menuTreis == 2:
                    novaSenha = float(input("\nDigite a nova senha: "))

                    if novaSenha == senhaAdmin:  
                        print(f"\nSenha digitada é a mesma da anterior")
                    else:
                        senhaAdmin = novaSenha
                        print("\nSua senhafoi alterada com sucesso\n")
                elif menuTreis == 3:
                        break
                else:
                    print(f"Digite uma opçao válida\n")
        else:
            print("Senha inválida\n")

    elif menuUm == 3:
        break
    else:
        print(f"Digite uma opçao válida\n")
    
