
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
    int arr[5],i=0,flag=0;
    while(rep>0)
    {arr[i]=rep%10;
    rep=rep/10;
    i++;
        
    }
    for(int r=0;r<i;r++)
    {
        for(int s=r+1;s<i;s++)
        {if(arr[r]==arr[s])
        {flag++;
            
        }
        }
        
    }
    
  return flag;  
}