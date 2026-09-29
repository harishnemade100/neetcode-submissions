class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0 
        count = 0
        freq = {}

        for num in nums:
            prefix += num

            if prefix == k:
                count+=1

            required = prefix - k 

            if required in freq:
                count += freq[required]
            
            freq[prefix] = freq.get(prefix, 0) + 1
        
        return count
                    