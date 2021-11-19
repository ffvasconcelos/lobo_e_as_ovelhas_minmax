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
  [0, 0, 0, 1, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0],
  [-1, 0, -1, 0, -1, 0, -1, 0],
]

def vitoria(estado, jogador):
  if (jogador == HUMANO):
    estados_de_vitoria = [
      estado[7][0], estado[7][1], estado[7][2], estado[7][3], estado[7][4], estado[7][5], estado[7][6], estado[7][7],
    ]

    if(HUMANO in estados_de_vitoria): return True
    else: return False

  if(jogador == COMP):
    for i in range(estado[0]):
      for j in range(estado[0]):
        if(estado[i][j] == HUMANO):
          if j == 0 & i == 0:
            if(estado[i+1][j+1] == COMP): return True
          elif i == 0:
            if(estado[i+1][j+1] == COMP & estado[i+1][j-1] == COMP): return True
          elif j == 0:
            if(estado[i+1][j+1] == COMP & estado[i-1][j+1] == COMP): return True
          elif j == 7:
            if(estado[i+1][j-1] == COMP & estado[i-1][j-1] == COMP): return True
          else:
            if(estado[i+1][j-1] == COMP & estado[i-1][j-1] == COMP & estado[i+1][j+1] == COMP & estado[i+1][j-1] == COMP): return True
          return False
