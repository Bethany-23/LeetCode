class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                # Skip duplicates
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                # Choose
                used[i] = True
                path.append(nums[i])
                
                # Explore
                backtrack(path)
                
                # Undo
                path.pop()
                used[i] = False
        
        backtrack([])
        return result