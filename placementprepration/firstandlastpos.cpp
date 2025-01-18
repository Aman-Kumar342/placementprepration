#include<bits/stdc++.h>
using namespace std;
class solution{
    private:
    int findfirstpos(vector<int>&nums,int target){
        int s=0;
        int e=nums.size()-1;
        int pos=-1;
        while(s<=e){
            int mid=s+(e-s)/2;
            if(nums[mid]==target){
                pos=mid;
                e=mid-1;       }
            else if(nums[mid]<target){
                s=mid+1;

            }
            else{
                e=-1+mid;
            }
        }
        return pos;
    }
    int findlastpos(vector<int>&nums,int target){
        int s=0;
        int e=nums.size()-1;
        int pos=-1;
        while(s<=e){
            int mid=s+(e-s)/2;
            if(nums[mid]==target){
                pos=mid;
                s=mid+1;
            }
            else if(nums[mid]<target){
                s=mid+1;
            }
            else{
                e=mid-1;
            }
        }
        return pos;
    }
    public:
    vector<int>searchrange(vector<int>&nums,int target){
        vector<int>res(2,-1);
        if(nums.empty()){
            return res;
        }
        res[0]=findfirstpos(nums,target);
        res[1]=findlastpos(nums,target);
        return res;
    }

};
int main(){
    int n;
    cin>>n;
    int k;
    cin>>k;
    vector<int>arr(n);
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    searchrange(arr,k);

}