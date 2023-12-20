from block import Block
from posicao import Posicao


class LBlock(Block):  # Dessa maneira, LBlock è filha da classe Block
    def __init__(self):
        super(). __init__(id=3)  # chamar o método init da classe mãe
        self.celulas = {
            0: [Posicao(0, 2), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(2, 2)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 0)],
            3: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 1), Posicao(2, 1)]
        }
        self.move(0, 3)  # o bloco aparece na coluna do meio


class JBlock(Block):
    def __init__(self):
        super().__init__(id=7)
        self.celulas = {
            0: [Posicao(0, 0), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(0, 2), Posicao(1, 1), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 2)],
            3: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 0), Posicao(2, 1)]
        }
        self.move(0, 3)


class IBlock(Block):
    def __init__(self):
        super().__init__(id=6)
        self.celulas = {
            0: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(1, 3)],
            1: [Posicao(0, 2), Posicao(1, 2), Posicao(2, 2), Posicao(3, 2)],
            2: [Posicao(2, 0), Posicao(2, 1), Posicao(2, 2), Posicao(2, 3)],
            3: [Posicao(0, 1), Posicao(1, 1), Posicao(2, 1), Posicao(3, 1)]
        }
        self.move(-1, 3)


class OBlock(Block):
    def __init__(self):
        super().__init__(id=4)
        self.celulas = {
            0: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 0), Posicao(1, 1)],
            1: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 0), Posicao(1, 1)],
            2: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 0), Posicao(1, 1)],
            3: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 0), Posicao(1, 1)]
        }
        self.move(0, 2)


class SBlock(Block):
    def __init__(self):
        super().__init__(id=1)
        self.celulas = {
            0: [Posicao(0, 1), Posicao(0, 2), Posicao(1, 0), Posicao(1, 1)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(1, 2), Posicao(2, 2)],
            2: [Posicao(1, 1), Posicao(1, 2), Posicao(2, 0), Posicao(2, 1)],
            3: [Posicao(0, 0), Posicao(1, 0), Posicao(1, 1), Posicao(2, 1)]
        }
        self.move(0, 3)


class TBlock(Block):
    def __init__(self):
        super().__init__(id=5)
        self.celulas = {
            0: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 1), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            3: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(2, 1)]
        }
        self.move(0, 3)


class ZBlock(Block):
    def __init__(self):
        super().__init__(id=2)
        self.celulas = {
            0: [Posicao(0, 0), Posicao(0, 1), Posicao(1, 1), Posicao(1, 2)],
            1: [Posicao(0, 2), Posicao(1, 1), Posicao(1, 2), Posicao(2, 1)],
            2: [Posicao(1, 0), Posicao(1, 1), Posicao(2, 1), Posicao(2, 2)],
            3: [Posicao(0, 1), Posicao(1, 0), Posicao(1, 1), Posicao(2, 0)]
        }
        self.move(0, 3)


