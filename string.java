public class string
{
	public static void main(String[] args) {
		String ss= "rohanrr";
		int count[] = new int[100];
		String[] ary = ss.split("");
		for(int i =0 ; i<ss.length();i++)
		 {int sum=0;
		     for(int j=0;j<ss.length();j++)
		     {
		        if(ary[i].equals(ary[j]))
		        {
		            sum++;
		            //System.out.println("print at i and j"+i+" "+j);
		        }
		        count[j]=sum;
		    }
		     
		 }
		for(int j=0;j<ss.length();j++)
		    {
		        System.out.println(count[j]);
		    }
		     
	}
}