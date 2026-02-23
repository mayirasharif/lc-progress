class Solution:
    def reverseBits(self, n: int) -> int:

        current_bit = format(n, '032b')
        print(current_bit)
        new_bit = current_bit[::-1]
        output = int(new_bit, 2)
        
        return output
        