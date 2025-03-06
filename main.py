# TicTacToe.py
# Name: [Your Name]
# Course: [Course Number]
# Section: [Section Number]
# Assignment: Assignment 1
# Date: [Date]

import random
import copy


# Function to display the game board
def display_grid(board):
    print("\nCurrent Board:")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("-----------")


# Function to check if a player has won
def has_winner(board, symbol):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == symbol for j in range(3)) or all(board[j][i] == symbol for j in range(3)):
            return True
    # Check diagonals
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False


# Function to check if the board is full
def board_is_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))


# Function to get a random move for the computer (Easy mode)
def find_random_spot(board):
    available_spots = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(available_spots) if available_spots else None


# Function to get the best move for the computer (Hard mode)
def best_move(board, ai_symbol, player_symbol):
    # Check if AI can win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai_symbol
                if has_winner(board, ai_symbol):
                    board[i][j] = " "
                    return (i, j)
                board[i][j] = " "
    # Block opponent from winning
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player_symbol
                if has_winner(board, player_symbol):
                    board[i][j] = " "
                    return (i, j)
                board[i][j] = " "
    # Choose center, then corners, then any available space
    if board[1][1] == " ":
        return (1, 1)
    for corner in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[corner[0]][corner[1]] == " ":
            return corner
    return find_random_spot(board)


# Main game loop
def run_game():
    last_match = []
    while True:
        print("\n1. Single player\n2. Two player\nD. Display last match\nQ. Quit")
        user_choice = input("What would you like to do: ").strip().upper()

        if user_choice == "1":
            player_name = input("Enter your name: ")
            difficulty = input("E: Easy\nM: Medium\nH: Hard\nChoose difficulty: ").strip().upper()
            computer_symbol, player_symbol = "O", "X"
            current_turn = player_symbol if random.choice([True, False]) else computer_symbol
            print("Tossing a coin...", f"{player_name if current_turn == player_symbol else 'Computer'} goes first.")
            game_board = [[" " for _ in range(3)] for _ in range(3)]
            match_history = []

            while True:
                display_grid(game_board)
                if current_turn == player_symbol:
                    try:
                        r, c = int(input(f"{player_name}, enter row (0-2): ")), int(input("Enter column (0-2): "))
                        if game_board[r][c] != " ":
                            print("Invalid move. Try again.")
                            continue
                    except (ValueError, IndexError):
                        print("Invalid input. Try again.")
                        continue
                else:
                    move = find_random_spot(game_board) if difficulty == "E" else best_move(game_board, computer_symbol,
                                                                                            player_symbol)
                    if difficulty == "M" and random.choice([True, False]):
                        move = find_random_spot(game_board)
                    if move:
                        r, c = move
                        print(f"Computer plays at ({r}, {c})")

                game_board[r][c] = current_turn
                match_history.append(copy.deepcopy(game_board))

                if has_winner(game_board, current_turn):
                    display_grid(game_board)
                    print(f"{player_name if current_turn == player_symbol else 'Computer'} wins!")
                    break
                if board_is_full(game_board):
                    display_grid(game_board)
                    print("It's a draw!")
                    break
                current_turn = player_symbol if current_turn == computer_symbol else computer_symbol
            last_match = match_history.copy()

        elif user_choice == "D":
            if last_match:
                print("Last Match Replay:")
                for move in last_match:
                    display_grid(move)
                    print()
            else:
                print("No match found.")

        elif user_choice == "Q":
            print("Thanks for playing. Hope you had fun!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    run_game()
