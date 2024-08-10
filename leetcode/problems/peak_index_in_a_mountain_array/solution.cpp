class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int n = arr.size();
        int start = 0;
        int end = n - 1;
        int mid = (start + end) / 2;
        while (start < end)
        {
            mid = (start + end) / 2;
            if (arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1])
                return mid;
            if (arr[mid - 1] < arr[mid])
                start = mid;
            else if (arr[mid] > arr[mid + 1])
                end = mid;
        }
        return mid;
    }
};