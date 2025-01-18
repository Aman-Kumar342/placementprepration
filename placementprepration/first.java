import java.util.Scanner;
public class first{
    public static void main(String[] args){
      
        System.out.println("1.println");
        System.out.println("2.println");
        // System.out.print("1.print");
        // System.out.print("2.print");
        double number=-10.6;
        System.out.println("I am "+" awesome");
        System.out.println("number="+ number);
        int a = 3;
        int b = 4;
        System.out.println( a + b );
        System.out.println( "3" + "4" );
        System.out.println( "" + (a + b) );
        System.out.println( 3 + 4 + a + " " + b + a );
        System.out.println( "Result: " + a + b );
        System.out.println( "Result: " + ( a + b ) );
        char ch=85;
        char ch1='A';
        System.out.println(ch);
        System.out.println(ch1);
        Scanner in=new Scanner(System.in);
        System.out.println("enter the string s");
        String s=in.nextLine();
        System.out.println("your string is "+ s);

        Scanner sc=new Scanner(System.in);
        int numb=sc.nextInt();
        System.out.println("your number is "+ numb);

        Scanner sc1=new Scanner(System.in);
        int num1=sc1.nextInt();
        System.out.println("your numbr is "+ num1);

        Scanner in1=new Scanner(System.in);
        int num2=in1.nextInt();
        System.out.println("your number is "+ num2);

    }
}