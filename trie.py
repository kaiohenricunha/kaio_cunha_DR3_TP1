class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário que mapeia caracteres para seus nós filhos.
        self.end_of_word = False  # Indica se a palavra termina neste nó.

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word

# Exemplo de uso:
trie = Trie()
trie.insert("python")
trie.insert("programacao")
print(trie.search("python"))        # Saída: True
print(trie.search("programar"))       # Saída: False
