#include <iostream>
using namespace std;

int find(int arr[], int n)
{
    int maxPro = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = i; j < n; j++)
        {
            if (arr[j] > arr[i])
            {
                maxPro = max(arr[j] - arr[i], maxPro);
            }
        }
    }
    return maxPro;
}

int optimal(int arr[], int n)
{
    int maxPro = 0;
    int minPro = INT_MAX;
    for (int i = 0; i < n; i++)
    {
        minPro = min(minPro, arr[i]);
        maxPro = max(maxPro, arr[i] - minPro);
    }
    return maxPro;
}

void optimalDay(int arr[], int n)
{
    int maxPro = 0;
    int minPro = INT_MAX;
    int start = 0;
    int end = 0;
    for (int i = 0; i < n; i++)
    {
        if (minPro > arr[i])
        {
            minPro = arr[i];
            start = i;
        }
        if (maxPro < arr[i] - minPro)
        {
            maxPro = arr[i] - minPro;
            end = i;
        }
    }
    cout << "Buy Day: " << start << "\n"
         << "Sell Day: " << end << "\n"
         << "Max Profit: " << maxPro << endl;
}

int main()
{
    int arr[] = {7, 1, 5, 3, 6, 4};
    int n = sizeof(arr) / sizeof(arr[0]);
    int result = find(arr, n);
    cout << "Max Profit: " << result << endl;

    result = optimal(arr, n);
    cout << "Max Profit: " << result << endl;

    optimalDay(arr, n);
}