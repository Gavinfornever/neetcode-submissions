class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = {}
        length = len(s)
        last = 0
        for i in range(length):
            if s[:i+1] not in wordDict and \
                s[:last+1] in wordDict and \
                s[last+1:i+1] not in wordDict:
                dp[i] = False
                continue
            
            dp[i] = True
            last = i
        
        return dp[length-1]


