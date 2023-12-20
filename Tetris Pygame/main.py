import pygame, sys
import time
from arquivos import Fontes, background1, background2
from jogo import Jogo
from cores import Cores


# game_grid = Grid()
# game_grid.print_grid()

pygame.init()
screen = pygame.display.set_mode((700, 620))
texto_score = Fontes.fonte1.render("Score", True, Cores.branco)
texto_timer = Fontes.fonte1.render("Timer", True, Cores.branco)
retangulo_score = pygame.Rect(41, 495, 120, 90)
retangulo_timer = pygame.Rect(41, 380, 120, 90)

pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()
jogo = Jogo()
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

MENU = 0
JOGANDO = 1
FINAL = 2
VENCER = 3
estado = MENU


def menu():
    while True:
        screen.blit(background1, (0, 0))
        texto_menu = Fontes.fonte2.render("PyTETRIS", True, Cores.branco)
        texto_rect = texto_menu.get_rect()
        texto_rect.center = (screen.get_width() // 2, screen.get_height() // 2 -200)
        screen.blit(texto_menu, texto_rect)

        # Desenhar botão Play
        texto_play = Fontes.fonte2.render("Play", True, Cores.branco)
        texto_rect = texto_play.get_rect()
        texto_rect.center = (screen.get_width() // 2, screen.get_height() // 2 -30)
        screen.blit(texto_play, texto_rect)

        # Desenhar botão Quit
        texto_quit = Fontes.fonte2.render("Quit", True, Cores.branco)
        texto_rect = texto_quit.get_rect()
        texto_rect.center = (screen.get_width() // 2, screen.get_height() // 2 + 40)
        screen.blit(texto_quit, texto_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                if 270 <= posicao_mouse[0] <= 430:
                    if 260 <= posicao_mouse[1] <= 300:
                        # Se o botão "Play" for pressionado
                        return JOGANDO  # Muda para o estado JOGANDO
                    elif 340 <= posicao_mouse[1] <= 370:
                        pygame.quit()
                        sys.exit()


def jogando():
    tempo_total = 120
    tempo_inicio = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not jogo.game_over:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        jogo.move_esquerda()
                    if event.key == pygame.K_RIGHT:
                        jogo.move_direita()
                    if event.key == pygame.K_DOWN:
                        jogo.move_baixo()
                        jogo.atualizar_score(0, 1)
                    if event.key == pygame.K_UP:
                        jogo.girar()
                if event.type == GAME_UPDATE and not jogo.game_over:
                    jogo.move_baixo()
        tempo_passado = time.time() - tempo_inicio
        tempo_restante = tempo_total - tempo_passado
        if tempo_restante <= 0:
            jogo.game_over = True
        elif jogo.score >= 1000:
            return VENCER
        if jogo.game_over:
            return FINAL
        else:

            screen.blit(background2, (0, 0))
            pygame.draw.rect(screen, Cores.cinza, (198, 9, 302, 602))

    # Desenha a caixa do score, valor do score, e nome score.
            valor_score = Fontes.fonte1.render(str(jogo.score), True, Cores.branco)
            valor_score_rect = valor_score.get_rect()
            valor_score_rect.centerx = retangulo_score.centerx
            valor_score_rect.centery = retangulo_score.centery + 15
            pygame.draw.rect(screen, Cores.cinza, retangulo_score, 0, 10)
            screen.blit(valor_score, valor_score_rect)
            screen.blit(texto_score, (45, 500, 50, 50))
    # Desenha a caixa do timer, valor do timer, e o nome timer.
            tempo = f"{int(tempo_restante)}s"
            valor_timer = Fontes.fonte1.render(tempo, True, Cores.branco)
            valor_timer_rect = valor_timer.get_rect()
            valor_timer_rect.centerx = retangulo_timer.centerx
            valor_timer_rect.centery = retangulo_timer.centery + 15
            pygame.draw.rect(screen, Cores.cinza, retangulo_timer, 0, 10)
            screen.blit(valor_timer, valor_timer_rect)
            screen.blit(texto_timer, (50, 385, 50, 50))

            jogo.desenhar(screen)
            pygame.display.update()
            clock.tick(60)


def final():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                if 270 <= posicao_mouse[0] <= 430:
                    if 285 <= posicao_mouse[1] <= 330:
                        jogo.game_over = False
                        jogo.reset()
                        return JOGANDO
                    elif 360 <= posicao_mouse[1] <= 400:
                        pygame.quit()
                        sys.exit()
        texto_game_over = Fontes.fonte2.render("Game Over", True, Cores.branco)
        screen.blit(background1, (0, 0))
        # pygame.draw.rect(screen, (25, 25, 112), (41, 495, 120, 90), 0, 10)
        # screen.blit(texto_score, (45, 500, 50, 50))
        texto_game_over_rect = texto_game_over.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 70))
        screen.blit(texto_game_over, texto_game_over_rect)

        botao_quit = Fontes.fonte2.render("QUIT", True, Cores.branco)
        botao_quit_rect = botao_quit.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 70))
        screen.blit(botao_quit, botao_quit_rect)

        botao_restart = Fontes.fonte2.render("RESTART", True, Cores.branco)
        botao_restart_rect = botao_restart.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(botao_restart, botao_restart_rect)
        pygame.display.update()


def vencer():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicao_mouse = pygame.mouse.get_pos()
                if 270 <= posicao_mouse[0] <= 430:
                    if 285 <= posicao_mouse[1] <= 330:
                        jogo.game_over = False
                        jogo.reset()
                        return JOGANDO
                    elif 360 <= posicao_mouse[1] <= 400:
                        pygame.quit()
                        sys.exit()
            texto_game_over = Fontes.fonte2.render("Você Venceu!", True, Cores.branco)
            screen.blit(background1, (0, 0))
            # pygame.draw.rect(screen, (25, 25, 112), (41, 495, 120, 90), 0, 10)
            # screen.blit(texto_score, (45, 500, 50, 50))
            texto_game_over_rect = texto_game_over.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 70))
            screen.blit(texto_game_over, texto_game_over_rect)

            botao_quit = Fontes.fonte2.render("QUIT", True, Cores.branco)
            botao_quit_rect = botao_quit.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 70))
            screen.blit(botao_quit, botao_quit_rect)

            botao_restart = Fontes.fonte2.render("RESTART", True, Cores.branco)
            botao_restart_rect = botao_restart.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(botao_restart, botao_restart_rect)
            pygame.display.update()





while True:
    if estado == MENU:
        estado = menu()
    elif estado == JOGANDO:
        estado = jogando()
    elif estado == FINAL:
        estado = final()
    elif estado == VENCER:
        estado = vencer()
