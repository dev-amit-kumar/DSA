// https://leetcode.com/problems/combinations/

#include <iostream>
#include <vector>
using namespace std;

void backtrack(vector<vector<int>> &ans, vector<int> &curr, int n, int k, int pos)
{
    if (curr.size() == k)
    {
        ans.push_back(curr);
        return;
    }
    for (int i = pos; i <= n; i++)
    {
        curr.push_back(i);
        backtrack(ans, curr, n, k, i + 1);
        curr.pop_back();
    }
}

vector<vector<int>> combine(int n, int k)
{
    vector<vector<int>> ans;
    vector<int> curr;
    backtrack(ans, curr, n, k, 1);
    return ans;
}

int main()
{
    int n = 4, k = 2;
    vector<vector<int>> arr = combine(n, k);
    cout << "result" << endl;
    for (vector<int> arr1 : arr)
    {
        for (int i : arr1)
            cout << i << " ";
        cout << endl;
    }
}