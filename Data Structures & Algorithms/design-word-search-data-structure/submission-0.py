class Node:
    def __init__(self,):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        def dfs(i, node):
            if i == len(word):
                return node.is_word
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if dfs(i+1, child):
                        return True
                return False

            if not c in node.children:
                return False
            
            return True

        return dfs(0, node)

