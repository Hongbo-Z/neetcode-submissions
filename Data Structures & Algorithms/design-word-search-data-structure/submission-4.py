class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        
        def dfs(i, node): # check if word[i:] is matched in any path from node
            curr = node
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.isEnd
        return dfs(0, self.root)    



        
