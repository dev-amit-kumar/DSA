class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        # The size of the sliding window
        max_size = sum(nums)
        
        # Create a window of max_size and count the number of ones and zeros
        i, j = max_size, 0
        current_ones = sum(nums[:max_size]) # Number of ones in the window.
        minimum_number_of_zeros = max_size - current_ones # Number of zeros in the window. WE WANT TO MINIMIZE THIS.
        
        # now we just need to add a new number from the right and remove one from the left
        while i < len(nums)*2: # * 2 because the array is circular
            # Add from the right
            current_ones += nums[i % len(nums)]
            # Remove from the left
            current_ones -= nums[j % len(nums)]
            
            # By writting the previous two lines we maintain the size of sliding window.
            # Minimize the number of zeros
            minimum_number_of_zeros = min(minimum_number_of_zeros, max_size - current_ones)
            
            i += 1
            j += 1
            

        return minimum_number_of_zeros 