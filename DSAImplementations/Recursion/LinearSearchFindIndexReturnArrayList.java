package DSAImplementations.Recursion;

import java.util.ArrayList;

public class LinearSearchFindIndexReturnArrayList {
    public static void main(String[] args) {
        int[] arr= {1,2,3,4,5,5,6};
        int target = 5;

        System.out.println(returnArrayList(arr,target,0, new ArrayList<> ()));
    }
    static ArrayList<Integer> returnArrayList(int[] arr, int target, int index, ArrayList<Integer> list ){
        if (index==arr.length){
            return list ;
        }
        if (arr[index]==target){
            list.add(index);

        }
        return returnArrayList(arr,target,index+1,list);

    }
}
