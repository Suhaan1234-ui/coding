#include <iostream>
#include <cstring>
using namespace std;
int main(){
    cout <<"enter any name"<<" ";
    char str[100];
    cin.getline(str,100);
    int i=0;
    int j= (strlen(str) - 1);
    while(i<j){
        swap( str[i], str[j]);
        i++;
        j--;
    }
    cout << "here is your reversed name"<<"  "<< str;
       return 0;
}