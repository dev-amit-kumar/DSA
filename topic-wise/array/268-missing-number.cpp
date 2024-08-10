// https://leetcode.com/problems/missing-number/
// Link: https://practice.geeksforgeeks.org/problems/missing-number4257/1

#include <iostream>
using namespace std;

int main()
{
    int arr[] = {2, 5, 3, 1};
    int n = sizeof(arr) / sizeof(arr[0]) + 1;
    int sum = (n * (n + 1)) / 2;

    for (int i = 0; i < n - 1; i++)
        sum -= arr[i];
    cout << sum << endl;
}