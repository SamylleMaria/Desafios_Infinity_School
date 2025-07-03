# --------------------------- DESAFIO --------------------------
# 1. Solicite um valor e em seguida informe quantas notas de (100, 50, 20, 10, 5, 2 e 1) são necessárias para reproduzir este valor.
# Dica: Utilize os operadores de divisão inteira // e módulo para pegar o resto da divisão %
# Ex: 1793
# 17 nota(s) de 100
# 1 nota(s) de 50
# 2 nota(s) de 20
# 0 nota(s) de 10
# 0 nota(s) de 5
# 1 nota(s) de 2
# 1 nota(s) de 1


valor = int(input("Digite um valor inteiro "))

notas_de_100 = valor // 100
resto_do_valor = valor % 100

notas_de_50 = resto_do_valor // 50
resto_do_valor = resto_do_valor % 50

notas_de_20 = resto_do_valor // 20
resto_do_valor = resto_do_valor % 20

notas_de_10 = resto_do_valor // 10
resto_do_valor = resto_do_valor % 10

notas_de_5 = resto_do_valor // 5
resto_do_valor = resto_do_valor % 5

notas_de_2 = resto_do_valor // 2
resto_do_valor = resto_do_valor % 2

notas_de_1 = resto_do_valor // 1
resto_do_valor = resto_do_valor % 1

print(f"Para o valor {valor}, são necessárias {notas_de_100} notas de 100, {notas_de_50} notas de 50,00, {notas_de_20} notas de 20,00, {notas_de_10} notas de 10,00, {notas_de_5} notas de 5,00, {notas_de_2} notas de 2,00, {notas_de_1} notas de 1,00.")