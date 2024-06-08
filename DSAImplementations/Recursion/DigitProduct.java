package DSAImplementations.Recursion;

public class DigitProduct {
    public static void main(String[] args) {
        int ans = productOfDigits(505);
        System.out.println(ans);
    }
    static int productOfDigits(int n){

        if (n%10==n){
            return n;
        }
        return (n%10)*productOfDigits(n/10);
    }
}
