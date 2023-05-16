import tkinter as tk
from tkinter import messagebox


# Функция создания доски
def create_board():
    for i in range(3):
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 50), height=1, width=3, bg="lightpink", command=lambda row=i, col=j: handle_click(row, col))
            button.grid(row=i, column=j, sticky="nsew")


# Функция для простановки значков Х и О во время игры
def handle_click(row, col):
    global current_player
    if board[row][col] == 0:
        if current_player == 1:
            board[row][col] = "X"
            current_player = 2
        else:
            board[row][col] = "O"
            current_player = 1
        button = window.grid_slaves(row=row, column=col)[0]
        button.config(text=board[row][col])
        check_for_winner()

# Проверка окончания игры: выигрыш или ничья
def check_for_winner():
    winner = None
    # Проверка по строкам
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            winner = row[0]
            break
    # Проверка по столбцам
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            winner = board[0][col]
            break
    # Проверка по диагоналям
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        winner = board[0][2]
    if all([all(row) for row in board]) and winner is None:
        winner = "ничья"
    if winner:
        declare_winner(winner)

# Окно для вывода победителя или объявления ничьи
def declare_winner(winner):
    if winner == "ничья":
        message = "Ничья! "
    else:
        message = f"Игрок {winner} победил! "

    answer = messagebox.askyesno("Игра окончена", message + "Хотите начать новую игру?")
    if answer:
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                button.config(text="")
        global current_player
        current_player = 1
    else:
        window.quit()


window = tk.Tk()
window.title("Крестики-нолики")
create_board()
# Initialize variables
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1
window.mainloop()
