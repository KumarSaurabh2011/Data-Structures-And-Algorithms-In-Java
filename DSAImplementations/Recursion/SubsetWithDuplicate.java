package DSAImplementations.Recursion;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
/*Revisit this question again very Imp*/
/*start pointer is basically first blank arraylist and end pointer is second level blank array list. if we find duplicate that means dup
* number is same as previous level last arraylist. Thats when starts become end+1*/
public class SubsetWithDuplicate {
    public static void main(String[] args) {
        int[] arr = {2,2, 3};
        List<List<Integer>> ans = subsetDuplicate(arr);
        for (List<Integer> list : ans) {
            System.out.println(list);
        }
    }



    static List<List<Integer>> subsetDuplicate(int[] arr) {
        Arrays.sort(arr);
        List<List<Integer>> outer = new ArrayList<>();
        outer.add(new ArrayList<>());
        int start = 0;
        int end = 0;
        for (int i = 0; i < arr.length; i++) {
            start = 0;
            // if current and previous element is same, s = e + 1
            if (i > 0 && arr[i] == arr[i-1]) {
                start = end + 1;
            }
            end = outer.size() - 1;
            int n = outer.size();
            for (int j = start; j < n; j++) {
                List<Integer> internal = new ArrayList<>(outer.get(j));
                internal.add(arr[i]);
                outer.add(internal);
            }
        }
        return outer;
    }
}