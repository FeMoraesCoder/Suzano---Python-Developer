# %%

''' 
### O que são funções?

Funções são blocos de código que são executados quando chamados. Elas são usadas para realizar tarefas específicas.

### Por que usar funções?

1. Reutilização de código
2. Facilidade de manutenção
3. Facilidade de teste
4. Facilidade
5. Modularidade

### Sintaxe

Para definir uma função em Python, você usa a palavra-chave def, seguida pelo nome da função, parênteses, dois pontos e o corpo da função.

Exemplo:

def saudacao():
    print("Olá, mundo!")

### Chamando uma função

Para chamar uma função, você simplesmente digita o nome da função seguido por parênteses.

Exemplo:

saudacao()

### Parâmetros

Os parâmetros são valores que você passa para a função. Eles são usados para personalizar a função.

Exemplo:

def saudacao(nome):
    print(f"Olá, {nome}!") 

saudacao("Felipe")
saudacao("Maria")
saudacao("João")

### Retorno

O retorno é o valor que a função retorna quando é chamada. Você pode usar a palavra-chave return para retornar um valor.

Exemplo:

def soma(a, b):
    return a + b

resultado = soma(10, 20)
print(resultado)

### Exercício

Crie uma função chamada "soma" que recebe dois parâmetros e retorna a soma dos dois números.


'''

# Exemplo

def exibir_mensagem():
    print("Olá, mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo, {nome}")

def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem-vindo, {nome}")

exibir_mensagem()

exibir_mensagem_2(nome="Felipe")

exibir_mensagem_3()
exibir_mensagem_3(nome="Felipe M")

# %%

# Exercício

def calcular_total(numeros):
    return sum(numeros)

def retonar_antecessor_e_sucessor(numero):
    antecessor = numero -1
    sucessor = numero +1

    return antecessor, sucessor

def func_3():
    print("Ola Mundo")


print(calcular_total([1, 2, 3, 4, 5])) # total = 15
print(retonar_antecessor_e_sucessor(10)) # antecessor = 9, sucessor = 11
print(func_3()) # Ola Mundo e None

# %%

# Argumentos nomeados, posicionais e desempacotamento

def salvar_carro(marca, modelo, ano, placa):  # Define a função salvar_carro com quatro parâmetros
    # Salva o carro no banco de dados...
    print(f"Salvando carro {marca} {modelo} {ano} {placa}")  # Imprime uma mensagem formatada com os detalhes do carro

salvar_carro("Fiat", "Uno", 2020, "ABC-1234")  # Chama a função salvar_carro com argumentos posicionais
salvar_carro(marca="Fiat", modelo="Uno", ano=2020, placa="ABC-1234")  # Chama a função salvar_carro com argumentos nomeados
salvar_carro(**{"marca": "Fiat", "modelo": "Uno", "ano": 2020, "placa": "ABC-1234"})  # Chama a função salvar_carro com um dicionário desempacotado

# %%

# Args e Kwargs

''' 
aRGS e Kwargs são usados para passar um número variável de argumentos para uma função.

Args: é uma tupla que permite passar um número variável de argumentos posicionais para uma função.

Kwargs: é um dicionário que permite passar um número variável de argumentos nomeados para uma função.

O que são tuplas e dicionários?

Tuplas: são coleções ordenadas e imutáveis de itens. Elas são definidas entre parênteses e separadas por vírgulas.

Dicionários: são coleções não ordenadas de itens. Eles são definidos entre chaves e consistem em pares de chave-valor separados por dois pontos.

Exemplo:

args = (1, 2, 3, 4, 5)
kwargs = {"nome": "Felipe", "idade": 32}

'''

# %%

# exemplo 

def exibir_poema(data_extenso, *args, **kwargs):
    # A função exibir_poema recebe três tipos de argumentos:
    # - data_extenso: uma string que representa a data ou título do poema.
    # - *args: uma lista de argumentos variáveis que serão as linhas do poema.
    # - **kwargs: um dicionário de argumentos nomeados que serão os metadados do poema.

    # Une todas as linhas do poema (passadas como *args) em uma única string, separadas por quebras de linha.
    texto = "\n".join(args)
    
    # Cria uma string com os metadados (passados como **kwargs), onde cada chave-valor é formatada como "Chave: valor".
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    
    # Combina a data/título, o texto do poema e os metadados em uma única mensagem.
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    
    # Exibe a mensagem final no console.
    print(mensagem)

# Chama a função exibir_poema com um título, duas linhas de poema e dois metadados.
exibir_poema("Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

# %%

''' 
Parâmetors especiais

Parâmetros especiais são parâmetros que têm um significado especial em Python. Eles são usados para criar funções mais flexíveis e poderosas.

1. *args: é uma tupla que permite passar um número variável de argumentos posicionais para uma função.

2. **kwargs: é um dicionário que permite passar um número variável de argumentos nomeados para uma função.

3. *: é usado para indicar que todos os argumentos posicionais restantes devem ser tratados como *args.

4. **: é usado para indicar que todos os argumentos nomeados restantes devem ser

5. /: é usado para separar os argumentos posicionais dos argumentos nomeados.

Exemplo:

def soma(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f

'''

# %%

# Exemplo - Posicitonal-only arguments

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Erro, porque modelo, ano e placa são positional-only arguments

# %%

# Exemplo - Keyword only arguments

def criar_carro(modelo, ano, placa, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") # Erro, porque marca, motor e combustivel são keyword-only

# %%
# Exemplo - Argumentos posicionais e nomeados

def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # valido  
criar_carro("Palio", 1999, "ABC-1234", "Fiat", motor="1.0", combustivel="Gasolina") # valido  

# %%

#objetos de primeira classe

""" 
*** Objetos de primeira classe ***

Em Python as funções são consideradas objetos de primeira classe, o que significa que elas podem ser tratadas como qualquer outro objeto.

Isso permite que você:

1. Atribua funções a variáveis.
2. Passe funções como argumentos para outras funções.
3. Retorne funções de outras funções.
4. Armazene funções em estruturas de dados.
5. Crie funções dentro de outras funções.

Exemplo:

def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Felipe")
print(mensagem)

"""
def saudacao(nome):
    return f"Olá, {nome}!"

mensagem = saudacao("Felipe")
print(mensagem)

# %%

# Exemplo

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(funcao, a, b):
    resultado = funcao(a, b)
    print(f"O resultado da operação é {resultado}")

exibir_resultado(somar, 10, 10) # O resultado da operação 10 + 10 é 20
exibir_resultado(subtrair, 10, 5) # O resultado da operação 10 - 5 é 5
# %%

# Escopo local e escopo global

"""
*** Escopo local e escopo global ***
Em Python, as variáveis podem ter escopo local ou global.

Escopo local: uma variável é local quando é definida dentro de uma função. Ela só pode ser acessada dentro da função.

Escopo global: uma variável é global quando é definida fora de qualquer função. Ela pode ser acessada em qualquer lugar do código.

Exemplo:

def saudacao():
    mensagem = "Olá, mundo!"
    print(mensagem)

saudacao()
print(mensagem) # Erro, porque a variável mensagem é local à função saudacao


*** Essa NÃO é a melhor prática de programação ***
"""

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500) # 2500
print(salario_com_bonus)

# %%

