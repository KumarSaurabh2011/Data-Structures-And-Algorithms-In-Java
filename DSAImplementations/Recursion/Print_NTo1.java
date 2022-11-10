package DSAImplementations.Recursion;

public class Print_NTo1 {

    public static void  printNumbers(int n){
        if (n==0) {
            return;
        }
        System.out.print(+n +" ");
        printNumbers(n-1);
        System.out.print(+n +" ");


    }
    public static void main(String[] args){
        printNumbers(5);

    }
}
