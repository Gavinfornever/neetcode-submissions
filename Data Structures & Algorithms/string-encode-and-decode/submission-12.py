import ast
class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            res+="0"
        res = ""
        for s in strs:
            res += s
            res += str(len(s))
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        if s=="0":
            res.append("")
        print(res)
        tmp = ""
        for c in s:
            print(c)
            if '1'<=c and c<='9':
                #three scenarios:
                ## 1. is the length of former str
                if len(tmp)==int(c):
                    res.append(tmp)
                    tmp = ""
                    continue
                ## 2. forms the length of former str with former 1-2 letter(s)
                if ord(tmp[-1]) in (ord('1'), ord('9')+1):
                    num+=10*int(tmp[-1])
                    if len(tmp[:-1]) == num:
                        res.append(tmp[:-1])
                        tmp = ""
                        continue
                if ord(tmp[-2]) in (ord('1'), ord('9')+1):
                    num+=100*int(tmp[-2])
                    res.append(tmp[:-2])
                    tmp = ""
                    continue
                ## 3. not 1 and not 2, continue and no code
                tmp+=c
            else:
                tmp+=c
        return res
