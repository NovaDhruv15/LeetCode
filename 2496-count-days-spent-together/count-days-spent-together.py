from datetime import datetime

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        
        if start > end:
            return 0
            
        d1 = datetime.strptime(start, "%m-%d")
        d2 = datetime.strptime(end, "%m-%d")
        
        return (d2 - d1).days + 1