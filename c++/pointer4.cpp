#include<iostream>
using namespace std;

void print(int *p) {

    cout << *p << endl; 

}

void update(int *p) { 

   // p = p + 1;
   //cout << "inside "<< p <<endl;
   *p = *p + 1; //value(*p) can be updated but not the adresss(p) by pass by adress
                 // as *p tells value inside adress and p is just a variable holding adress

}

int getSum(int *arr /*equivalent to int arr[]*/, int n) {

    cout << endl << "Size : " << sizeof(arr) << endl; //pointer is passed

    int sum = 0;
    for(int i=0;i<n;i++) {
        sum += arr[i];
    }
    return sum;
}

int main() {
/*
    int value = 5;
    int *p = &value;

    //print(p);
    cout <<" Before " << *p << endl; prints 5  in both p and p*
    update(p);
    cout <<" After " << *p << endl; print 6 in p* and 5 in p
    */

    int arr[6] = {1,2,3,4,5,8};
    //benefit of pointer in arrays is that we can send any part of the array

    cout << "Sum is " << getSum(arr+3 ,3) << endl ;  

    return 0;
}