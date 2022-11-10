package DSAImplementations.Recursion;

public class LinearSearch {
    public static void main(String[] args) {
        int[] arr= {1,2,3,4,5,6};
        int target = 9;
        System.out.println(recursiveLinearSearch(arr,target,0));
    }
    static boolean recursiveLinearSearch(int[] arr, int target, int index){
        if(index== arr.length){
            return false;
        }
        return arr[index] == target || recursiveLinearSearch(arr,target,index+1);

    }
}
