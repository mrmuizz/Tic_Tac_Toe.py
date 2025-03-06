# TicTacToe.py
# Name: [Your Name]
# Course: [Course Number]
# Section: [Section Number]
# Assignment: Assignment 1
# Date: [Date]

import random
import copy


# Function to display the game board
def show_board(grid):
    for i in range(3):
        print(f" {grid[i][0]} | {grid[i][1]} | {grid[i][2]} ")
        if i < 2:
            print("-----------")


# Function to check if someone has won
def check_win(grid, marker):
    # Check rows
    for i in range(3):
        if grid[i][0] == marker and grid[i][1] == marker and grid[i][2] == marker:
            return True

    # Check columns
    for i in range(3):
        if grid[0][i] == marker and grid[1][i] == marker and grid[2][i] == marker:
            return True

    # Check diagonals
    if grid[0][0] == marker and grid[1][1] == marker and grid[2][2] == marker:
        return True
    if grid[0][2] == marker and grid[1][1] == marker and grid[2][0] == marker:
        return True

    return False


# Function to check if the board is full
def is_full(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                return False
    return True


# Function to get a random empty spot for the computer (easy mode)
def random_move(grid):
    available_spots = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                available_spots.append((i, j))
    if len(available_spots) > 0:
        return random.choice(available_spots)
    return None


# Function to decide the computer's move (hard mode)
def smart_move(grid, comp, player):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = comp
                if check_win(grid, comp):
                    grid[i][j] = " "
                    return (i, j)
                grid[i][j] = " "

    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                grid[i][j] = player
                if check_win(grid, player):
                    grid[i][j] = " "
                    return (i, j)
                grid[i][j] = " "

    if grid[1][1] == " ":
        return (1, 1)

    for corner in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if grid[corner[0]][corner[1]] == " ":
            return corner

    return random_move(grid)


# Function to handle game logic
def start_game():
    last_game = []

    while True:
        print("\n1. Single player\n2. Two player\nD. Display last match\nQ. Quit")
        user_choice = input("What would you like to do: ").strip().upper()

        if user_choice == "1":
            difficulty = input("E: Easy\nM: Medium\nH: Hard\nWhich level do you want to play: ").strip().upper()
            player_name = input("Enter your name: ")
            comp_marker = "O"
            player_marker = "X"
            current_turn = player_marker if random.choice([True, False]) else comp_marker
            print("Tossing a coin...")
            print(f"{player_name if current_turn == player_marker else 'Computer'} goes first.")
            game_grid = [[" " for _ in range(3)] for _ in range(3)]
            move_history = []

            while True:
                show_board(game_grid)
                if current_turn == player_marker:
                    try:
                        r = int(input(f"{player_name}, enter row (0-2): "))
                        c = int(input(f"{player_name}, enter column (0-2): "))
                        if game_grid[r][c] != " ":
                            print("Invalid move. Try again.")
                            continue
                    except (ValueError, IndexError):
                        print("Invalid input. Try again.")
                        continue
                else:
                    if difficulty == "E":
                        move = random_move(game_grid)
                    elif difficulty == "H":
                        move = smart_move(game_grid, comp_marker, player_marker)
                    else:
                        if random.choice([True, False]):
                            move = random_move(game_grid)
                        else:
                            move = smart_move(game_grid, comp_marker, player_marker)
                    if move:
                        r, c = move
                        print(f"Computer plays at ({r}, {c})")

                game_grid[r][c] = current_turn
                move_history.append(copy.deepcopy(game_grid))

                if check_win(game_grid, current_turn):
                    show_board(game_grid)
                    print(f"{player_name if current_turn == player_marker else 'Computer'} wins!")
                    break
                if is_full(game_grid):
                    show_board(game_grid)
                    print("It's a draw!")
                    break

                current_turn = player_marker if current_turn == comp_marker else comp_marker

            last_game = move_history.copy()

        elif user_choice == "D":
            if last_game:
                print("Last Match Replay:")
                for move in last_game:
                    show_board(move)
                    print()
            else:
                print("No match found.")

        elif user_choice == "Q":
            print("Thanks for playing. Hope you had fun!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    start_game()
