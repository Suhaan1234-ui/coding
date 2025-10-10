#include <iostream>
#include <cstring>
using namespace std;
bool iseven(int a){
    bool ifeven= (a%2==0);
     if (ifeven){
     cout<<"even";
      return 0;
     }
     else{
     cout<<"odd";
     return 1;
     }
}
int main() {
    cout<<"enter any number to find its parity";
    int n;
    cin>>n;
    cout<<iseven(n);
    
}