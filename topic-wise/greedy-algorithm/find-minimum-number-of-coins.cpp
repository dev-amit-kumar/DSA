// Link: https://practice.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> coins = {1, 2, 5, 10, 20, 50, 100, 500, 1000};
    int n = coins.size();
    int V = 99;
    vector<int> ans;
    int i = n - 1;

    // sol 1
    // for (int i = n - 1; i >= 0; i--)
    // {
    //     while (V > coins[i])
    //     {
    //         V = V - coins[i];
    //         ans.push_back(coins[i]);
    //     }
    // }

    // sol 2
    while (i >= 0 && V != 0)
    {
        if (V >= coins[i])
        {
            V = V - coins[i];
            ans.push_back(coins[i]);
        }
        else
            i--;
    }
    cout << "The minimum number of coins is " << ans.size() << endl;
    cout << "The coins are ";
    for (i = 0; i < ans.size(); i++)
        cout << ans[i] << " ";
    cout << endl;
    return 0;
}