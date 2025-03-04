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

    def _dfs(self, node, prefix, words):
        # Se o nó marca o fim de uma palavra, adiciona o prefixo atual à lista.
        if node.is_end_of_word:
            words.append(prefix)
        # Explora recursivamente cada filho do nó atual.
        for char, child in node.children.items():
            self._dfs(child, prefix + char, words)
            
    def autocomplete(self, prefix):
        node = self.root
        # Navega até o nó que representa o último caractere do prefixo.
        for char in prefix:
            if char not in node.children:
                return []  # Se o prefixo não existir, retorna lista vazia.
            node = node.children[char]
        # A partir desse nó, realiza uma DFS para coletar todas as palavras que compartilham o prefixo.
        words = []
        self._dfs(node, prefix, words)
        return words

# Exemplo de uso:
trie = Trie()
palavras = ["casa", "carro", "caminhão", "cachorro", "cadeira", "calor", "camisa"]
for palavra in palavras:
    trie.insert(palavra)

# Testando o autocomplete com o prefixo "ca"
resultado = trie.autocomplete("ca")
print("Palavras com o prefixo 'ca':", resultado)
