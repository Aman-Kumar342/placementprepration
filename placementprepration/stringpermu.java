import java.util.*;
public class stringpermu{
    public static void stringpermut(String str,int left,int right){
        if(left==right){
            System.out.println(str);
        }else{
            for(int i=left;i<=right;i++){
                str=swap(str,left,i);
                stringpermut(str, left+1, right);
                str=swap(str,left,i);
            }
        }
    }
    public static String swap(String str,int i,int j){
        char[] charArray = str.toCharArray();
        char temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
        return String.valueOf(charArray);
    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        String in=sc.nextLine();
        stringpermut(in,0,in.length()-1);

    }
}