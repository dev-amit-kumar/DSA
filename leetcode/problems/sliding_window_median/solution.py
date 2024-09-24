class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        self.initialize(nums,k)

        for i in range(k,len(nums) + 2):
            # set Median
            self.storeMedian()

            if i == len(nums):
                break
            incomingElement = nums[i]
            outgoingElement = nums[i-k]

            # Remove outgoing element from heaps lazy
            balancePointer = self.removeOldElementFromHeapsLazy(outgoingElement)
            
            # add incoming number to heaps
            balancePointer = self.addNewElementToHeaps(incomingElement,balancePointer)
            
            # now balance the heap
            self.balanceHeaps(balancePointer)

            # cleanup the elements which are discarded but present on top of heaps
            # as we only care about top of heaps for our output

            self.cleanTrashCan()

        return self.medians
            


    def initialize(self,nums,k):
        self.medians = []
        self.left = [] # max heap
        self.right = [] # min heap
        self.nums = nums
        self.k = k
        self.trashCan = defaultdict(int)
        # push first k elements in both the heaps
        for i in range(k):
            heapq.heappush(self.left,-nums[i])

        for j in range(k//2):
            heapq.heappush(self.right,-heapq.heappop(self.left))

    def storeMedian(self):
        if self.k % 2 == 1:
            self.medians.append(float(-self.left[0]))
        else:
            self.medians.append( (-self.left[0] + self.right[0]) / 2.0 )
        
    def removeOldElementFromHeapsLazy(self,outgoingElement):
        balancePointer = 0
        self.trashCan[outgoingElement] += 1

        if outgoingElement <= -self.left[0]:
            balancePointer -= 1
        else:
            balancePointer += 1

        return balancePointer

    def addNewElementToHeaps(self,incomingElement,balancePointer):
        if not self.left or incomingElement <= -self.left[0]:
            heapq.heappush(self.left,-incomingElement)
            balancePointer += 1
        else:
            heapq.heappush(self.right,incomingElement)
            balancePointer -= 1
        return balancePointer

    def balanceHeaps(self,balancePointer):
        if balancePointer < 0:
            heapq.heappush(self.left,-heapq.heappop(self.right))
        elif balancePointer > 0:
            heapq.heappush(self.right,-heapq.heappop(self.left))

    def cleanTrashCan(self):
        while self.left and self.trashCan[-self.left[0]]:
            self.trashCan[-self.left[0]] -= 1
            heapq.heappop(self.left)

        while self.right and self.trashCan[self.right[0]]:
            self.trashCan[self.right[0]] -= 1
            heapq.heappop(self.right)

    