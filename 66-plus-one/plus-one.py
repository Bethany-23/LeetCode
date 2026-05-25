class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # start from the last digit
        for i in range(len(digits) - 1, -1, -1):
            
            # if digit is less than 9
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            # if digit is 9
            digits[i] = 0
        
        # if all digits were 9
        return [1] + digits