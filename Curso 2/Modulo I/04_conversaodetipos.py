# %%

'''
Convertento tipos

Em alguns momentos é necessário converter o tipo de uma variável para manipular de forma diferente.
Por exemplo: 
Variáveis do tipo string, que armazenam números e precisamos fazer alguma operação matemática com esse valor.


'''
#Inteiro para float

preco = 10
print(preco)

preco = float(preco)
print(preco)

# %%

# Conversão por divisão

preco = 10
print(preco)

print(preco / 2)

print(preco // 2)


# %%

# Númerico para String

preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f'idade {idade} preco {preco}'
print(texto)

# %%

# Strint para número

preco = "10.50"
idade = "28"

print(float(preco))

print (int(idade))

# %%

# Erro de Conversão

preco ="python"
print(float(preco))

# vai dar erro aqui

# %%

# Conversão de tipos - Exercitanto a conversão de tipos 

print (int(1.973487)) # aqui o resultado vai ser '1' porque o int só pega a parte inteira

print(int("10")) # aqui o resultado vai ser '10'
print(float("10.10")) # aqui o resultado vai ser '10.1'
print(float(100)) # aqui o resultado vai ser '100.0'

print(str(10.10)) # aqui o resultado vai ser '10.1'

valor = 10
valor_str = str(valor) 
print(type(valor)) # aqui o resultado vai ser 'int', porque o valor é um número inteiro
print(type(valor_str)) # aqui o resultado vai ser 'str', porque o valor foi convertido para string

print(100 / 2) # aqui o resultado vai ser '50.0'

print(100 / 2) # aqui o resultado vai ser '50.0', porque o / pega a parte decimal
print(100 // 2) # aqui o resultado vai ser '50', porque o // pega a parte inteira
# %%

