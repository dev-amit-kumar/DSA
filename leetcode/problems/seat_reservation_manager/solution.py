class SeatManager:

    def __init__(self, n: int):
        self.heapList = list(range(n+1))[1:]
        heapq.heapify(self.heapList)

    def reserve(self) -> int:
        return heapq.heappop(self.heapList)
        
    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.heapList, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)