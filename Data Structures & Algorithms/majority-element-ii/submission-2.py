class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        m = defaultdict(int)

        for num in nums:
            m[num]+=1
        
        n = n//3
        res = []
        for key, value in m.items():
            if value > n:
                res.append(key)
        
        return res
        