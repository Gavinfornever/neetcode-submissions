"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        def getRemovedIntervals(itls):
            removedIntervals = []
            itls = sorted(itls, key=lambda x:x.start)
            l, r = 0, 1
            while r<len(itls):
                if itls[l].end<=itls[r].start:
                    l=r
                    r+=1
                else:
                    if itls[l].end<=itls[r].end:
                        # remove r
                        removedIntervals.append(itls[r])
                        # tmp = itls[r]
                        # itls[r] = itls[l]
                        # itls[l] = tmp
                        # l=r
                        r+=1
                    else:
                        #remove l
                        removedIntervals.append(itls[l])
                        l=r
                        r+=1
            return removedIntervals
        res = 0
        # removedIntervals = getRemovedIntervals(intervals)
        removedIntervals = intervals
        # res = 1
        while removedIntervals:
            removedIntervals = getRemovedIntervals(removedIntervals)
            res+=1
        return res


