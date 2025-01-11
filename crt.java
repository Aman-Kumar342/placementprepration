public class crt {
    public static int findX(int num1, int rem1, int num2, int rem2) {
        int x = 1;
        while (true) {
            if (x % num1 == rem1 && x % num2 == rem2) {
                return x; 
            }
            x++;
        }
    }

    public static void main(String[] args) {
        int num1 = 7, rem1 = 2;
        int num2 = 11, rem2 = 3;

        int x = findX(num1, rem1, num2, rem2);

        System.out.println("The smallest x satisfying the given congruences is: " + x);
    }
}
