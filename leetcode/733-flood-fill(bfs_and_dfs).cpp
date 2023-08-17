// https://leetcode.com/problems/flood-fill/

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

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

int main()
{
    vector<vector<int>> image = {{1, 1, 1}, {1, 1, 0}, {1, 0, 1}};
    int sr = 1;
    int sc = 1;
    int color = 2;
    floodFill(image, sr, sc, color);
    for (auto subset : image)
    {
        for (auto i : subset)
            cout << i << ' ';
        cout << endl;
    }
}