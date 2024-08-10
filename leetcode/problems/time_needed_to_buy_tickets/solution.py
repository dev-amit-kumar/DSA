class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        queue = deque()
        for i in range(len(tickets)):
            queue.append(i)
        while(queue):
            top = queue.popleft()
            tickets[top] -= 1
            count += 1
            if k == top and tickets[top] == 0:
                return count
            if tickets[top] > 0:
                queue.append(top)
        return count