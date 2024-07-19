# Word Games

This repository contains a university project that I created for the course Advanced Data Structures at the Universitat Politècnica de Catalunya. The goal is to implement an application capable of playing two word-based games: Word Challenge and Wordle. 

Both games, while different in their gameplay mechanics, challenge players to deduce or construct words from a given set of letters, underpinning their entertainment value with considerable algorithmic complexity. At the heart of these games is the efficient management of a dictionary, the generation of feedback based on player guesses, and the strategic selection of guesses by the computer. This analysis aims to explain the data structures and algorithms that facilitate these core functionalities, emphasizing their role in ensuring game performance and player engagement.

In addition, the report presents a performance analysis of the two games, focusing on metrics such as the average number of guesses required in Wordle and the scalability of WordChallenge with respect to word length. By performing benchmarks, I aim to quantify the efficiency of my implemented solution and provide insights into the computational requirements and optimization strategies that characterize these games.

## Usage
### Repository Contents
- `trie.py`: Implementation of the Trie data structure
- `dictionary.txt`: List of English words with frequency counts
- `wordChallenge.py`: Script for the Word Challenge game logic
- `wordle.py`: Script for the Wordle game logic
- `requirements.txt`: List of Python package dependencies
- `README.md`: This file

### How to Run
Ensure you have Python 3.7+ installed on your system.

- To start the game, run:
    ```sh
    python play.py

## Trie
The Trie, a fundamental data structure in computer science, is essential to a wide range of applications, from autocomplete systems to spell checkers and beyond. At its core, a trie is a tree-like structure that efficiently stores a dynamic set of strings by using the common prefixes of the strings. This section explains the characteristics of the Trie data structure, highlighted by a discussion of my implementation of its key properties: nodes, insertion and search.

![image](https://github.com/user-attachments/assets/1c6d4a29-b1b9-4f63-8e4c-38b478a6dff7)

### TrieNode
The TrieNode class serves as the foundational element of the Trie. Each node contains 'children' (A dictionary that maps characters to their subsequent TrieNodes) and 'is_end_of_word' (A boolean flag that marks the completion of a valid word). This structure enables the Trie to represent each letter of a string with a node in the tree, where paths from the root to a marked end node spell out the strings stored in the Trie.

### Insert Function
The insert method integrates a new word into the Trie with the following steps: Initialization (Begin at the root node), Traversal and Expansion (If no child node exists for the character, a new TrieNode is created) and Mark Completion (Upon reaching the end of the word, set the is end of word flag of the final node to True, signifying the presence of a complete word within the Trie). By inserting each word from the dictionary file into the Trie, we can build a comprehensive Trie representing all possible words with very efficient access for the word games. Additionally, I create the dictionary words by length, that maps the length of words to lists containing all words of that specific length. This improves the selection process for game mechanisms that require a word of a certain length.

### Search Function
The search method locates a word in the Trie with the following steps: Initialization (Begin at the root node), Traversal (For each character in the target word, the search moves to the corresponding child node), Check Existence (If at any point the required child node does not exist, the word is not in the Trie, and the search returns False) and Word Completion (Successfully reaching the end of the word with is end of word flagged as True confirms the word’s presence in the Trie)



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
Wordle challenges players to guess a secret word through iterative guessing and strategic reasoning, guided by feedback provided for each guess. It can be interactively played in a guesser mode, where the player tries to find the secret word receiving feedback from the program and a keeper mode, where the player provides the feedback for the programs guesses. In automatic mode the program represents both the keeper and the guesser. This section outlines the strategies and data structures that support these core mechanics of the game.
The selection of a random word (e.g. the secret word or the guess) is again done using the previously created words by length dictionary.
After receiving the guesses from the guesser, the keeper generates a feed- back. The used function compares the guess with the secret word and generates a string of digits, where ’2’ indicates a correctly placed letter, ’1’ indicates a correct letter in the wrong position, and ’0’ indicates a wrong letter.
The guesser randomly selects the next guess from a list of valid words for each attempt, initially containing all words of the correct length. This list can then be refined based on the received feedback, excluding words that do not match the feedback pattern. This iterative filtering narrows down the possibilities, guiding the guesser toward the correct word efficiently.

![image](https://github.com/user-attachments/assets/29c96519-99ca-45f3-ab83-cd0852c827bf)

To assess the performance of my implementation of Wordle I measured the average guesses needed to guess the correct word and the average CPU time for each word length. The benchmark was run with 10000 iterations for each word length.

![wordle_avg-guesses](https://github.com/user-attachments/assets/15047106-95fd-4496-a107-003831595503)

The first graph suggests a linear relationship between average guesses and word length: as word length increases, the average number of guesses required to solve the problem decreases. Several factors could cause this decrease, such as the ease of eliminating incorrect letters in longer words, or the shortage of longer words in the dictionary.

![wordle_avg-times](https://github.com/user-attachments/assets/1fe6f6c5-bf77-42d9-8d8e-68f2aa14a6ac)

At the same time, we observe an interesting pattern where CPU time peaks at a certain word length of 6 before decreasing, which suggests a point of maximal computational complexity relative to the length of the words being processed. 

![n_words](https://github.com/user-attachments/assets/1b98b949-835f-4bfb-8a7a-738d8a5bbd07)

Considering the distribution of the number of words for each word length, we notice that the CPU time seems to strongly correlate to the number of words. Less possible words in the dictionary, simplify the search and decision-making process of the algorithm.

Overall, these trends in the Wordle game highlight a contrast to those observed in Word Chal- lenge, demonstrating how different algorithmic strategies can yield varied performance across word lengths. This analysis underscores the importance of tailored optimization strategies for each game to maintain consistant performance.

