class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        while i<n and intervals[i][1]<newInterval[0]:
            res.append(intervals[i])
            i+=1
        # overlap
        while  i<n and intervals[i][0]<=newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        
        res.append(newInterval)
        
        # while i<n and intervals[i][0]>newInterval[1]:
        while i<n:
            res.append(intervals[i])
            i+=1

        # for i in range(len(intervals)):
        #     if inserted:
        #         if intervals[i][1]<newInterval[0]:
        #             res.append(intervals[i])
        #         elif intervals[i][0]>newInterval[1]:
        #             res.append(intervals[i])
        #     else:
        #         if intervals[i][1]<newInterval[0]:
        #             res.append(intervals[i])
        #         else:
        #             newInterval[0] = min(newInterval[0], intervals[i][0])
        #             newInterval[1] = max(newInterval[1], intervals[i][1])
        #             if i+1<len(intervals) and intervals[i+1][0]>newInterval[1]:
        #                 res.append(newInterval)
        #                 inserted = True
                
        return res

