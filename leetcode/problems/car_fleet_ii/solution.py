class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        answer = [-1.0] * n  # Initialize collision times with -1
        stack = []  # Stack to keep track of cars and their speeds
        
        for i in range(n - 1, -1, -1):
            position, speed = cars[i]
            
            # Remove cars that are faster and will never be collided by the CURRENT car, by the time it gets to that point - that stack[-1] is already gone (collided)
            while stack and (cars[stack[-1]][1] >= speed or (cars[stack[-1]][0] - position)/(speed - cars[stack[-1]][1]) >= answer[stack[-1]] >= 0):
                stack.pop()
            
            # Calculate collision time if there's a car in front
            if stack:
                answer[i] = (cars[stack[-1]][0] - position)/(speed - cars[stack[-1]][1])
            
            # Add current car to the stack
            stack.append(i)
        
        return answer