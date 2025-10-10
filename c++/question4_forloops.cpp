#include <iostream>
using namespace std;
int main(){

 int result= 0;
for(int a= 1 ; a<=50 ; a+=1){
   
    result = result + a;
  } // we cannot use int result inside the block as outside it the result wont recognize it

  cout <<result<<endl ;
    return 0;
// if i save the file using question4(loops) then the platform will think of it as a function and will show error of this 





}