class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # Bit shifting method
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Try to shift left (double) until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract and add to result
            dividend -= temp
            quotient += multiple
        
        return -quotient if negative else quotient
