class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == 0:
            return []
        
        char_freq = {}

        for num in nums:
            if num in char_freq:
                char_freq[num]+=1
            else:
                char_freq[num]=1
        
        values = list(char_freq.items())

        values.sort(key=lambda x:x[1], reverse=True)

        ordered_dict = dict(values)
        keys_list = list(ordered_dict.keys())

        return keys_list[:k]


        