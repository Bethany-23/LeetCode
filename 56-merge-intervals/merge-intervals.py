class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # sort by start
        
        merged = []
        
        for interval in intervals:
            # if no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # overlap → merge
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged