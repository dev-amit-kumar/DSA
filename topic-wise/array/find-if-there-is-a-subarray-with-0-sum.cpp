// Link: https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

bool subArrayExists(int arr[], int n)
{
    int currTotal = 0;
    unordered_set<int> sumSet;
    for (int i = 0; i <= n; i++)
    {
        currTotal += arr[i];
        if (currTotal == 0 || sumSet.find(currTotal) != sumSet.end())
            return true;
        sumSet.insert(currTotal);
    }
    return false;
}

int main()
{
    int arr[] = {-3, 2, 3, 1, 6};
    int n = sizeof(arr) / sizeof(arr[0]);
}
