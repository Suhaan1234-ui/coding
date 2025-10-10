#include <iostream>
using namespace std;
int main (){
   
cout<<"enter the number of rows";
int row;
cin>>row;
 
cout<< "enter the number of columns";
int col;
cin>>col;
  int num=1;

for (int i= 0; i<row; i++){
  
    for( int j=0 ; j<col; j++){
       if(j<num)
       cout<<num;
    }
    cout<<endl;
       num=num+1;
}
 return 0;
















}