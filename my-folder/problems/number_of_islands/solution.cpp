class Solution {
public:
    void dfs(vector<vector<char>>& grid, int i, int j, int rows, int cols){
        if( i < 0 || i == rows || j < 0 || j == cols || grid[i][j] != '1') return;
        grid[i][j] = '2';
        dfs(grid, i+1, j, rows, cols);
        dfs(grid, i-1, j, rows, cols);
        dfs(grid, i, j+1, rows, cols);
        dfs(grid, i, j-1, rows, cols);
    }

    int numIslands(vector<vector<char>>& grid) {
        int nums = 0;
        int rows = grid.size();
        if(rows == 0) return 0;
        int cols = grid[0].size();
        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                if(grid[i][j] == '1'){
                    nums++;
                    dfs(grid, i, j, rows, cols);
                }
            }
        }
        return nums;
    }
};