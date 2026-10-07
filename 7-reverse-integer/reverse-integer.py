class Solution:
    def reverse(self, x: int) -> int:
        below_zero = x < 0
        positive_num = abs(x)
        
        num_as_text = str(positive_num)
        flipped_text = num_as_text[::-1]
        final_num = int(flipped_text)
        
        if below_zero:
            final_num = -final_num
            
        if final_num < -2**31 or final_num > 2**31 - 1:
            return 0
            
        return final_num