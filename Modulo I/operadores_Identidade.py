# %%
'''
*** Operadores de Identidade ***

Operadores de identidade são usados para comparar objetos, não se referindo ao valor, mas sim à identidade dos objetos. 

Aqui estão os operadores de identidade em Python:

Operador	Descrição
is	        Retorna True se ambas as variáveis forem o mesmo objeto
is not	    Retorna True se ambas as variáveis não forem o mesmo objeto

Esses operadores são úteis para verificar se duas variáveis se referem ao mesmo objeto na memória. Eles são frequentemente usados em conjunto com 
operadores de comparação para verificar a igualdade de objetos.

O que são?

São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória;

Exemplo: 

curso = "Curso de Python"
nome_curso = curso

curso is nome_curso # True
curso is not nome_curso # False

saldo is limite # False
saldo is not limite # True

'''

# Exemplo 1

saldo = 1000
limite = 500

print(saldo is limite) # False
print(saldo is not limite) # True

# %%