package DSAImplementations.Recursion;

public class Sum {
    public static void main(String[] args) {
        int ans = sumOfNumber(5);
                System.out.println(ans);

    }
    public static int sumOfNumber(int n){
        if (n<=1){
            return 1;
        }
        return n+sumOfNumber(n-1);

    }

}
