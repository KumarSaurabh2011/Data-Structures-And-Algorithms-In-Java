package DSAImplementations.Recursion;
import java.util.ArrayList;


public class ReturnArrayListOfSubsetWithAsciiValue {
    public static void main(String[] args) {
        System.out.println(contigousSubseq("","abc"));

    }

    static ArrayList<String> contigousSubseq(String P, String up){
        if(up.isEmpty()){

            ArrayList<String> list = new ArrayList<String> ();
            list.add(P);
            return list;
        }
        char ch = up.charAt(0);

        ArrayList<String> left=contigousSubseq(P+ch,up.substring(1));
        ArrayList<String> Ascii=contigousSubseq(P+(ch+0),up.substring(1));
        ArrayList<String> right=contigousSubseq(P,up.substring(1));
         left.addAll(right);
         left.addAll(Ascii);
         return left;


    }
}
