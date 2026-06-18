class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+=str(len(s))
            res+="#"
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i=0
        tmp=""
        while i<len(s):
            c=s[i]
            if '0'<=c and c<='9':
                tmp+=c
                i+=1
                continue
            elif c=='#':
                length = 0
                for j, x in enumerate(reversed(tmp)):
                    length += 10**j * (ord(x)-ord('0'))
                m = ""
                m+= s[i+1:i+1+length]
                res.append(m)
                i+=length+1
                continue
        return res



                