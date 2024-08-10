class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        unordered_map<int, int> coins;
        coins[5] = 0;
        coins[10] = 0;
        coins[20] = 0;
        int n = bills.size();
        for (int i = 0; i < n; i++)
        {
            int left = bills[i] - 5;
            coins[bills[i]] += 1;
            if (left == 0)
                continue;
            else if (left == 5 && coins[5] >= 1)
                coins[5] -= 1;
            else if (left == 10 && coins[10] >= 1)
                coins[10] -= 1;
            else if (left == 10 && coins[5] >= 2)
                coins[5] -= 2;
            else if (left == 15 && coins[10] >= 1 && coins[5] >= 1)
            {
                coins[10] -= 1;
                coins[5] -= 1;
            }
            else if (left == 15 && coins[5] >= 3)
                coins[5] -= 3;
            else
                return false;
        }
        return true;
    }
};