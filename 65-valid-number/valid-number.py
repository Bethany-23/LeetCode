class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        if not s:
            return False
        
        digitSeen = False
        dotSeen = False
        eSeen = False
        digitAfterE = True
        
        for i in range(len(s)):
            c = s[i]
            
            if c.isdigit():
                digitSeen = True
                digitAfterE = True
            
            elif c in ['+', '-']:
                # sign only allowed at start or after e
                if i != 0 and s[i - 1] not in ['e', 'E']:
                    return False
            
            elif c == '.':
                if dotSeen or eSeen:
                    return False
                dotSeen = True
            
            elif c in ['e', 'E']:
                if eSeen or not digitSeen:
                    return False
                eSeen = True
                digitAfterE = False
            
            else:
                return False
        
        return digitSeen and digitAfterE