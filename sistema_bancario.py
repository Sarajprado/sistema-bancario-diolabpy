import time

menu = '''
[0] Depositar

[1] Sacar

[2] Extrato

[3] Sair

=>  '''


sim = "S"
nao = "N"
saldo = 0 
limite = 500 
extrato = " "
numero_saques = 0
LIMITES_SAQUES = 3



while True:
    
    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe qual o valor que deseja depositar: "))

        if valor > 0: # O valor do depósito deve ser sempre positivo.
            saldo += valor 
            extrato += f"Depósito: R$ {valor:.2f}\n"

            time.sleep(1) #Coloca o programa para "dormir" pela quantidade de segundos determinado.
            print("Depósito feito com sucesso!")

        else: 
            print("Operação falhou! O valor informado é inválido.")  # se o depósito for menor do que 0.

            time.sleep(1)  
            resposta = str(input("Deseja fazer outra operação? S/N")) 
            if resposta == sim:
                print(menu)
                continue
             
            else:
                print("Fim da Operação!")
                break

    elif opcao == "1":
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo #Se o valor de saque desejado for maior que saldo.

        excedeu_limite = valor > limite #Se o valor excedeu o valor limmite de saque. 

        excedeu_saques = numero_saques >= LIMITES_SAQUES  #Se a quantidade de saques ultrapassou o limite diário.

        sucesso_saque = valor <= limite


        if excedeu_saldo:
                time.sleep(1)
                print("\033[0;31mFalha na operação! Saldo insuficiente!\033[m") # Houve mudança na cor das letras no terminal.

        elif excedeu_limite:
                time.sleep(1)
                print("\033[0;31mFalha na operação! O valor do saque é maior que o limite.\033[m")

        elif excedeu_saques:
                time.sleep(1)
                print("\033[0;31mFalha na operação! Você alcançou o limite de saques.\033[m")

        elif sucesso_saque:
             print("carregando....")
             time.sleep(2)
             print("Saque realizado com sucesso!")
             
             time.sleep(1)
             resposta = str(input("Deseja fazer outra operação? S/N")) 
             if resposta == sim:
                print(menu)
                continue
             
             else:
                  print("Fim da Operação!")
                  break
       
        elif valor > 0: # Para tentativa de saque negativo.
           saldo -= valor
           extrato += f"Saque: R$ {valor:.2f}\n"
           numero_saques += 1 #Para contagem de vezes de saque.
           
        else: 
            print("Falha na operação! O valor informado é invalido.")
            

    elif opcao == "2":

        time.sleep(2)

        print("========== \033[1m Extrato \033[m ==========")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("================================")

        time.sleep(1)
        resposta = str(input("Deseja fazer outra operação? S/N")) 
        if resposta == sim:
            print(menu)
            continue
             
        else:
            print("Fim da Operação!")
            break
            
    elif opcao == "3":
            print("Fim da operação!")
            break

    else:
        print("Opção não identificada! Por favor selecione novamente a operação desejada.")
