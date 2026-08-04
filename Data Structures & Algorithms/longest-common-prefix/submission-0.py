class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        strs.sort()

        first = strs[0]
        last = strs[-1]
        minlength = min(len(first), len(last))

        i = 0

        while i < minlength and first[i] == last[i]:
            i+=1
        
        return first[:i]


        