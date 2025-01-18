import java.util.*;
public class majority{
    public static int element(int [] arr){
        int n=arr.length;
        for(int i=0;i<n;i++){
            int count=0;
            for(int j=1;j<n;j++){
                if(arr[j]==arr[i]){
                    count++;
                }
            }
            if(count>n/2){
                return arr[i];
            }
        }
        return -1;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("ENter the value of n");
        int n=sc.nextInt();
        int [] arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        int res=element(arr);
        System.out.println(res);
    }
}
