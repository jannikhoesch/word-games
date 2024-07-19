# Word Games

This repository contains a university project that I created for the course Advanced Data Structures at the Universitat Politècnica de Catalunya. The goal is to implement an application capable of playing two word-based games: Word Challenge and Wordle. Both games, while different in their gameplay mechanics, challenge players to deduce or construct words from a given set of letters, underpinning their entertainment value with considerable algorithmic complexity. At the heart of these games is the efficient management of a dictionary, the generation of feedback based on player guesses, and the strategic selection of guesses by the computer. This analysis aims to explain the data structures and algorithms that facilitate these core functionalities, emphasizing their role in ensuring game performance and player engagement.
In addition, the report presents a performance analysis of the two games, focusing on metrics such as the average number of guesses required in Wordle and the scalability of WordChallenge with respect to word length. By performing benchmarks, I aim to quantify the efficiency of my implemented solution and provide insights into the computational requirements and optimization strategies that characterize these games.

## Usage
### Repository Contents
- `trie.py`: Implementation of the Trie data structure
- `dictionary.txt`: List of English words with frequency counts
- `wordChallenge.py`: Script for the Word Challenge game logic
- `wordle.py`: Script for the Wordle game logic
- `requirements.txt`: List of Python package dependencies
- `README.md`: This file
- `Hoesch_Jannik-4-wordgames.pdf`: Project report

### How to Run
Ensure you have Python 3.7+ installed on your system.

- To start the game, run:
    ```sh
    python play.py

## Data Structures
The Trie, a fundamental data structure in computer science, is essential to a wide range of appli- cations, from autocomplete systems to spell checkers and beyond. At its core, a trie is a tree-like structure that efficiently stores a dynamic set of strings by using the common prefixes of the strings. This section explains the characteristics of the Trie data structure, highlighted by a discussion of my implementation of its key properties: nodes, insertion and search.

## Games
### Word Challenge
Word Challenge is a game that challenges players to generate all possible words from a given set of letters, while adhering to a dictionary of valid words.
In interactive mode the player chooses the set of letters manually, while in automatic mode, the program selects a random word from the dictionary of length l. First, the program selects a random word from the dictionary of length l. I use the words by length dictionary created when the initial dictionary was loaded into the Trie to efficiently select a random word of length l. This eliminates traversing the Trie to find all words of a certain length. Before using the selected word as input for the solver, the letters are randomly shuffled.
Both in interactive and automatic mode, the program then searches for all possible valid letter combinations in the dictionary. The generation of possible words from a given set of input letters in Word Challenge involves a process that combines algorithmics with the structural advantages of the Trie data structure. Using a backtracking algorithm, the program iteratively constructs candidate words by exploring every possible combination of the given letters. Each step in this recursive process extends a partial word by one letter, checking against the Trie to determine whether the current concatenation remains a prefix of a valid word. Paths that no longer correspond to any word prefix in the Trie are abandoned, significantly narrowing the search space. Upon reaching a node in the trie that marks the end of a valid word, the constructed word is saved as a successful match. The algorithm takes into account the number of letters, ensuring that each letter from the input set is used no more than its available number. This generation process not only guarantees the identification of all valid words within the constraints of the given set of letters, but does so with remarkable efficiency, taking advantage of the Trie’s ability to quickly navigate
through the set of possible words.

To assess the performance of my implementation of Word Challenge I measured the average number of words found and the average CPU time for each word length. The benchmark was run with 10000 iterations for each word length.

![word-challenge_avg-words](https://github.com/user-attachments/assets/c2c7a87f-6ba1-4e8b-b840-f3d827368ca1)

The average number of words found seems to increase exponentially with word lengths. This is an expected result, since longer words can often be broken down into a larger number of smaller words, and the number of possible word combinations grows exponentially as more letters are available.

![word-challenge_avg-time](https://github.com/user-attachments/assets/c248645f-c0d8-42fc-a690-abfd2b279b1b)

In addition, the computational complexity of finding all possible words also increases exponen- tially with word length, due to the larger number of letter combinations that the algorithm must process for longer words.
Overall, the results indicate that the computational load of the Word Challenges becomes sig- nificantly higher with longer words, suggesting the need for performance optimization for longer word lengths, which I have successfully implemented using a Trie structure.

### Wordle

