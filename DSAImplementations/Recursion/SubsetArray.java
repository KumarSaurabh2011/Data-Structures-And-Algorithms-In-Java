package DSAImplementations.Recursion;

public class SubsetArray {
    public static void main(String[] args) {
        contiguousSubseq("","ABC");
    }
    static void contiguousSubseq(String p, String up){
        if(up.isEmpty()){
            System.out.println(p);
            return;
        }
        char ch= up.charAt(0);

        contiguousSubseq(p+ch, up.substring(1));
        contiguousSubseq(p,up.substring(1));

    }
}
