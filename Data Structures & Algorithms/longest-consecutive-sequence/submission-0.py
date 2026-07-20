class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        unique_nums = set(nums)

        longest = 0

        for num in unique_nums:
            if num -1 not in unique_nums:
                current = num
                length = 1

                while current + 1 in unique_nums:
                    current+=1
                    length+=1

                longest = max(longest, length)

        return longest

        