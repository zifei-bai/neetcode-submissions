"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        booked = []
        left, right = None, None
        for inter in intervals:
            # print(inter.start, inter.end)
            s, e = inter.start, inter.end
            if len(booked) == 0:
                booked.append((s, e))
                left = s
                right = e
            else:
                if e <= left or s >= right:
                    booked.append((s, e))
                    left = min(left, s)
                    right = max(right, e)
                else:
                    for a, b in booked:
                
                        if a <= s < b or a < e <= b or s <= a < b <= e:
                            return False
        return True