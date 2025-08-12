# %%

# Maiúsculas, minúsculas e titulos, e eliminando espaços em branco

nome = "Felipe"

print(nome.upper()) # Converte para maiúsculas
print(nome.lower()) # Converte para minúsculas
print(nome.title()) # Converte para título

texto = "   Python   "

print("." + texto.strip() + ".") # Remove espaços em branco
print("." + texto.lstrip() + ".") # Remove espaços em branco à esquerda
print("." + texto.rstrip() + ".") # Remove espaços em branco à direita

# %%

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))


print("-".join(menu))

#Como seria com for? 

for letra in menu:
    print(letra, end="-")

# %%

