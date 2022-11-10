package DSAImplementations.Recursion;
import java.util.ArrayList;


public class ReturnArrayListOfSubset {
    public static void main(String[] args) {

        System.out.println (contigousSubseq("", "abc"));
    }

    static ArrayList<String> contigousSubseq(String P, String up){

        if(up.isEmpty()){
            ArrayList<String> list=new ArrayList<String>();
            list.add(P);
            return list;
        }
        char ch = up.charAt(0);

        ArrayList<String> Left = contigousSubseq(P+ch, up.substring(1));
        ArrayList<String> Right = contigousSubseq(P, up.substring(1));
        Left.addAll(Right);
        return Left;
    }
}
