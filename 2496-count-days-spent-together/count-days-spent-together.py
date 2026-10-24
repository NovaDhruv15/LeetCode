class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        
        sm, sd = map(int, start.split('-'))
        em, ed = map(int, end.split('-'))
        
        start_day = sum(days[:sm]) + sd
        end_day = sum(days[:em]) + ed
        
        return max(0, end_day - start_day + 1)