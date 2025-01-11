import java.util.*;
public class leaders{
    public static List<Integer> findl(int [] arr){
        int n=arr.length-1;
        List<Integer> leaders = new ArrayList<>();
        for(int i=0;i<n;i++){ 
            boolean isleader=true;
            for(int j=i+1;j<n;j++){
                if(arr[i]<=arr[j]){
                    isleader=false;
                    break;
                }
            }
            if(isleader){
            leaders.add(arr[i]);
            }
        }
        return leaders;
    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int [] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        List<Integer>leaders=findl(arr);
        System.out.print(leaders);

    }
}