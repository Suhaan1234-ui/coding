#include <iostream>
#include <string>
using namespace std;
string touppercase(string s){
    for(int i=0; i<s.length(); i++){
        bool gap = ' ';
        if(gap)
           cout<<' ';
        else
        s[i]= s[i] - 'a' +'A';
    }
    return s;

}
int main(){
    cout<<"Enter a name or sentence";
    string s;
    getline(cin,s);
    cout<<touppercase(s);


}