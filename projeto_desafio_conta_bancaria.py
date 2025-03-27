

menu = f""" 

======================== ESCOLHA A OPERAÇÃO DESEJADA ========================

                            [1] Depósito 
                            [2] Saque
                            [3] Extrato
                            [4] Sair

==============================================================================
"""
saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True: 

    print(menu)
    opcao_escolhida = float(input("Digite a opção: "))

        #DEPOSITO

    if opcao_escolhida == 1:
        deposito = float(input("Digite o valor para depósito: "))
        if deposito > 0:
            def depositar (valor):
                global saldo
                saldo += valor
            extrato += f"\nDepósito: R$ {deposito:.2f}"
            depositar(deposito)
        print(f"O valor do saldo atual é de: {saldo:.2f}")

        if deposito <=0:
            print("O valor de deposito informado é inválido!") 
    
    
            #SAQUE
         
    elif opcao_escolhida == 2: 
        if numeros_saques < LIMITE_SAQUES:
            saque = float(input("Digite o valor que deseja sacar: "))
        
            if saque > 500:
                print("O valor informado passou do limite de 500 reais. ")

            elif saque > saldo:   
                print("Saldo Insuficiente!") 
            else:
                saldo-= saque
                numeros_saques += 1
                extrato += f"\n Saque: R$ {saque:.2f}"
                print(f"Saque realizado! Saldo atual R$: {saldo:.2f} ")
        else:
            print("Limite de saque diário atingido!")
    

        #EXTRATO:
    elif opcao_escolhida == 3:
        print(f"\n========================= EXTRATO=======================")
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("===========================================================")
    elif opcao_escolhida == 4:
        print("Operação Finalizada!")
        break
    else:
        print("Operação inválida, tente novamente!")