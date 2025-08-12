# %%

'''
Desafio 

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu
a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

- Operação de depósito:

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos
preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

- Operação de saque:

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve
exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos
na operação de extrato.

- Operação de extrato:

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 

1500.45 é R$ 1500.45


'''

menu = '''
[1] - Depósito
[2] - Saque
[3] - Extrato
[4] - Sair

Escolha uma opção:
'''

saldo = 0
limite_saque = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("****** Depósito ******")
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print("Valor inválido.\n")

    elif opcao == "2":
        print("****** Saque ****** \n")
        if numero_de_saques < LIMITE_DE_SAQUES:
            valor = float(input("Digite o valor do saque: "))
            if valor <= 0:
                print("Valor de saque inválido.\n")
            elif valor <= saldo and valor <= limite_saque:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_de_saques += 1
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
            else:
                print("Saldo insuficiente ou valor do saque maior que o limite permitido.\n")
        else:
            print("Limite de saques diários atingido.\n")

    elif opcao == "3":
        print("****** Extrato ****** \n")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "4":
        print("Saindo do sistema... Tchau!")
        break

    else:
        print("Opção inválida.\n")
# %%