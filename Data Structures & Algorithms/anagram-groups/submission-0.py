class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            groups = {}

            for word in strs:
                # Step 1: Build frequency count for each word (26 letters for a–z)
                count = [0] * 26
                for char in word:
                    count[ord(char) - ord('a')] += 1   # map 'a'->0, 'b'->1, ...

                # Step 2: Convert list to tuple (hashable, can be dictionary key)
                key = tuple(count)

                # Step 3: Group words by this key
                if key not in groups:
                    groups[key] = []
                groups[key].append(word)

            # Step 4: Return grouped lists
            return list(groups.values())     