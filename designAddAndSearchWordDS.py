#Day 22

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        return self._search(self.root, word)
    
    def _search(self, node, word):
        if not word:
            return node.is_end_of_word
        
        char = word[0]
        if char == '.':
            for child in node.children.values():
                if self._search(child, word[1:]):
                    return True
            return False
        else:
            if char in node.children:
                return self._search(node.children[char], word[1:])
            return False

class WordDictionary:
    def __init__(self):
        self.trie = Trie()
    
    def addWord(self, word):
        self.trie.addWord(word)
    
    def search(self, word):
        return self.trie.search(word)
