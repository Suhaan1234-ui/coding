#include <iostream>
using namespace std;
int main (){

cout<<"enter the number: "<<endl;
int number;
cin>>number;
long long factorial;
factorial= 1;
for(int i=1 ; i<=number; i++)
  factorial=factorial*i;
  

cout<<"factorial of "<<number<<"is :"<< factorial;
return 0;











}