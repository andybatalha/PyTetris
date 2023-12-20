import pygame

pygame.init()
screen = pygame.display.set_mode((700, 620))
pygame.display.set_caption("Python Tetris")

background1 = pygame.image.load('Backgrounds\\Tetris_Background.png').convert()
background2 = pygame.image.load('Backgrounds\\Tetris_Background2.png').convert()


class Fontes:
    fonte_tipo1 = 'Fontes\\Heavitas.ttf'
    fonte_tipo2 = 'Fontes\\upheavtt.ttf'
    fonte1 = pygame.font.Font(fonte_tipo1, 30)
    fonte2 = pygame.font.Font(fonte_tipo2, 50)



