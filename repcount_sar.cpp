
#include <iostream>

using namespace std;
int repeatt(int rep);

int main()

{   
    int num1=0,num2=2;
    int cnt=0;
    cin>>num1>>num2;
     for(int i= num1;i<=num2;i++)
     {
      int j=repeatt(i);
      if(j!=0)
       cnt++;
     }
     cout<<(num2-num1)-cnt+1;
    
   

    return 0;
}
int repeatt(int rep)
{
    int arra[5],i=0,flag=0;
   bool arr[12] = {false};
   while(rep>0)
   {
       if(arr[rep%10]==true)
       break;
       arr[rep%10]=true;
       rep=rep/10;
   }
 if(rep!=0)
 flag=1;
  return flag;  
}