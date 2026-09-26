from collections  import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups= defaultdict(list)

        for word in strs:
            sorted_words = "".join(sorted(word))

            key = tuple(sorted_words)
            
            groups[key].append(word)

        return list(groups.values())




        