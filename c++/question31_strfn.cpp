#include <iostream>
#include <algorithm>
#include "question30_strfn.cpp" // Include the header file for finlen function
using namespace std;
extern int finlen( char str[]);
bool ispal(char a[]){
    int i=0;
    int end = finlen(a)-1; // or sizeof(arr[])/sizeof(arr[0])
    while(a<=end){
        if(a[i]!=a[end])
            return false
            
    }
    a++;
    end--;
return true;
}