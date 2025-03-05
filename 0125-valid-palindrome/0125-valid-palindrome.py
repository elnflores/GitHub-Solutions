class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for char in s:
            if char not in string.punctuation and char != ' ':
                st += char.lower()
        
        if len(st) % 2 == 0:
            b = len(st) // 2
            a = b - 1 
        else:
            a = len(st) // 2 - 1
            b = len(st) // 2 + 1
        
        while (a >= 0 and b < len(st)):
            if st[a] != st[b]:
                return False
            a-=1
            b +=1
        return True


        