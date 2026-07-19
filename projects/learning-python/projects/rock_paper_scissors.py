# ### 7. Rock–paper–scissors with score tracking
# Best-of-N against the computer.
# - **Requirements:** play rounds until someone reaches N wins; track and display
#   the running score; reject invalid moves; announce the overall winner.
# - **You'll learn:** game loops, dict-based win logic (beats-table), state tracking.
# - **Stretch:** add lizard–Spock; log every game's result to a file.

import random
from helper import input_y_or_n, save_data, load_data

N = 5
round_count = 0
player_win_count = 0
computer_win_count = 0

FILE_NAME = "rock_paper_scissor_results.json"

outcome = {
    "rock": {
        "paper": False,
        "scissor": True,
        "rock": None,
    },
    "paper": {
        "rock": True,
        "scissor": False,
        "paper": None,
    },
    "scissor": {
        "rock": False,
        "paper": True,
        "scissor": None,
    },
}

valid_moves = {
    "r": "rock",
    "p": "paper",
    "s": "scissor",
    "rock": "rock",
    "paper": "paper",
    "scissor": "scissor",
}


def game():
    try:
        global round_count
        global player_win_count
        global computer_win_count

        print("\n=== new round ===")
        print(f"(player {player_win_count} - computer {computer_win_count})")
        player_move = input("player move: ")

        if player_move not in valid_moves:
            print("Invalid move.\n")
            return game()

        player_move = valid_moves[player_move]

        computer_move = random.choice(["rock", "paper", "scissor"])
        is_player_win = outcome[player_move][computer_move]

        print(f"computer move: {computer_move}")

        if is_player_win == None:
            print("result: tie!")
            print(f"{player_move} = {computer_move}")
        elif is_player_win:
            print("result: player won!")
            print(f"{player_move} > {computer_move}")
            player_win_count += 1
        else:
            print("result: player loss!")
            print(f"{player_move} < {computer_move}")
            computer_win_count += 1

        round_count += 1

        if player_win_count < N and computer_win_count < N:
            return game()
        else:
            return announcement()

    except Exception as e:
        print(f"Error: {e}")


def reset():
    global round_count
    global player_win_count
    global computer_win_count

    round_count = 0
    player_win_count = 0
    computer_win_count = 0

    return


def announcement():
    overall_winner = "player" if player_win_count > computer_win_count else "computer"

    print("\n=== end ===")
    print(f"player win: {player_win_count}")
    print(f"computer win: {computer_win_count}")
    print(f"overall winner: {overall_winner}")

    game_result = {
        "round_count": round_count,
        "player_win_count": player_win_count,
        "computer_win_count": computer_win_count,
        "overall_winner": overall_winner,
    }

    results = []
    persist = load_data(FILE_NAME)

    if not persist:
        persist = []

    results = persist
    results.append(game_result)

    save_data(FILE_NAME, results)

    play_again = input_y_or_n("play again? (y/n): ")

    if play_again:
        reset()
        game()
    else:
        exit()


def main():
    print("rock-paper-scissor game program.")
    print(
        f"The game end when either you or the computer win {N} {'time' if N>0 else 'times'}.\n"
    )
    print(f"You make a move by prompting: rock|paper|scissor or r|p|s")

    reset()
    game()


main()
