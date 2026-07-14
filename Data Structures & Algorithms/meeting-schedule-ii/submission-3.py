class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        def getRemovedIntervals(itls):
            removed = []
            itls = sorted(itls, key=lambda x: x.start)

            l, r = 0, 1

            while r < len(itls):
                if itls[l].end <= itls[r].start:
                    l = r
                else:
                    if itls[l].end <= itls[r].end:
                        removed.append(itls[r])
                    else:
                        removed.append(itls[l])
                        l = r

                r += 1

            return removed

        rooms = 0
        remaining = intervals

        while remaining:
            remaining = getRemovedIntervals(remaining)
            rooms += 1

        return rooms