class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int n = A.size();
        int j=0, count=0;
        int res = 0;
        for(int i=0; i<n; i++){
            while( j<n && (count < K || A[j]==1)){
                if(A[j]==0)
                    count++;
                j++;
            }
            res = max(res, j-i);
            if(A[i]==0)
                count--;
        }
        return res;
    }
};
