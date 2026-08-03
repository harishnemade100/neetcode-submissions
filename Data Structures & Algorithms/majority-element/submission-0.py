class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        max_items =0
        result = 0

        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
            
        for key, value in freq.items():
            if value >= max_items:
                max_items = value
                result = key
        
        return result


        