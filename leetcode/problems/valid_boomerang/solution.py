class Solution(object):
    def isBoomerang(self, points):
        temp1 = points[0][0]*(points[1][1] - points[2][1])  
        temp2 = points[1][0]*(points[2][1] - points[0][1])
        temp3 = points[2][0]*(points[0][1] - points[1][1])
        if (temp1 + temp2 + temp3) != 0:
            return True
        else :
            return False