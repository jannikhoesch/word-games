import random
import time
from trie import Trie


def choose_word(word_lengths, length):
    if length not in word_lengths:
        return None
    words = word_lengths[length]
    return random.choice(words)


def generate_feedback(secret_word, guess):
    feedback = []
    for i, char in enumerate(guess):
        if char == secret_word[i]:
            feedback.append('2')  # Correct position
        elif char in secret_word:
            feedback.append('1')  # Wrong position
        else:
            feedback.append('0')  # Not in word
    return "".join(feedback)


def filter_words(valid_words, guess, feedback):
    new_valid_words = []
    for word in valid_words:
        match = True
        for i, char in enumerate(guess):
            if feedback[i] == '2' and word[i] != char:
                match = False
                break
            if feedback[i] == '1' and (char not in word or word[i] == char):
                match = False
                break
            if feedback[i] == '0' and char in word:
                match = False
                break
        if match:
            new_valid_words.append(word)
    return new_valid_words


def guesser(word_lengths, length):

    # Pick a random word
    secret = choose_word(word_lengths, length)
    if not secret:
        print("No words of this length.")
        return

    max_guesses = 6
    print(f"Guess the word. Length: {length}")

    for attempt in range(1, max_guesses + 1):

        # Ask for guess
        guess = input("Enter your guess: ")
        if len(guess) != length:
            print("Invalid guess length.")
            continue

        # Generate feedback
        feedback = generate_feedback(secret, guess)
        print("Feedback:", feedback)

        # Correct guess
        if feedback == "2" * length:
            print("You guessed correctly!")
            return

    print("Max guesses reached. Secret word was:", secret)


def keeper(word_lengths, length):

    # Pick a random word
    secret = choose_word(word_lengths, length)
    if not secret:
        print("No words of this length.")
        return
    valid_words = word_lengths[length].copy()

    max_guesses = 6
    for attempt in range(1, max_guesses + 1):

        # Select word as guess
        guess = random.choice(valid_words)
        print("Computer's guess:", guess)

        # Ask for feedback
        feedback = input("Enter feedback: ")

        # Correct guess
        if feedback == "2" * length:
            print("Computer guessed correctly!")
            return

        # Update list of valid words
        valid_words = filter_words(valid_words, guess, feedback)

    print("Max guesses reached. Secret word was:", secret)


def automatic(word_lengths, length, iterations):

    total_attempts = 0
    cpu_time = 0

    for _ in range(iterations):

        # Pick a random word
        secret = choose_word(word_lengths, length)
        valid_words = word_lengths[length].copy()

        start_time = time.time()
        for attempt in range(1, 7):

            # Select guess
            guess = random.choice(valid_words)

            # Receive feedback
            feedback = generate_feedback(secret, guess)

            # Correct guess
            if feedback == "2" * length:
                total_attempts += attempt
                break

            # Update list of valid words
            valid_words = filter_words(valid_words, guess, feedback)

        end_time = time.time()
        cpu_time += end_time - start_time

    avg_attempts = total_attempts / iterations
    avg_cpu_time = cpu_time / iterations
    print(f"Average Attempts: {avg_attempts}")
    print(f"Average CPU Time: {avg_cpu_time:.10f} seconds")


def play_wordle():

    # Insert the dictionary words into the tree
    trie, word_lengths = Trie().load_dictionary("dictionary.txt")

    print("Choose mode:")
    print("1. Play as Guesser")
    print("2. Play as Keeper")
    print("3. Automatic Mode")
    choice = input("Enter choice (1-3): ")
    length = int(input("Enter word length: "))

    if choice == "1":
        guesser(word_lengths, length)
    elif choice == "2":
        keeper(word_lengths, length)
    elif choice == "3":
        iterations = int(input("Enter number of iterations: "))
        automatic(word_lengths, length, iterations)
    else:
        print("Invalid choice.")


if __name__ == '__main__':
    play_wordle()
