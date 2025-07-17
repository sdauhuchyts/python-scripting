#!/usr/bin/env python3

sudoku = []

for i in range(9):
    while True:
        line = input(f"Please enter #{i} line: ")
        if not line.isdigit():
            print("Only digits are allowed")
            continue
        if len(line) != 9:
            print("Only 9 digits are allowed")
            continue
        break
    sudoku.append(line)

def is_valid(sudoku):
    valid = True

    for i in range(9):
        s_hor = 0
        s_ver = 0
        for j in range(9):
            s_hor += int(sudoku[i][j])
            s_ver += int(sudoku[j][i])
        if s_hor != 45 or s_ver != 45:
            valid = False
            break

    if not valid:
        return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s_cel = 0
            for k in range(3):
                for l in range(3):
                    s_cel += int(sudoku[i + k][j + l])
            if s_cel != 45:
                valid = False
                break
        if not valid:
            break

    return valid

print(is_valid(sudoku))
