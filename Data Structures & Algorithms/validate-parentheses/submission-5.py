class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
            
        matchMap = {"}": "{", ")": "(", "]": "["}
        stack = []
        
        for c in s:
            if c in matchMap:
                if not stack or stack.pop() != matchMap[c]:
                    return False
            else:
                stack.append(c)
                
        return not stack 