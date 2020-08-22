class Solution(object):
    def coinChange(self, coins, amount):
        temp_arr = [amount+1] *(amount+1)
        temp_arr[0]=0
        for i in range(1, amount+1):
            for value in coins:
                if i >=value:
                    temp_arr[i] = min(temp_arr[i], temp_arr[i-value]+1)
        if temp_arr[amount] == amount+1:
            return -1
        return temp_arr[amount]