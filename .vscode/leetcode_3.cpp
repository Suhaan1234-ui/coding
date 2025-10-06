#include <iostream>
#include <cmath>
using namespace std;
int main(){
    
    cout<<"enter any number ";
    int n;
    cin>>n;
    int b;
    int j=0;
    int i=0;
    while(n!=0){
        

       if (j > (pow(2,31) - 1) / 10 ||  j< (pow(-2,31) / 10)) {
            return 0;
        }
        else{
        b=n%10;
       j=j*10+b;
       
        n=n/10;
    i++;
        
    } 
}
    cout<<j;

}