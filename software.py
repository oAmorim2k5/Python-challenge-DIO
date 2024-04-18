saldo = 0
limite = 500
extrato = []
ext_saque = []
ext_deposito = []
numero_saques = 0
max_saques = 3
deposito = float

menu = """
######MENU######

[1] - EXTRATO
[2] - DEPOSITO 
[3] - SAQUE
[0] - SAIR

################
=> """

while True:

    opcao = input(menu)

    if opcao == "1": #If option 1 is selected Statement
        while True:
            print("Extrato:\n")
            print("Extrato saques:")
            print(ext_saque, "\n\n")

            print("Extrato depósitos:")
            print(ext_deposito)

            input_ext = input("Para sair digite qualquer coisa: ")
            if str(input_ext.upper) == "SAIR":
                break
            else:
                break

    elif opcao == "2": #If option 2 is selected Deposit
        while True:
            deposito_menu = f"""
Depósito:
Quanto gostaria de depositar?
Valor minimo = R$1,00
Caso não queira depositar digite "sair"
=> R$"""
            deposito = input(deposito_menu)
            try: #Ultiliza o try para ver se o valor atribuido é um numero
                if str(deposito.upper()) == "SAIR":
                    break
                if float(deposito) < 0:
                    print(deposito_menu, end="\nValor inserido inválido....")
                elif float(deposito) > 0:
                    saldo += float(deposito)
                    print(f"Saldo atual: R${round(saldo, 2)}")
                    ext_deposito.append(f"Depósito à conta: R${deposito} .") #Add an statement list the deposit
                else:
                    print(deposito_menu, end="\nValor inserido inválido....")
            except ValueError:
                print(deposito_menu, end=f"\nEspera-se que digite um valor numérico!!!")

    elif opcao == "3":
        while True:
            saque_menu = f"""
Saque
Limite de saque: R$500,00
Quantidade de saques p/dia: {numero_saques}|{max_saques}
Saldo em conta: R${round(saldo, 2)}
Caso não queira sacar digite "sair"
=> R$"""
            saque = input(saque_menu)
            try:
                if str(saque.upper()) == "SAIR":
                    break
                if float(saque) > saldo:
                    print(saque_menu, end=f"\nValor de saque acima do saldo da conta, saldo: R${round(saldo,2)}")
                elif numero_saques == 3:
                    print(saque_menu, end="Maximo de saques diários alcançado.")
                elif float(saque) <= saldo and float(saque) <= 500:
                    saldo -= float(saque)
                    ext_saque.append(f"Valor de saque: R${round(float(saque),2)}")
                    numero_saques += 1
                elif float(saque) > 500:
                    print(saque_menu, end="Valor inserido acima do permitido")
            except ValueError:
                print(saque_menu, end="\nValor inserido inválido....")

    elif opcao == "0":
        print("Saindo...")
        break