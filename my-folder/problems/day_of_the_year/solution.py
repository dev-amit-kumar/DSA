class Solution:
    def dayOfYear(self, date: str) -> int:
        
        dod = list(map(int,date.split("-")))
        
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
        
        if (dod[0] % 400 == 0) or (dod[0]%4 == 0 and dod[0]%100!=0):
            month_days[1]+=1
           
        total_days = dod[2]
        for i in range(0,dod[1]-1):
            total_days = total_days + month_days[i]
        return total_days
        