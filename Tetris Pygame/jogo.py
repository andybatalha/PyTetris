import pygame, sys
from grid import Grid
from blocks import *
from cores import Cores
import random


class Jogo:
    # Construtor da classe jogo,
    # Define variaveis para o controle do jogo, gameover e score
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.bloco_atual = self.bloco_aleatorio()
        self.proximo_bloco = self.bloco_aleatorio()
        self.game_over = False
        self.score = 0
        self.pause = False

    # Atualiza a pontuação do jogador com base nas linhas que foram limpas
# Adicionando pontos de acordo com o número de linhas limpas
    def atualizar_score(self, linhas_limpas, blocos_para_baixo):
        self.score += blocos_para_baixo
        if linhas_limpas == 1:
            self.score += 100
        elif linhas_limpas == 2:
            self.score += 250
        elif linhas_limpas == 3:
            self.score += 450
        elif linhas_limpas == 4:
            self.score += 600
        elif linhas_limpas > 4:
            self.score += 1000

# Escolhe um bloco aleatorio da lista e remove o bloco da lista para evitar repetição
# Quando a lista fica vazia (==0) a lista self.blocks è reabastecida.
    def bloco_aleatorio(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        bloco = random.choice(self.blocks)
        self.blocks.remove(bloco)
        return bloco

# Verifica se todas as celuas do bloco atual estao dentro do grid. Retorna True se estiver dentro e False caso contraio.
    def bloco_dentro(self):
        blocos = self.bloco_atual.posicao_cell()
        for bloco in blocos:
            if not self.grid.esta_dentro(bloco.linha, bloco.coluna):
                return False
        return True

# função de movimento para a esquerda
# move o bloco atual para a esquerda quando chamada no main.py
    def move_esquerda(self):
        self.bloco_atual.move(0, -1)
        if not self.bloco_dentro() or not self.encaixar_bloco():
            self.bloco_atual.move(0, 1)

# função de movimento para a direita
# move o bloco atual para a direita quando chamada no main.py
    def move_direita(self):
        self.bloco_atual.move(0, 1)
        if not self.bloco_dentro() or not self.encaixar_bloco():
            self.bloco_atual.move(0, -1)

# função de movimento para baixo
# move o bloco atual para baixo quando chamada no main.py
    def move_baixo(self):
        self.bloco_atual.move(1, 0)
        if not self.bloco_dentro() or not self.encaixar_bloco():
            self.bloco_atual.move(-1, 0)
            self.travar_bloco()

# Verifica se a rotação é possivel, se nao for, reverte a rotação
    def girar(self):
        self.bloco_atual.girar()
        if not self.bloco_dentro() or not self.encaixar_bloco():
            self.bloco_atual.cancelar_giro()

# reinicia o jogo, redefine o grid, a lista de blocos, o score, o bloco atual e proximo
    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.bloco_atual = self.bloco_aleatorio()
        self.proximo_bloco = self.bloco_aleatorio()
        self.score = 0
        self.num_blocos = 0

# verifica se o bloco atual se encaixa no grid, verifica colisão, se as celulas onde o bloco esta estao vazias
    def encaixar_bloco(self):
        blocos = self.bloco_atual.posicao_cell()
        for bloco in blocos:
            if not self.grid.esta_vazio(bloco.linha, bloco.coluna):
                return False
        return True

    def travar_bloco(self):
        blocos = self.bloco_atual.posicao_cell() # Obtem a posição atual de todas as celulas do bloco atual
        for posicao in blocos: # itera sobre cada posição do bloco atual
            # Define no grid a posição ocupada pelo bloc atual com o ID correspondente.
            self.grid.grid[posicao.linha][posicao.coluna] = self.bloco_atual.id
        # Atualiza o bloco atual para ser o proximo bloco que estava armazenado
        self.bloco_atual = self.proximo_bloco
        # Gera um novo bloco aleatorio para ser o proximo bloco
        self.proximo_bloco = self.bloco_aleatorio()
        # Verifica se existem linhas preenchidas na grade e as limpa, se houver, retorna o numero de linahs limpas
        linhas_limpas = self.grid.limpar_linhas_cheias()
        # Atualiza a pontuação do jogador com base no numero de linhas limpas e de blocos para baixo
        self.atualizar_score(linhas_limpas, 0)
        # Verifica se o proximo bloco podee ser encaixado no grid, se nao puder, define game over como True
        if not self.encaixar_bloco():
            self.game_over = True

# Desenha a grade e o bloco atual na tela usando as funções de densenho do bloco atual de __init__
# e draw do arquivo grid.py
    def desenhar(self, screen):
        self.grid.draw(screen)
        self.bloco_atual.draw(screen)
