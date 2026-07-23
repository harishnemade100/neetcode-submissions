class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""

        for str_data in strs:
            encode += str(len(str_data))
            encode += '#'
            encode += str_data
        return encode

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0
        n = len(s)
        
        while i < n:

            length = 0 
            # Extract the length
            while s[i] != '#':
                length = length * 10 + (ord(s[i]) - ord('0'))
                i+=1
            
            i+=1 # skip '#'

            temp = s[i : i+length]
            result.append(temp)
            i+=length
        
        return result

            

