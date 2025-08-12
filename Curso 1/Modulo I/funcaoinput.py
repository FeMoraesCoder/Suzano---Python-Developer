# %%
'''
*** Função input() ***	

A função input() é utilizada para receber dados do usuário
através do teclado. Ela lê o que o usuário digita e retorna
uma string com o valor digitado.
A função built-in input() é utilizada quando queremos ler dados da entrada padrão, que é o teclado.
Ela recebe um argumento do tipo string, que é exibido para o usuário na saída padrão (tela). A funçãoi lÊ a entrada, converte para string e retorna o valor digitado.

'''
# Exemplos

nome = input("Informe o seu nome: ")


# %%

'''
*** Fução print() ***

A função print() é utilizada quando queremos exibir dados na saída padrão, que é o monitor.	Ela recebe um argumento obrigatório do 
tipo varargs de objetos e 4 argumentos opcionais: sep, end, file e flush.

Todos os objetos são convertidos para string, separados por sep e terminados por end. A string final é exibida para o usuário.

Explicação sep, end, file e flush: 
sep: é o separador entre os objetos. O padrão é um espaço em branco.
end: é o que será exibido no final da string. O padrão é uma quebra de linha.
file: é o objeto de arquivo onde a saída será escrita. O padrão é sys.stdout.
flush: é um booleano que indica se a saída deve ser descarregada. O padrão é False.

'''

# Exemplos

nome = 'Felipe'
sobrenome = 'Moraes'

print(nome, sobrenome) # aqui o separador é o espaço e o final é uma quebra de linha
print(nome, sobrenome, end='...\n') # aqui o separador é o espaço e o final é reticências e uma quebra de linha
print(nome, sobrenome, sep="#") # aqui o separador é a cerquilha e o final é uma quebra de linha

# %%

# Praticando 

nome = input("Digite o seu nome: ")
idade = input('Digite a sua idade: ')

print(nome, idade)
print(nome, idade, end='...\n')
print(nome, idade, sep='#', end='...\n')
print(nome, idade, sep='#')
# %%