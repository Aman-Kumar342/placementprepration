import java.util.*;
public class stockspan{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int []price=new int[n];
        int [] span=new int [n];
        for(int i=0;i<n;i++){
            price[i]=sc.nextInt();
        }
        for(int i=0;i<n;i++){
            span[i]=1;
            for(int j=i-1;j>=0;j--){
                if(price[j]<=price[i]){
                    span[i]++;
                }
                else{
                    break;
                }
            }
        }
        for(int i=0;i<n;i++){
            System.out.print(span[i]+" ");
        }
        

    }
}