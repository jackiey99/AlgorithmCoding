class Solution {
public:
    int maxSumRangeQuery(vector<int>& nums, vector<vector<int>>& requests) {
        int n = nums.size();
        vector<int> diff(n+1, 0);
        for(auto request: requests){
            diff[request[0]] += 1;
            diff[request[1]+1] -= 1;
        }
        vector<int> freq(n, 0);
        int prev = 0;
        for(int i=0;i<n;i++){
            prev += diff[i];
            freq[i] = prev;
        }
        sort(freq.begin(), freq.end());
        sort(nums.begin(), nums.end());
        long res = 0;
        long M = 1e9 + 7;
        for(int i=0;i<n;i++){
            res = (res + (long)freq[i] * (long)nums[i]) % M;
        }
        return res;
    }
};
