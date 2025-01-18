#include<bits/stdc++.h>
using namespace std;
int max_count(int arr[], int n){
    int ct=0;
    int maxi=0;
    for(int i=0;i<n;i++){
        if(arr[i]==1){
            ct++;
            maxi=max(ct,maxi);
        }
        else{
            ct=0;
        }
    }
    return maxi;
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int res=max_count(arr,n);
    cout<<res;
    return 0;

}