from screen import Screen


def battle():
    altura = 600
    largura = 1230
    scren = Screen(altura, largura, 10, (0, 0, 0))
    scren.criarTel()
    running = True
    while running:
        scren.pntEsa()
        scren.atualiEfps()
