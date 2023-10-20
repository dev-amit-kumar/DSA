// https://takeuforward.org/data-structure/minimum-number-of-platforms-required-for-a-railway/

#include <iostream>
using namespace std;

int countPlatformsBrute(int n, int arr[], int dep[]){
    int ans = 1;
    for(int i = 0; i <= n-1; i++){
        int count = 1;
        for(int j = i+1; j <= n-1; j++){
            if((arr[i] >= arr[j] && arr[i] <= dep[j]) || (arr[j] >= arr[i] && arr[j] <= dep[i]))
                count++;
        }
        ans = max(ans, count);
    }
    return ans;
}

int countPlatformsOptimal(int n, int arr[], int dep[]){
    sort(arr, arr + n);
    sort(dep, dep + n);

    int ans = 1;
    int count = 1;
    int i = 1, j = 0;
    while(i < n && j < n){
        if(arr[i] <= dep[j]){
            count++;
            i++;
        }
        else{
            count--;
            j--;
        }
        ans = max(count, ans);
    }
    return ans;
}

int main()
{
    int arr[] = {900, 945, 955, 1100, 1500, 1800};
    int dep[] = {920, 1200, 1130, 1150, 1900, 2000};
    int n = sizeof(dep) / sizeof(dep[0]);
    cout << "countPlatformsBrute : " << countPlatformsBrute(n, arr, dep) << endl;
    cout << "countPlatformsOptimal : " << countPlatformsBrute(n, arr, dep) << endl;
}