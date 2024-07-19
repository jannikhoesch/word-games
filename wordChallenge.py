import random
import time
from trie import Trie


def interactive(trie):
    letters = input("Enter your letters: ")
    found_words = trie.find_words(letters)

    # Sort words
    found_words = sorted(found_words, key=lambda word: (len(word), word))
    if not found_words:
        print("No words found.")
    else:
        for word in found_words:
            print(word)


def automatic(trie, word_lengths):

    length = int(input("Enter word length: "))
    iterations = int(input("Enter number of iterations: "))

    words_found = 0
    total_cpu_time = 0

    for _ in range(iterations):

        # Pick a random word
        secret = random.choice(word_lengths[length])

        # Rearrange letters
        letters = list(secret)
        random.shuffle(letters)
        shuffled = ''.join(letters)

        print(shuffled)

        # Solve riddle
        start_time = time.time()
        found_words = trie.find_words(shuffled)
        end_time = time.time()

        words_found += len(found_words)
        total_cpu_time += (end_time - start_time)

    avg_words = words_found / iterations
    avg_cpu_time = total_cpu_time / iterations
    print(f"Average words found: {avg_words}")
    print(f"Average CPU time: {avg_cpu_time:.10f} seconds")


def play_wordChallenge():

    # Insert the dictionary words into the tree
    trie, word_lengths = Trie().load_dictionary("dictionary.txt")

    print("Choose mode:")
    print("1. Interactive")
    print("2. Automatic")
    choice = input("Enter choice (1-2): ")

    if choice == "1":
        interactive(trie)
    elif choice == "2":
        automatic(trie, word_lengths)
    else:
        print("Invalid choice.")


if __name__ == '__main__':
    play_wordChallenge()
