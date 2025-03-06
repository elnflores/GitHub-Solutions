class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char.lower()

        beg = 0
        end = len(cleaned_string) - 1

        while (beg != end and beg < end):
            if cleaned_string[beg] != cleaned_string[end]:
                return False
            beg += 1
            end -= 1
        return True


        