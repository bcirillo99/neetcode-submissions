class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            for i in range(len(s)):
              res += chr(ord(s[i])*(i+2))
              res+=","
            res+="#"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        for string in s.split("#")[:-1]:
            tmp = ""
            for i, c in enumerate(string.split(",")):
                if c:
                    tmp += chr(round(ord(c) / (i + 2)))
            res.append(tmp)
        return res
