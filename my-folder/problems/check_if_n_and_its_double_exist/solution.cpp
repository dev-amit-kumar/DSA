class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        int n = arr.size();
        for(int i = 0; i < n; i++){
            int target = arr[i] * 2;
            int low = 0;
            int high = n - 1;
            while(low <= high){
                int mid = (low + high) / 2;
                if(arr[mid] == target && i != mid) return true;
                else if(arr[mid] < target) low = mid + 1;
                else high = mid - 1;
            }
        }
        return false;
    }
};