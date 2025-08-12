# %%

#Interpolação de strings

"""
Interpolação de Strings

Interpolação de strings é uma forma de criar strings que contêm variáveis.

--- Old Style % ---

O operador % é conhecido como Old Style, e é uma forma antiga de interpolação de strings.

Em Python, podemos usar o operador % para interpolar strings.

Exemplo:

nome = "Felipe"
idade = 30

print("Meu nome é %s e tenho %d anos." % (nome, idade))

O %s é usado para strings e o %d é usado para números inteiros.


--- New Style {} / Format Method ---

O método format() é uma forma mais moderna de interpolação de strings, e é feita com chaves {}.

O New Style é uma forma mais moderna de interpolação de strings, e é feita com chaves {}.

Exemplo:

nome = "Felipe"
idade = 30

print("Meu nome é {} e tenho {} anos.".format(nome, idade))

O New Style é mais flexível e mais fácil de usar do que o Old Style.

--- F-Strings ---

As F-Strings são uma forma ainda mais moderna de interpolação de strings, e são feitas com chaves {} e a letra f antes das aspas.

Exemplo:

nome = "Felipe"
idade = 30

print(f"Meu nome é {nome} e tenho {idade} anos.")

As F-Strings são mais simples e mais legíveis do que o Old Style e o New Style.

"""

nome = "Felipe"
idade = 30

print("Meu nome é %s e tenho %d anos." % (nome, idade))

print('\n')

print("Meu nome é {} e tenho {} anos.".format(nome, idade))

print('\n')

print(f"Meu nome é {nome} e tenho {idade} anos.")

# %%

PI = 3.14159265359

print(f"O valor de PI é {PI:.2f}")
print(f"O valor de PI é {PI:.4f}")
print(f"O valor de PI é {PI:.6f}")
print(f"O valor de PI é {PI:10.2f}")
print(f"O valor de PI é {PI:8.4f}")
# %%

#Exercício

nome = "Felipe"
idade = 30
profissao = "Programador"
linguagem = "Python"
saldo = 56.784

dados = {"nome": "Felipe", "idade": 30}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade:{idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: (nome) Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo: 10.1f}")




# %%
