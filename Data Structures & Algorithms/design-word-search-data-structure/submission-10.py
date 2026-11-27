class WordDictionary:
    def __init__(self):
        self.d = {}

    def addWord(self, word: str) -> None:
        nd = self.d
        for w in word:
            if w not in nd:
                nd[w] = {}
            nd = nd[w]
        nd[1] = True

    def search(self, word: str) -> bool:
        def search1(nd, word: str) -> bool:
            i = 0
            for w in word:
                i += 1
                if w != "." and w not in nd:
                    return False

                if w == ".":
                    nw = word[i:]
                    for nd1 in nd:
                        res = search1(nd[nd1], nw)
                        if res:
                            return True
                    return False

                nd = nd[w]
            print(nd)
            return isinstance(nd, dict) and 1 in nd

        return search1(self.d, word)
