// Link: https://practice.geeksforgeeks.org/problems/lemonade-change/1

#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

bool sol(vector<int> bills, int N)
{
    unordered_map<int, int> coins;
    coins[5] = 0;
    coins[10] = 0;
    coins[20] = 0;

    for (int i = 0; i < N; i++)
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
int main()
{
    vector<int> bills = {5, 5, 10, 10, 20};
    int n = bills.size();
    int result = sol(bills, n);
    cout << (result == 0 ? "false" : "true") << endl;
    return 0;
}