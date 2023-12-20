from cores import Cores
import pygame
from posicao import Posicao


class Block():
    # Inicializa as propriedades basicas de um bloco.
    def __init__(self, id):  # todas as informações para desenhar os blocos
        self.id = id
        self.celulas = {}
        self.tamanho_cell = 30
        self.desvio_linha = 0
        self.desvio_coluna = 0
        self.rotation_state = 0
        self.cores = Cores.cores_cell() # Obtem as cores de cores.py a partir do classmethod.

    # Funcao usada em blocks.py para mudar o local de nascimento do bloco.
    def move(self, linhas, colunas):
        self.desvio_linha += linhas
        self.desvio_coluna += colunas

    # calcula a posição atual das células do bloco levando em conta o desvio de linha e coluna.
    def posicao_cell(self):
        blocos = self.celulas[self.rotation_state]
        blocos_movidos = []
        for posicao in blocos:
            posicao = Posicao(posicao.linha+self.desvio_linha, posicao.coluna+self.desvio_coluna)
            blocos_movidos.append(posicao)
        return blocos_movidos

    def girar(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.celulas):
            self.rotation_state = 0

    def cancelar_giro(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.celulas) - 1

    # Desenha o bloco na tela usando pygame, considerando a posição atual das células do bloco.
    def draw(self, screen):
        blocos = self.posicao_cell()
        for bloco in blocos:
            bloco_rect = pygame.Rect(bloco.coluna*self.tamanho_cell+200, bloco.linha*self.tamanho_cell+11,
            self.tamanho_cell-1, self.tamanho_cell-1)
            pygame.draw.rect(screen, self.cores[self.id], bloco_rect)