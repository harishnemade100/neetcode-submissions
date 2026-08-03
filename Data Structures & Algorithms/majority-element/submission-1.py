class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        max_items =0
        result = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            
            if freq[num] > max_items:
                max_items = freq[num]
                result = num

        return result


        