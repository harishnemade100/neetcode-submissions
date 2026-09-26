class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq ={}

        for num in nums:
            if num not in freq:
                freq[num]=0
            freq[num]+=1
        
        result = []

        for _ in range(k):

            max_freq =0 
            max_num = None

            for num in freq:
                if freq[num] > max_freq:
                    max_freq= freq[num]
                    max_num = num
                
            result.append(max_num)
            del freq[max_num]
        
        return result
