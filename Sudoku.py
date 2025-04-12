from Board import Board
from Box import Box
def sub_div(pointer):
    row_group = pointer[0] // 3
    col_group = pointer[1] // 3
    pointer[2] = row_group * 3 + col_group + 1
    return pointer
def avancer(pointer: list, sens: int, box: Box, base=False):
    def move_forward():
        pointer[1] += 1
        if pointer[1] == 9:
            pointer[1] = 0
            pointer[0] += 1
        return sub_div(pointer)

    def move_backward():
        pointer[1] -= 1
        if pointer[1] == -1:
            pointer[1] = 8
            pointer[0] -= 1
        return sub_div(pointer)

    if base:
        pointer = move_forward() if sens == 1 else move_backward()
        return

    if sens == 1:
        box.arrival(box.possible[0])
        box.possible.pop(0)
        pointer = move_forward()
    else:
        box.leave()
        pointer = move_backward()
def solve(j: Board):
    pointer = [0, 0, 1]
    '''the pointer is defined as the coordinate and the sub-division'''
    sens = 1
    if not j.is_solvable():
        return False

    if j.soluce is not None:
        j.terrain = j.soluce
        return j

    while True:
        if not process_cell(j, pointer, sens):
            break
        print(pointer)
        if pointer == [9, 0, 10]:
            return j


def process_cell(j: Board, pointer: list, sens: int) -> bool:
    cell = j.terrain[pointer[0]][pointer[1]]
    if not cell.base:
        if not handle_non_base_cell(j, pointer, sens, cell):
            return False
    else:
        handle_base_cell(j, pointer, cell)
    return True


def handle_non_base_cell(j: Board, pointer: list, sens: int, cell: Box) -> bool:
    if not cell.possible:
        if sens == -1:
            return False
        cell.possible = [i for i in range(1, len(j.terrain) + 1)]

    while cell.possible:
        i = cell.possible[0]
        print(pointer)
        if is_valid_move(j, pointer, i):
            sens = 1
            break
        else:
            cell.possible.pop(0)
            sens = -1

    avancer(pointer, sens, cell)
    j.update()
    return True


def handle_base_cell(j: Board, pointer: list, cell: Box):
    cell.possible = [i for i in range(1, 10) if i not in [cell.occupant]]
    avancer(pointer, 1, cell, True)
    j.update()


def is_valid_move(j: Board, pointer: list, value: int) -> bool:
    return not j.check_ligne(pointer[0], value) and not j.check_column(pointer[1], value) and not j.check_subdiv(pointer[2], value)
    

if __name__=="__main__":
    Board1=Board()
    Board1.set_terrain([
        [0,0,0,0,0,0,6,0,2],
        [0,6,2,8,7,0,0,3,4],
        [3,4,1,9,0,0,0,7,8],
        [0,9,6,7,2,8,4,0,3],
        [0,0,4,6,0,3,0,1,0],
        [0,5,0,0,0,0,7,0,6],
        [7,0,9,1,0,6,2,0,5],
        [0,0,0,0,3,7,0,0,1],
        [0,1,5,2,8,9,0,6,0]
    ])
    Board2=Board()
    Board2.set_terrain([
        [0,0,1,0,0,0,0,0,0],
        [8,0,0,0,0,0,0,9,4],
        [0,9,0,0,0,0,0,0,0],
        [0,0,8,0,0,4,0,7,0],
        [0,0,0,0,0,1,0,0,0],
        [0,0,0,5,0,0,3,0,2],
        [0,0,5,1,0,2,0,0,0],
        [4,3,0,0,0,9,0,0,0],
        [0,1,0,0,0,3,0,0,0]
    ])
    Board3=Board()
    Board3.set_terrain([
        [8,7,5,3,6,2,9,1,4],
        [0,0,3,0,0,0,0,0,0],
        [0,0,0,0,0,5,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [2,0,0,5,0,0,0,9,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,7,0,0],
        [0,3,0,0,5,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ])
    Board4=Board()
    Board4.set_terrain([
        [9,4,0,0,3,8,0,0,0],
        [0,0,0,0,0,0,9,6,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,3],
        [1,5,0,0,0,0,0,0,0],
        [0,0,0,0,5,4,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,7,2,0],
        [4,0,0,0,0,3,5,0,0]
    ])

    # print(Board3)
    print(solve(Board1))
    # print(Board3)