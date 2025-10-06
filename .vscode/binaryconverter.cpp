#include <iostream>
#include <cmath>
using namespace std;
int main(){
   cout<<"enter any number";
   int n;
   cin>>n;
   int bit;
   int value=0;
   int i=1;
   while(n>0){
       bit =n&1;
       value = (bit*(pow(10,i)) + value);
       n=n>>1;
       i++;
   }
   cout<<value;
   return 0;
