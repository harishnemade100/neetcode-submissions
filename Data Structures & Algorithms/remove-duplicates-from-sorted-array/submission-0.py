class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        seen = set()
        idx = 0

        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[idx] = num
                idx+=1
            
        return idx
        