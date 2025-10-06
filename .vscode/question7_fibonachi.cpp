//to print fibonacchi series up to n terms
#include <iostream>
using namespace std;
int main(){

cout<<"enter the number of terms for which the fibonacchi is needed";
int n;
cin>>n;
  int a=0 , b=1 , c;

for(int i=3; i<=n ; i++) {
     c=a+b;
     cout<<c<<endl;
     a=b;
     b=c;
     
}

return 0;




}
