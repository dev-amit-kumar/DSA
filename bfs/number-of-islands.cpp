// https://leetcode.com/problems/number-of-islands/

class Solution
{
private:
    void dfs(vector<vector<char>> &grid, int rows, int cols, int i, int j)
    {
        if (i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != '1')
            return;
        grid[i][j] = 2;
        dfs(grid, rows, cols, i, j + 1);
        dfs(grid, rows, cols, i, j - 1);
        dfs(grid, rows, cols, i + 1, j);
        dfs(grid, rows, cols, i - 1, j);
    }

public:
    int numIslands(vector<vector<char>> &grid)
    {
        int num = 0;
        int rows = grid.size();
        if (rows == 0)
            return 0;
        int cols = grid[0].size();
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                if (grid[i][j] == '1')
                {
                    num++;
                    dfs(grid, rows, cols, i, j);
                }
            }
        }
        return num;
    }
};