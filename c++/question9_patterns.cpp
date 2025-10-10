// to print a pattern with single digit 1 by taking an input from the user
#include <iostream>
using namespace std;
int main (){

cout<<"enter the number of rows";
int row;
cin>>row;+-

cout<<"enter the number of columns";
int col;
cin>>col;       

      for (int k=1 ; k<=row; k++){
               for(int i=1; i<=col; i+=1){     
                                    cout<<"1";
               }
       cout<<endl;
            }

return 0;
}