package DSAImplementations.Recursion;

public class SumOfDigits {
    public static void main(String[] args) {
        int ans = digitSum(1342);
        System.out.println(ans);

    }
    static int digitSum(int n){
        if(n%10==n){
            return n;}
        return (n%10)+digitSum(n/10);

    }
}
