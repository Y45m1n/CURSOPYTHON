# Operações com Variáveis:

salario = 3000
bonus = 500
salario_total = salario + bonus
print (salario_total)

# Manipulação de Strings:

nome = "Maria"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome
print (nome_completo)

# Atualização de Variáveis:

contador = 0
contador = contador + 1
print (contador)


# Variáveis em Estruturas de Controle:

idade = 13
if idade >= 18:
    pode_votar = True
else:
    pode_votar = False

print(pode_votar)

# tipagem

numero = 42
texto = "Python"
# resultado = numero+texto
# print(resultado)
print(f"{numero}"+texto)

# Conversão de Tipos (Type Casting):
numero = 42
texto = str(numero)
print(texto)
