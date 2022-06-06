from seabattle.game.const import *


def check(size, mas, ship_x, ship_y):
    N = size - 1

    # TODO проверка для многопалубных кораблей, что они разположены по горизонтали или вертикали
    def check_line():
        return True

    def check_neighbors():
        return (ship_x == 0 or mas[ship_x - 1][ship_y] == FIELD_EMPTY) and \
               (ship_x == N or mas[ship_x + 1][ship_y] == FIELD_EMPTY) and \
               (ship_y == 0 or mas[ship_x][ship_y - 1] == FIELD_EMPTY) and \
               (ship_y == N or mas[ship_x][ship_y + 1] == FIELD_EMPTY) and \
               (ship_x == 0 or ship_y == 0 or mas[ship_x - 1][ship_y - 1] == FIELD_EMPTY) and \
               (ship_x == N or ship_y == N or mas[ship_x + 1][ship_y + 1] == FIELD_EMPTY) and \
               (ship_y == 0 or ship_x == N or mas[ship_x + 1][ship_y - 1] == FIELD_EMPTY) and \
               (ship_y == N or ship_x == 0 or mas[ship_x - 1][ship_y + 1] == FIELD_EMPTY)

    return check_neighbors()
