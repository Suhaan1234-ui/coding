#include <iostream> // MAKE A BANK WHICH WITHDRAWS OR ENTER MONEY 
#include <string> // and gives people associated and money
using namespace std;

class bank{
  string name;
  int accno, balance;
  static int people;
  static int paise;
  public:
  static double money(bool a , int b){
      if(a){
     paise = paise + b;
     cout<<paise<<endl;
     return paise;
          
      }
     if (!a && paise>=b){
       paise = paise -b;
       cout<<paise<<endl;
       return paise;
     }
     else 
       return 0;
     
  }

  bank(string n, int a, int b){
      cout<< "number of people registered with this bank"<<people<<endl;
      name =n;
      accno=a;
      balance=b;
      people++;
      cout<<people<<endl;
  }
 void display(bool a){
     cout<<"enter 1 to submit and 0 to withdraw"<<endl;
 }
  
  
  
};
int bank :: paise=10000;
int bank :: people=0;

int main(){
    bank c1("suhaan", 234 , 5000);
    c1.display(1);
    bank :: money(1,5000);
}