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
                if len(prefix) == len(word):
                    d[prefix][1] = True
                continue

            d[prefix] = {} 
            d[last][prefix] = d[prefix]

            if len(prefix) == len(word):
                d[prefix][1] = True


    def search(self, word: str) -> bool:
        d = self.d
        return word in d and 1 in d[word]
        

    def startsWith(self, prefix: str) -> bool:
        d = self.d
        return prefix in d
            
            
            

        
        