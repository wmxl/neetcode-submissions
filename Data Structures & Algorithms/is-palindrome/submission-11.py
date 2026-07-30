class Solution:
    def isPalindrome(self, s: str) -> bool:
        parts =[]
        for i in s:
            if i >= 'A' and i <= 'Z':
                i = i.lower()
            if i >= 'a' and i <= 'z':
                parts.append(i)
            if i >= '0' and i <= '9':
                parts.append(i)
                
        ss = "".join(parts)
        print(ss)
        s = ss
        length = len(s) // 2
        for i in range(len(s) // 2):
            left = s[i]
            right = s[len(s) - 1 - i]
            print(f"left:{left} right:{right}")
            if  left != right:
                return False
        
        return True