#include<bits/stdc++.h>
using namespace std;
vector<int>longestsubarrayofsumk(vector<int>arr,int k){
    int sum=0;
    int i=0;
    int j=0;
    while(j<arr.size()){
        sum=sum+arr[j];
        if(sum<k){
            j++;
        }
        int max=0;
        if(sum==k){
            if((j-i+k)>max){
                max=j-i+1;
            }
            j++;
        }
        if(sum>k){
            while(sum>k){
                sum=sum-arr[i];
                i++;
            }
        }
        j++;
    }
}
using namespace std;
int main(){

}
