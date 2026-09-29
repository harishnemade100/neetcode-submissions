class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
                
        result = []
        for key, values in freq.items():
            if values > len(nums)//3:
                result.append(key)
        
        return result
        