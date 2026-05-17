class tree:
    def __init__(self):
        self.child={}
        self.res = False
class WordDictionary:

    def __init__(self):
        self.root=tree()

    def addWord(self, word: str) -> None:
        node =self.root
        for i in range(0,len(word)):
            if word[i] in node.child:
                node = node.child[word[i]]
            else:
                node.child[word[i]]=tree()
                node = node.child[word[i]]
            if len(word)-1 ==i:
                node.res=True


    def search(self, word: str) -> bool:
        def search(i,node):
            if len(word) ==i:
                return node.res
            if word[i] =='.':
                found = False
                for val in node.child.values():
                    found = found or search(i+1,val)
                return found
            if word[i] in node.child:
                node = node.child[word[i]]
                return search(i+1,node)
            else:
                return False

        return search(0,self.root)
