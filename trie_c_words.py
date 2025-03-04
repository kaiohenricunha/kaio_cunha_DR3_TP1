class TrieNode:
    def __init__(self):
        self.children = {}  # Mapeia caracteres para seus nós filhos.
        self.end_of_word = False  # Indica o fim de uma palavra.

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

    def _print_trie(self, node, prefix):
        # Lista os filhos do nó atual
        children = list(node.children.items())
        count = len(children)
        for i, (char, child) in enumerate(children):
            # Define o conector: "└── " para o último ou "├── " para os demais.
            is_last = (i == count - 1)
            branch = "└── " if is_last else "├── "
            # Marca o fim da palavra se for o caso.
            marker = " (fim)" if child.end_of_word else ""
            print(prefix + branch + char + marker)
            # Atualiza o prefixo para os próximos níveis.
            new_prefix = prefix + ("    " if is_last else "│   ")
            self._print_trie(child, new_prefix)

    def print_trie(self):
        print("(root)")
        self._print_trie(self.root, "")

# Testando a Trie com as palavras fornecidas
trie = Trie()
palavras = ["casa", "carro", "caminhão", "cachorro", "cadeira"]
for palavra in palavras:
    trie.insert(palavra)

# Exibe a estrutura hierárquica da Trie
trie.print_trie()
