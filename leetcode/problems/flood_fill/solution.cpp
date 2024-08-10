class Solution {
public:
    void dfs(vector<vector<int>> &image, int newColor, int floodColor, int row, int col)
    {
        if (row < 0 || col < 0 || row >= image.size() || col >= image[0].size() || image[row][col] != floodColor)
            return;
        if (image[row][col] == floodColor)
            image[row][col] = newColor;
        dfs(image, newColor, floodColor, row + 1, col);
        dfs(image, newColor, floodColor, row - 1, col);
        dfs(image, newColor, floodColor, row, col + 1);
        dfs(image, newColor, floodColor, row, col - 1);
    }

    vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int newColor)
    {
        int floodColor = image[sr][sc];
        if (floodColor != newColor)
            dfs(image, newColor, floodColor, sr, sc);
        return image;
    }
};