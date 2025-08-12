# %%
'''
*** Operadores de Associação ***

Operadores de associação são usados para verificar se um objeto é uma instância de uma classe ou se uma variável é uma instância de um objeto.

Aqui estão os operadores de associação em Python:

Operador	Descrição
in	        Retorna True se um valor específico estiver presente em um objeto
not in	    Retorna True se um valor específico não estiver presente em um objeto

O que são?

São operadores utilizados para verificar se um objeto está presente em uma sequência, como uma lista, tupla, string, etc.

Exemplo:

curso = "Curso de Python"
frutas = ["maçã", "banana", "laranja"]
saque = [100, 200, 300]

"Python" in curso # True
"Python" not in curso # False

"maçã" in frutas # True
"maçã" not in frutas # False

500 in saque # False
500 not in saque # True

'''

curso = "Curso de Python"
frutas = ["maçã", "banana", "laranja"]
saque = [100, 200, 300]

"Python" in curso # True
print("Python" in curso)
"Python" not in curso # False
print("Python" not in curso)

print('\n')
"maçã" in frutas # True
print("maçã" in frutas)
"maçã" not in frutas # False
print("maçã" not in frutas)

print('\n') 
500 in saque # False
print(500 in saque)
500 not in saque # True
print(500 not in saque)


0#%% 