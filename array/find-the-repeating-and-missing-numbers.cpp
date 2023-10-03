// https://takeuforward.org/data-structure/find-the-repeating-and-missing-numbers/

#include <iostream>
using namespace std;

vector<int> better_approach(vector<int> arr)
{
    int n = arr.size();
    vector<int> hash(n, 0);
    vector<int> result(2, 0);
    for(int i = 0; i < n; i++){
        int num = arr[i];
        hash[num] = hash[num] + 1;
    }
    for (int i = 1; i < n+1; i++)
    {
        if(hash[i] == 0){
            result[0] = i;
        }
        else if (hash[i] == 2)
        {
            result[1] = i;
        }
    }
    return result;
}

int main()
{
    vector<int> arr = {3, 1, 2, 5, 4, 6, 7, 5};
    vector<int> result = better_approach(arr);
    cout << "Missing: " << result[0] << endl;
    cout << "Duplicate: " << result[1] << endl;
}