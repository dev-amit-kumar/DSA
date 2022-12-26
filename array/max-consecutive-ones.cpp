// Link: https://leetcode.com/problems/max-consecutive-ones/

#include <iostream>
using namespace std;

int find(int arr[], int n)
{
    int curr_max = 0;
    int total = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == 0)
        {
            total = max(total, curr_max);
            curr_max = 0;
        }
        else
        {
            curr_max++;
        }
    }
    return max(total, curr_max);
}

int main()
{
    int arr[] = {1, 1, 0, 1, 1, 1};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = find(arr, n);
    cout << result << endl;
}