#include <iostream>
using namespace std;
int main(){

cout<<"enter your percentile : "<<endl;
double percentile ;
cin>>percentile; //.1 percentile= 1400 rank 

if (percentile >= 93.10){
    cout<<"congrats!! you are qualified for jee advanced "<<endl;
    double result ;
    result = (100-percentile)*14000;
    cout<<"here is your rank: "<<result<<endl;
    if (percentile > 99 )
       cout<<" you can get into top NIT's and govt collages"<<endl;
    else
        cout<<"you can get into govt collages"<<endl;
        
}
else {
     cout<< "you are not qualified for jee advance"<<endl;
     double result ;
     result = (100-percentile)*14000;
     cout<<"here is your rank: "<<result;
}
return 0;













}