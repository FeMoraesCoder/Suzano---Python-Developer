# %%

'''
*** Operadores Lógicos ***

Operadores lógicos são usados para combinar expressões condicionais e retornar um valor booleano (True ou False). Aqui estão os operadores lógicos em Python:

Operador	Descrição
and	        Retorna True se ambas as expressões forem verdadeiras
or	        Retorna True se pelo menos uma das expressões for verdadeira
not	        Inverte o valor da expressão

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, 
o resultado retornado é um booleano, dessa forma podemos combinar operadores de comparação com os operadores lógicos, exemplo:

op_comparacao + op_logico + op_comparacao... N...


'''

#OPERADOR AND

saldo = 1000
saque = 200
limite = 100

print("\n*** OPERADOR AND ***\n")
saldo >= saque and saldo <= limite # True
print(saldo >= saque and saldo <= limite)
saldo >= saque and saldo > limite # False
print(saldo >= saque and saldo > limite)   # False

#OPERADOR OR

print("\n*** OPERADOR OR ***\n")
saldo >= saque or saldo <= limite # True
print("saldo >= saque or saldo <= limite = ", saldo >= saque or saldo <= limite) # True

saldo >= saque or saldo > limite # True
print("saldo >= saque or saldo > limite = ", saldo >= saque or saldo > limite) # True

#OPERADOR NOT
print("\n*** OPERADADOR NOT ***\n")
saldo >= saque # True
print("saldo >= saque = ", saldo >= saque) # True
not saldo >= saque # False
print("not saldo >= saque = ", not saldo >= saque) #False

operador = not False
print(operador)

# %%

# EXEMPLO SISTEMA BANCÁRIO

# Usando parenteses para fazer a precedencia de operadores

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(saldo >= saque and saque <= limite or conta_especial and saldo >= saque)

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print((saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque))

# a ideia aqui foi mostrar como fica mais legível fazer da segunda forma

# %%

# tabela verdade

print("True  and True   = ", True and True) # True
print("True  and False  = ", True and False) # False
print("False and True   = ", False and True) # False
print("False and False  = ",False and False) # False
print("\n")
print("True  or True   = ", True or True) # True
print("True  or False  = ", True or False) # True
print("False or True   = ", False or True) # True
print("False or False  = ", False or False) # False
print("\n")
print("not True   = ",not True) # False
print("not False  = ", not False) # True

# %%