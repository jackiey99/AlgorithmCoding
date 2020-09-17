class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        int M=1e9+7;
        int n = nums.size();
        vector<long> power(n+1, 1);
        for(int i=1;i<=n;i++){
            power[i] = power[i-1] * 2 % M;
        }
        sort(nums.begin(), nums.end());
        
        int i=0, j=n-1;
        long res = 0;
        while(i<=j){
            while(i<=j && nums[i]+nums[j]>target){
                j--;
            }
            if(i>j) break;
            res = (res + power[j-i])%M;
            i += 1;
        }
        return res;
    }
};
