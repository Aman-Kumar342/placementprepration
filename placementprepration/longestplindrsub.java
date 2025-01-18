import java.util.*;
public class longestplindrsub{
    public static boolean ispalind(String str){
        int left=0;
        int right=str.length()-1;
        while(left<right){
            if(str.charAt(left)!=str.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
    public static String longestpalind(String str){
        if(str==null || str.length()<1){
            return "";
        }
        int maxlength=0;
        String res="";
        for(int i=0;i<str.length();i++){
            for(int j=i+1;j<str.length();j++){
                String substr=str.substring(i,j);
                if(ispalind(substr) && substr.length()>maxlength){
                    res=substr;
                    maxlength=substr.length();
                }
            }
        }
        return res;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        String str=sc.nextLine();
        String res=longestpalind(str);
        System.out.println(res);
    }
}