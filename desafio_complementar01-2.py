"""
-------------------------- Dasafios: Análise de Número de Três Dígitos --------------------------
Você vai criar um programa que recebe um número inteiro de três dígitos e, em seguida, extrai e exibe cada um de seus dígitos separadamente, além de calcular a soma desses dígitos.
Instruções:
Solicite ao usuário que digite um número inteiro de três dígitos (por exemplo: 385, 712, 094, etc. - você pode assumir que o usuário digitará um número válido de três dígitos para este desafio).
Extraia o dígito da centena.
Extraia o dígito da dezena.
Extraia o dígito da unidade.
Calcule a soma de todos esses três dígitos.
Exiba os dígitos separadamente e a soma, de forma clara.
"""

numero_original = int(input(f"Para iniciarmos, digite um número inteiro com 3 digitos: "))
centena = numero_original // 100
unidades_restantes = numero_original % 100

dezena = unidades_restantes // 10
unidades_restantes = unidades_restantes % 10

unidade = unidades_restantes // 1
soma_dos_numeros = centena + dezena + unidade
print(f"O valor {numero_original} tem {centena} centenas, {dezena} dezenas e {unidade} unidades e a soma destes numeros totaliza {soma_dos_numeros}")