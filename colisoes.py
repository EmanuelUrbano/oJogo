def collisaEsquerdaParedeVertical(de, ate, px, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == px and pos_y == i:
            pos_x += 10
    return pos_x
def collisaDireitaVertical(de, ate, px, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == px and pos_y == i:
            pos_x -= 10
    return pos_x
def collisaCimaHorizontal(de, ate, py, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == i and pos_y == py:
            pos_y += 10
    return pos_y
def collisaBaixoHorizontal(de, ate, py, pos_x, pos_y):
    for i in range(de,ate):
        if pos_x == i and pos_y == py:
            pos_y -= 10
    return pos_y