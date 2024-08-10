// https://leetcode.com/problems/01-matrix/

#include <iostream>
#include <vector>
using namespace std;

vector<vector<int>> updateMatrix(vector<vector<int>> &mat)
{
}

int main()
{
    vector<vector<int>> mat = {{0, 0, 0}, {0, 1, 0}, {0, 0, 0}};
    vector<vector<int>> result = updateMatrix(mat);
    for (auto i : result)
    {
        for (auto j : i)
            cout << j << " ";
        cout << end l;
    }
}