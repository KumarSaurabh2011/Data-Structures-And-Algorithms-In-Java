package DSAImplementations.Recursion;

public class LinearSearchReturnIndex {
    public static void main(String[] args) {
        int[] arr ={1,2,3,4,5,6};
        int target = 5 ;
        System.out.println(returnIndex(arr,target,0));
    }
    static int returnIndex(int[] arr, int target, int index){
        if(index==arr.length){
            return -1;
        }
        if (arr[index]==target){
            return index;
        }
        return returnIndex(arr,target,index+1);
    }
}
