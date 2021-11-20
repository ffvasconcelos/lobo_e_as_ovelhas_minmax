from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMANO = -1
COMP = +1
tabuleiro = [
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
]
estado_inicial = [
  [0, 0, 0, -1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1, 0, 1, 0],
]

pos_inicial_L = [0,3]
pos_inicial_O = [[7,0],[7,2],[7,4],[7,6]]

def vitoria(jogador, posi_lobo, posi_ovelha):
  if (jogador == HUMANO):
    if(posi_lobo[0] == 7): return True
    else: return False

  if(jogador == COMP):
    movs = [[posi_lobo[0] + 1, posi_lobo[1] + 1], [posi_lobo[0] + 1, posi_lobo[1] - 1], [posi_lobo[0] - 1, posi_lobo[1] + 1], [posi_lobo[0] - 1, posi_lobo[1] - 1]]

    for i in movs:
      if(i[0] < 0 | i[0] > 7 | i[1] < 0 | i[1] > 7):
        movs.pop(movs.index(i))

    for i in movs:
      if i not in posi_ovelha: return False
    
    return True

def desenha_tabuleiro(estado):
  for i in range(0,8):
    print('\n-----------------')
    print("|", end='')
    for j in range(0,8):
      if estado[i][j] == COMP:
        print("O|", end='')
      elif estado[i][j] == HUMANO:
        print("L|", end='')
      else:
        print(" |", end='')
  print('\n-----------------')

def main():

  list1 = [[0,0],[1,1],[2,2]]
  list2 = [[1,1],[2,2]]

  print(list2 in list1)
  

if __name__ == '__main__':
  main()