// https://leetcode.com/problems/number-of-islands/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution
{
private:
    void dfs(vector<vector<string>> &grid, int i, int j, int m, int n)
    {
        if (i < 0 || i == m || j < 0 || j == n || grid[i][j] != "1")
            return;
        grid[i][j] = "2";
        dfs(grid, i++, j, m, n);
        dfs(grid, i--, j, m, n);
        dfs(grid, i, j++, m, n);
        dfs(grid, i, j--, m, n);
    }

public:
    int numIslands(vector<vector<string>> &grid)
    {
        int islands = 0;
        int m = grid.size();
        if (rows == 0)
            return 0;
        int n = grid[0].size();
        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (grid[i][j] == "1")
                {
                    islands++;
                    dfs(grid, i, j, m, n);
                }
            }
        }
        return islands;
    }
};

int main()
{
    vector<vector<string>> grid = {};
    cout << numIslands(grid)
         << endl;
}