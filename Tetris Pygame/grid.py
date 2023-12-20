import pygame
from cores import Cores  # importando as cores


class Grid:
    # Este é o construtor da classe Grid,chamado quando a instancia grid é gerada. Define as propriedades iniciais
    # do objeto, num_linhas, num_colunas, tamanho_cell e inicializa a matriz grid com zeros.
    def __init__(self):
        self.num_linhas = 20
        self.num_colunas = 10
        self.tamanho_cell = 30
        self.grid = [[0 for j in range(self.num_colunas)] for i in range(self.num_linhas)]  # Cria uma matriz de zeros
        self.cores = Cores.cores_cell()  # usando as cores de cores.py

    # O grid do Tetris é formando por 10 colunas e 20 linhas, o grid inicial está sendo formado apenas por 0
    # Existem 7 cores de peças no tetris, cada cor vai ser identificada por numeros de 1 a 7
    # Quando uma peça aparecer o os 0 do local em que a peça esta, sera substituido pelo numero da cor correspondente
    def print_grid(self):  # essa função imprime as colunas no console para ver se esta funcionando
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                print(self.grid[linha][coluna], end=" ")
            print()

    # verifica se as coordenadas (linha, coluna) estão dentro dos limites da grade, se estiverem retorna True
    # caso contrario retorna False
    def esta_dentro(self, linha, coluna):
        if 0 <= linha < self.num_linhas and 0 <= coluna < self.num_colunas:
            return True
        else:
            return False

    # Verifica se a linha especificada está completamente preenchida com valores diferentes de zero
    # Retorna True se estiver, False caso contrário.
    def linha_cheia(self, linha):
        for coluna in range(self.num_colunas):
            if self.grid[linha][coluna] == 0:
                return False
        return True

    # Move uma linha para baixo no grid
    def mover_linha(self, linha, num_linhas):
        for coluna in range(self.num_colunas):
            self.grid[linha + num_linhas][coluna] = self.grid[linha][coluna]
            self.grid[linha][coluna] = 0

    # Limpa uma linha especifica, definindo todos os valores para zero novamente
    def limpar_linha(self, linha):
        for coluna in range(self.num_colunas):
            self.grid[linha][coluna] = 0

    # Verifica e limpa todas as linhas completas no grid
    # Usa 'linha_cheia' para encontrar linhas completas e 'limpar_linha' para remover.
    def limpar_linhas_cheias(self):
        completo = 0
        for linha in range(self.num_linhas - 1, 0, -1):
            if self.linha_cheia(linha):
                self.limpar_linha(linha)
                completo += 1
            elif completo > 0:
                self.mover_linha(linha, completo)
        return completo

    # Verifica se a célula esta vazia. Retorna True se estiver.
    def esta_vazio(self, linha, coluna):
        if self.grid[linha][coluna] == 0:
            return True
        else:
            return False

    # Desenha o grid na tela usando pygame. Itera por cada célula na grade e desenh um
    # rect na posição correspondente
    def draw(self, screen):  # função para desenhar
        for linha in range(self.num_linhas):  # Utiliza dois loops "for" para percorrer cada célula no grid,
            for coluna in range(self.num_colunas): # percorrendo todas as linhas e colunas.
                valor_cell = self.grid[linha][coluna]
                # "valor_cell = self.grid[linha][coluna]" obtem o valor da celula na posição atual da iteração
                cell_rect = pygame.Rect(coluna * self.tamanho_cell + 200, linha * self.tamanho_cell+11,
                                        self.tamanho_cell-1, self.tamanho_cell-1)
                # Cria um retângulo (pygame.Rect) para representar a célula na tela.
                # coluna * self.tamanho_cell + 200: Determina a posição horizontal do retângulo baseado na coluna atual
# multiplicada pelo tamanho da célula, com um deslocamento de 200 pixels para a direita.
                # linha * self.tamanho_cell + 11: Determina a posição vertical do retângulo baseado na linha atual
# multiplicada pelo tamanho da célula, com um deslocamento de 11 pixels para baixo.
                # self.tamanho_cell - 1: Define a largura do retângulo como o tamanho da célula menos um pixel.
                # self.tamanho_cell - 1: Define a altura do retângulo como o tamanho da célula menos um pixel.
                pygame.draw.rect(screen, self.cores[valor_cell], cell_rect)
                # Desenha um rect na tela. self.colors[valor_cell] obtém a cor correspondente ao valor da célula atual
# da grade a partir da lista self.colors
                # cell_rect representa o retângulo a ser desenhado na tela com a cor apropriada.

                # (surface, cor, rect) desenha os objetos e a cores das celulas
                # as celulas são 30x30 e para parecer as divisões entre eles, reduzi as celulas para 29x29


    # Define todos os valores no grid de volta para zero. Usado para reiniciar o jogo.
    def reset(self):
        for linha in range(self.num_linhas):
            for coluna in range(self.num_colunas):
                self.grid[linha][coluna] = 0



