#include<bits/stdc++.h>
using namespace std;
int occur(int arr[],int n){
    map<int,int>mp;
    for(int i=0;i<n;i++){
        mp[arr[i]]++;
    }
    for(auto it:mp){
        if(it.second==1){
            return it.first;
        }
    }
    return -1;
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int res=occur(arr,n);
    cout<<res;
    return 0;

}