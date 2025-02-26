"""
Programa que conforme a quantidade digitada pelo usuário
Retorne 6 números aleatórios para sortear na loteria
"""
from time import sleep
from random import sample
jogo = [[], [], [], [], [], []]
print('SORTEIO DE NÚMEROS PARA A MEGA SENA')
print('-'*35)
sort = int(input('Quantos jogos você deseja sortear? '))
sleep(0.2)
print(f'-=' * 3, f'SORTEANDO {sort} JOGOS', f'-=' * 3,)
for c in range(0, sort):
    num = sample(range(1, 60), 6)
    sleep(0.5)
    num.sort()
    print(f'Jogo {c+1}: {num}')
print('-'*35)
print('Sorteio Encerrado!')

