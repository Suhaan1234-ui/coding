#include <iostream>
using namespace std;
int main(){
  char ch='a';
  cout<<"enter the number of rows < 5  ";
  int row;
  cin>>row;
   
  cout<<"Enter the number of columns<5  ";
  int col;
  cin>>col;
   
  while(col>=5 || row>=5 ){
     cout<<"invalid input"<<endl;
      cout<<"enter the number of rows < 5  ";
      cin>>row;
   
  cout<<"Enter the number of columns<5  ";
  cin>>col;
  }

  for(int i=0; i<row; i++){
    for ( int j=0 ; j<col; j++){
        cout<< char(ch + j)<<" ";
        /*   or
        cout<<ch;
        ch =ch +1;
    and no need to use ch = ch +col;
        */
    }
     ch = ch + col ;
    cout<<endl;
  }
  return 0;
} 