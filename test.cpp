#include<bits/stdc++.h>
using namespace std;

int main(){
    int a;
    int b[a];
    cin>>a;
    
    for(int i=0;i<a;i++){
        cin>>b[i];
    }
  int low=b[0];
  for(int i=1;i<a;i++){
      if(b[i]<low){
          low=b[i];
      }
  }
      cout<<low;
      
  }

