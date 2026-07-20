class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return []

        # Step 1: Pair values with indices
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        # Step 2: Sort by values
        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(nums_with_index) - 1

        while left < right:
            total = nums_with_index[left][0] + nums_with_index[right][0]

            if total == target:
                # FIX: sort indices before returning
                return sorted([nums_with_index[left][1], nums_with_index[right][1]])
            elif total < target:
                left += 1
            else:
                right -= 1

        return []