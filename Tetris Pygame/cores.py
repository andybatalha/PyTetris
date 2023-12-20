class Cores:
    cinza_escuro = (26, 31, 40)
    verde = (47, 230, 23)
    vermelho = (232, 18, 18)
    laranja = (226, 116, 17)
    amarelo = (237, 234, 4)
    roxo = (166, 0, 247)
    ciano = (21, 204, 209)
    azul = (13, 64, 216)
    branco = (255, 255, 255)
    azul_roxo = (44, 44, 127)
    azul_escuro = (25, 25, 112)
    cinza = (128, 128, 128)
    preto = (0, 0, 0)
    cinza_transparente = (128, 128, 128, 128)

    @classmethod
    def cores_cell(cls): # 0         # 1         # 2         # 3            # 4        # 5        # 6        # 7
        return [cls.cinza_escuro, cls.verde, cls.vermelho, cls.laranja, cls.amarelo, cls.roxo, cls.ciano, cls.azul]
    # @classmethod é um decorador python que permite definir um método que pode ser chamado em uma classe ao invez
    # de uma instancia da classe, dessa forma é possivel acessar os atributos da classe