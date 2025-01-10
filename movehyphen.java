// public class movehyphen {
//     public static void main(String[] args) {
//         String input = "java-code-example";
//         String result = moveHyphenToBeginning(input);
//         System.out.println(result); // Output: -javacodeexample
//     }

//     public static String moveHyphenToBeginning(String input) {
//         if (input == null || !input.contains("-")) {
//             return input;
//         }
        
//         String withoutHyphen = input.replace("-", ""); // Remove all hyphens
//         return "-" + withoutHyphen;
//     }
// }
import java.util.*;
public class movehyphen{
    public static String movr(String str){
        if(str==null || !str.contains("-")){
            return str;
        }
        String without=str.replace("-","");
        return "-"+ without;
    }
    public static void main(String [] args){
        Scanner sc=new Scanner(System.in);
        String str= sc.nextLine();
        String res=movr(str);
        System.out.print(res);
    }
}
