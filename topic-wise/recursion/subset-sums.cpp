// https://practice.geeksforgeeks.org/problems/subset-sums2234/1

#include <iostream>
#include <vector>
using namespace std;

void recursion(vector<int> &arr, vector<int> &ans, int sum, int pos)
{
    ans.push_back(sum);
    for (int i = pos; i < arr.size(); i++)
        recursion(arr, ans, sum + arr[i], i + 1);
}

vector<int> subsetSums(vector<int> arr, int N)
{
    vector<int> ans;
    recursion(arr, ans, 0, 0);
    return ans;
}

int main()
{
    vector<int> arr = {2, 3};
    vector<int> ans = subsetSums(arr, arr.size());
    for (int i : ans)
        cout << i << " ";
    cout << endl;
}