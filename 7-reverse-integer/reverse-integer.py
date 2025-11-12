class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit integer limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Get sign and work with positive value
        sign = -1 if x < 0 else 1
        x_abs = abs(x)

        # Reverse the digits
        reversed_x = int(str(x_abs)[::-1])

    
        reversed_x *= sign

        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0

        return reversed_x
