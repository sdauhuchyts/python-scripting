#!/usr/bin/env python3

from random import randrange

def display_board(board):
    for row in range(3):
        print(("+" + "-"*7)*3 + "+")
        print(("|" + " "*7)*3 + "|")
        for column in range(3):
            print("|" + " "*3 + str(board[row][column]) + " " * 3, end="")
        print("|")
        print(("|" + " "*7)*3 + "|")
    print(("+" + "-"*7)*3 + "+")

def enter_move(board):
    while True:
        try:
            user_move = int(input("Enter your move: "))
            if user_move not in range(1, 10):
                print("Sorry, you are out of board range")
                continue
            row = (user_move - 1) // 3
            column = (user_move - 1) % 3
            if board[row][column] in ['X', 'O']:
                print("Sorry, this field is occupied")
                continue
            break
        except ValueError:
            print("Please enter integer value")
        except:
            print("Sorry, something went wrong")
    board[row][column] = 'O'

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for column in range(3):
            if board[row][column] in range(1, 10):
                free_fields.append((row, column))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    cross1 = cross2 = True
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:
            return True
        if board[i][2 - i] != sign:
            cross1 = False
        if board[i][i] != sign:
            cross2 = False
    if cross1 or cross2:
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pc_move = randrange(len(make_list_of_free_fields(board)))
    row, column = make_list_of_free_fields(board)[pc_move]
    board[row][column] = 'X'

board = [
    [1, 2, 3],
    [4, 'X', 6],
    [7, 8, 9]
    ]

turn = "user"

while True:
    display_board(board)
    if victory_for(board, 'X'):
        print("PC won")
        break
    elif victory_for(board, 'O'):
        print("You won")
        break
    elif len(make_list_of_free_fields(board)) == 0:
        print("Draw")
        break
    else:
        if turn == "user":
            enter_move(board)
            turn = "pc"
            continue
        elif turn == "pc":
            draw_move(board)
            turn = "user"
            continue
