#include <stdio.h>
#include<iostream>

using namespace std;

int main()
{  int arr[10]={1,2,3,4,5,6,7,8,10};
   int i=1,x=0;
   
   while(x==0){
       int flag=0;
       for(int j=0;j<sizeof(arr)/sizeof(arr[0]);j++)
       {
           if(i==arr[j])
           {
               flag=1;
           }
       }
       if(flag==0)
       {
           cout<<i;
           break;
          // x=1;
       }
       i++;
   }
    

    return 0;
}