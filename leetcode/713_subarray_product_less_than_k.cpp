class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int n = nums.size();
        int j = 0;
        int prod = 1;
        int count = 0;
        for (int i=0;i<n;i++){
            if (j<i){
                j=i;
                prod =1;
            }
            
            while(j<n && nums[j] * prod <k){
                prod *= nums[j];
                j++;
            }
            count += j-i;
            prod /= nums[i];
        }
        return count;
    }
};
