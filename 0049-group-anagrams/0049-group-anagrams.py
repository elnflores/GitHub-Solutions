class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort string
        anagrams = {}

        for string in strs:
            rep = "".join(sorted(string))
            if anagrams.get(rep) is None:
                anagrams[rep] = [string]
            else:
                anagrams[rep].append(string)
        
        result = []
        for rep in anagrams:
            result.append(anagrams[rep])
        return result
            


        