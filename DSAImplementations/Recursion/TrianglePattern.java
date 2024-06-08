package DSAImplementations.Recursion;

public class TrianglePattern {
    public static void main(String[] args) {
         pattern(4,0);

    }
    static void pattern(int row, int columns){
        if(row==0){
            return;
        }
        if(columns<row){
            System.out.print("*");
            pattern(row,columns+1);
        }
        else{
            System.out.println();
            pattern(row-1,0);
        }
    }
}
