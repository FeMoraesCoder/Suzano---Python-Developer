# %%

'''
Em linguagens de programação podemos definir valores que podem sofrer
alterações no decorrer da execução do programa. Esses valores recebem
o nome de variáveis, pois eles nascem com um valor e não necessariamente
devem permanecer com o mesmo valor durante a execução do programa.

'''

age = 28 
name = 'Felipe'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

age = 27
name = 'Giovana'
print(f'Meu nome é {name} e eu tenho {age} ano(s) de idade.')

'''
Alterando os valores

Perceba que não precisamos definir o tipo de dados da variável,
o Python é uma linguagem de tipagem dinâmica, ou seja, o tipo de
dado é inferido a partir do valor atribuído à variável.
Para alterar o valor de uma variável, basta atribuir um novo valor.
'''
# %%

'''
*** Constantes ***

Assim como as variáveis, constantes são utilizadas para
armazenar valores. Uma constante nasce com um valor e 
permanece com ele até o final da execução do programa,
ou seja, o valor é imutável.

*** Python não tem constantes ***

Em Python, não existe um tipo de dado específico para constantes,
mas é uma convenção de programação que variáveis que não devem
ter seus valores alterados sejam escritas em letras maiúsculas.

Em algumas linguagens de programação, como C, C++ e Java, existe
um tipo de dado específico para constantes, que são valores que
não podem ser alterados durante a execução do programa.

'''

ABS_PATH = '/home/felipe/Documentos/Python/curso-python'
DEBUG = True

STATES = ['SP', 'RJ', 'MG', 'ES']
AMOUNT = 30.2

# %%

'''
BOAS PRÁTICAS

* O padrão de nomenclatura de variáveis em Python é o snake_case
* O padrão de nomenclatura de constantes em Python é o SNAKE_CASE
* Evite nomes de variáveis genéricos como a, b, c, x, y, z
* Evite nomes de variáveis que não fazem sentido como abc, xyz, etc
* Evite nomes de variáveis que começam com números
* Evite acentos e caracteres especiais nos nomes de variáveis
* Evite palavras reservadas do Python como nome de variáveis
* Evite usar o mesmo nome de variáveis globais e locais
* Evite usar o mesmo nome de variáveis com tipos de dados diferentes
* Evite usar o mesmo nome de variáveis com valores diferentes
* Evite usar variáveis com nomes muito extensos
* Evite usar variáveis com nomes muito curtos
* Evite usar variáveis com nomes muito parecidos
* Evite usar variáveis com nomes muito complexos
* Evite usar variáveis com nomes muito simples

'''

# %%

nome = 'Felipe'
idade = 32

nome = 'Lucas'

print(nome, idade)

limite_saque_diario = 1000

BRAZILIAN_STATES = ['SP', 'RJ', 'MG', 'ES']

print(BRAZILIAN_STATES)
# %%