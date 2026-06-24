class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        matchMap = {"{":"}","(":")","[":"]"}
        queue=[]
        for c in s:
            if c in matchMap.keys():
                queue.append(c)
            else:
                if queue:
                    if c!=matchMap[queue.pop()]:
                        return False
                else:
                    return False
        return len(queue)==0