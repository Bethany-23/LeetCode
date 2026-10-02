class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for _ in range(n):
            one, two = two, one + two

        return one