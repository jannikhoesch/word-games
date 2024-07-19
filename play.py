from wordle import play_wordle
from wordChallenge import play_wordChallenge


def main():
    print("Choose a game:")
    print("1. Word Challenge")
    print("2. Wordle")
    game_choice = input("Enter choice (1-2): ")

    if game_choice not in ["1", "2"]:
        print("Invalid choice.")
        return

    if game_choice == "1":
        play_wordChallenge()

    elif game_choice == "2":
        play_wordle()


if __name__ == "__main__":
    main()
