#include<bits/stdc++.h>
using namespace std;
int removee(int arr[],int n){
    set<int>st;
    for(int i=0;i<n;i++){
        st.insert(arr[i]);
    }
    int k=st.size();
    return k;
}
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    int res=removee(arr,n);
    cout<<res;
    return 0;
}
