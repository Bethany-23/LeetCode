class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            # If it’s an opening bracket, push it
            if ch in pairs.values():
                stack.append(ch)
            else:
                # If stack is empty or mismatch → invalid
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()

        # Valid only if no leftovers
        return not stack
