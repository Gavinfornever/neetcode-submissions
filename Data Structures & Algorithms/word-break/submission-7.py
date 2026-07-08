class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False]*(length+1)
        dp[0]=True

        for i in range(1, length+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

            # if s[:i+1] not in wordDict and \
            #     dp[last] and \
            #     s[last+1:i+1] not in wordDict:
            #     dp[i] = False
            #     continue
            
            # dp[i] = True
            # last = i
        
        return dp[length]


