#include <stdio.h>
#include <math.h>
int main(){
 int n,r,a=0,c=0,b;
 printf("enter the number:");
 scanf("%d",&n);
 b=n;
 while (n!=0){
    c++;
    n=n/10;
    
 }
 n=b;
 while(b!=0){
     r=b%10;
     a= a + pow(r,c);
     b=b/10;
 }
 if(n==a)
    printf("the given number is an armstrong number");
 else 
    printf("the given number is not an armstrong number");
 return 0;
}