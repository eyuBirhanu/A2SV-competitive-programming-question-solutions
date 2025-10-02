# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.isEnd
            if word[i] == '.':
                for ch in node.children.values():
                    if dfs(i+1, ch):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                return dfs(i+1, node.children[word[i]])
        
        return dfs(0, self.root)
                

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)