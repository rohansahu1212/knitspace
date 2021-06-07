

// Write a java program to demonstrate use of finally block

class java12{  
    public static void main(String args[])throws Exception
    {  
    try{  
     int data=25/2;  
     System.out.println(data);  
    }  
    catch(NullPointerException e)
    {System.out.println(e);}  

    finally
    {System.out.println("finally block is always executed");}  

    System.out.println("rest of the code...");  
    }  
  }  