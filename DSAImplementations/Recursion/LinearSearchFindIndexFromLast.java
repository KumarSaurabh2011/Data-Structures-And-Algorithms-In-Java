package DSAImplementations.Recursion;

public class LinearSearchFindIndexFromLast {
    public static void main(String[] args) {
        int arr[]={1,2,3,4,5,6};
        int target = 5;
        System.out.println(findIndexFromLast(arr,target,arr.length-1));
    }
    static int findIndexFromLast(int[] arr, int target, int index){
        if (index==-1){
            return -1;
        }
        if (arr[index]==target){
            return index;
        }
         return findIndexFromLast(arr,target,index-1);
    }
}
