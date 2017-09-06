class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int>res;
        int sz = nums1.size();
        int sz1 = nums2.size();
        for(int i = 0; i < sz; i++) res.push_back(nums1[i]);
        for(int i = 0; i < sz1; i++) res.push_back(nums2[i]);
        sort(res.begin(),res.end());
        int midp = res.size();
        double rest = (double)(res[(midp/2)-1] + res[(midp/2)])/2;
        if (midp%2 != 0) return res[midp/2] ;
        else return rest;
    }   
};