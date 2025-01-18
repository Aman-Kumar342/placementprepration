#include<bits/stdc++.h>
using namespace std;
vector<int>merge(vector<int>a, vector<int >b){
    vector<int>temp;
    for(int i=0;i<a.size();i++){
        temp.push_back(a[i]);
    }
    for(int i=0;i<b.size();i++){
        temp.push_back(b[i]);
    }
    return temp;
}
vector<int>unionof(vector<int>a, vector<int>b){
    vector<int>temp=merge(a,b);
    set<int>st;
    for(int i=0;i<temp.size();i++){
        st.insert(temp[i]);
    }
    int k=st.size();
    vector<int>result(st.begin(),st.end());
    for(int x:result){
        cout<<x<<" ";
    }
    cout<<endl;
    return result;
}
int main(){
    int n;
    cin>>n;
    int m;
    cin>>m;
    vector<int>a(n);
    vector<int>b(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    for(int i=0;i<m;i++){
        cin>>b[i];
    }
    vector<int> union_result = unionof(a, b);
    return 0;

}