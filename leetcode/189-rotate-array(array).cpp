// https://leetcode.com/problems/rotate-array/

#include <iostream>
using namespace std;

void rotation(int arr[], int d, int n)
{
    int temp_arr[d];
    int k = 0;
    for (int i = d; i < n; i++)
    {
        temp_arr[k] = arr[i];
        k += 1;
    }
    for (int i = 0; i < d; i++)
    {
        temp_arr[k] = arr[i];
        k += 1;
    }
    for (int i = 0; i < n; i++)
    {
        cout << temp_arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int d = 2;
    rotation(arr, d % n, n);
}