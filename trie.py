class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def find_words(self, letters):
        found_words = set()

        def backtrack(node, path, letter_counts):
            if node.is_end_of_word:
                found_words.add(''.join(path))
            for char, child_node in node.children.items():
                if letter_counts.get(char, 0) > 0:
                    letter_counts[char] -= 1
                    path.append(char)
                    backtrack(child_node, path, letter_counts)
                    path.pop()
                    letter_counts[char] += 1

        letter_counts = {char: letters.count(char) for char in set(letters)}
        backtrack(self.root, [], letter_counts)
        return sorted(found_words, key=len)

    def load_dictionary(self, file_path):
        words_by_length = {}
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip().split(":")[0]
                self.insert(word)
                words_by_length.setdefault(len(word), []).append(word)
        return self, words_by_length
