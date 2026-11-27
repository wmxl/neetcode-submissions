class PrefixTree:

    def __init__(self):
        self.d = {"":{}}
        self.exist = set()

    def insert(self, word: str) -> None:
        exist = self.exist
        exist.add(word)

        d = self.d
        prefix = ""
        for w in word:
            last = prefix
            prefix += w
            if prefix in d:
                continue
            d[prefix] = {} 
            d[last][prefix] = d[prefix]


    def search(self, word: str) -> bool:
        exist = self.exist
        return word in exist
        

    def startsWith(self, prefix: str) -> bool:
        d = self.d
        return prefix in d
            
        return prefix in d
            
            

        
        