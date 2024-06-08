package DSAImplementations.Recursion;
import java.util.List;
import java.util.ArrayList;
/*Visit this question again one of the imp concepts*/
public class SubsetOfArrayList {
    public static void main(String[] args) {

        int[] arr = {1,2,3};
        List<List<Integer>> ans = subset(arr);
        for(List<Integer> list: ans) {
            System.out.println(list);
        }
    }

    static List<List<Integer>> subset(int[] arr){

        List<List<Integer>> outer = new ArrayList<>();
        outer.add(new ArrayList<>());


        for(int num:arr){

            int n = outer.size();
            for(int i=0;i<n;i++){
                List<Integer> internal = new ArrayList<Integer>(outer.get(i));
                internal.add(num);
                outer.add(internal);


            }
        }
        return outer;

    }
}
