# %%

'''
Fatiamento de Strings

O fatiamento de strings é uma técnica que permite extrair partes de uma string.

Exemplo:

curso = "Curso de Python"

curso[0] # C
curso[1] # u
curso[2] # r
curso[3] # s
curso[4] # o
curso[5] # espaço
curso[6] # d
curso[7] # e
curso[8] # espaço
curso[9] # P
curso[10] # y
curso[11] # t
curso[12] # h
curso[13] # o
curso[14] # n

curso[0:5] # Curso
curso[6:8] # de
curso[9:14] # Python

curso[:5] # Curso
curso[6:] # de Python
curso[9:] # Python
curso[:] # Curso de Python

curso[0:14:2] # Cru e yhn
curso[::2] # Cru e yhn
curso[::-1] # nohtyP ed osruC
curso[::-2] # nhy oC

curso[0:14:-1] # Nada
curso[14:0:-1] # nohtyP ed osruC

curso[14:0:-1] # nohtyP ed osruC
curso[14::-1] # nohtyP ed osruC
curso[::-1] # nohtyP ed osruC
'''

# %%
curso = "Curso de Python"

curso[0] # C
print(curso[0])
print(curso[1]) # u
print(curso[2]) # r
print(curso[3]) # s
print(curso[4]) # o
print(curso[5]) # espaço
print(curso[6]) # d
print(curso[7]) # e
print(curso[8]) # espaço
print(curso[9]) # P
print(curso[10]) # y
print(curso[11]) # t
print(curso[12]) # h
print(curso[13]) # o
print(curso[14]) # n

print(curso[0:5]) # Curso
print(curso[6:8]) # de
print(curso[9:14]) # Python

print(curso[:5]) # Curso
print(curso[6:]) # de Python
print(curso[9:]) # Python
print(curso[:]) # Curso de Python

print(curso[0:14:2]) # Cru e yhn
print(curso[::2]) # Cru e yhn
print(curso[::-1]) # nohtyP ed osruC
print(curso[::-2]) # nhy oC

print(curso[0:14:-1]) # Nada
print(curso[14:0:-1]) # nohtyP ed osruC

print(curso[14:0:-1]) # nohtyP ed osruC
print(curso[14::-1]) # nohtyP ed osruC
print(curso[::-1]) # nohtyP ed osruC

# %%

# Exercício

nome = 'Felipe de Moraes Aparecido'

print(nome[0:6]) # Extrai os caracteres da posição 0 até a 5 (Felipe)
print(nome[7:9]) # Extrai os caracteres da posição 7 até a 8 (de)
print(nome[10:16]) # Extrai os caracteres da posição 10 até a 15 (Moraes)
print(nome[17:]) # Extrai os caracteres da posição 17 até o final (Aparecido)
print(nome[:6]) # Extrai os caracteres do início até a posição 5 (Felipe)
print(nome[7:]) # Extrai os caracteres da posição 7 até o final (de Moraes Aparecido)
print(nome[10:]) # Extrai os caracteres da posição 10 até o final (Moraes Aparecido)
print(nome[:]) # Extrai todos os caracteres da string (Felipe de Moraes Aparecido)
print(nome[0:23:2]) # Extrai os caracteres da posição 0 até a 22, pulando de 2 em 2 (Flied orsApcd)
print(nome[::2]) # Extrai todos os caracteres da string, pulando de 2 em 2 (Flied orsApcd)

# %%

# Exercício

nome = 'Felipe de Moraes Aparecido'  # Define a string com o nome completo

print(nome[0])  # Imprime o primeiro caractere da string (F)
print(nome[-2])  # Imprime o penúltimo caractere da string (e)
print(nome[:9])  # Imprime os caracteres da posição 0 até a 8 (Felipe de)
print(nome[10:])  # Imprime os caracteres da posição 10 até o final (Moraes Aparecido)
print(nome[10:16])  # Imprime os caracteres da posição 10 até a 15 (Moraes)
print(nome[10:16:2])  # Imprime os caracteres da posição 10 até a 15, pulando de 2 em 2 (Mra)
print(nome[:])  # Imprime todos os caracteres da string (Felipe de Moraes Aparecido)
print(nome[::-1])  # Imprime todos os caracteres da string em ordem reversa (odicerpA seaorM ed epileF)

# %%

