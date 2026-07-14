class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        # [0,2] [1,]
        l, r=0,1
        removeCount = 0
        while r<len(intervals):
            # nonoverlap, then move on each one
            if intervals[l][1]<=intervals[r][0]:
                l+=1
                r+=1
                continue
            # overlap
            else:
                if intervals[l][1]<=intervals[r][1]:
                    tmp = intervals[r]
                    intervals[r] = intervals[l]
                    intervals[l] = tmp
                    l=r
                    r+=1
                    removeCount+=1
                    continue
                else:
                    l=r
                    r+=1
                    removeCount+=1
                    continue
        return removeCount


            





