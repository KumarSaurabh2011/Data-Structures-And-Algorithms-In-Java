package DSAImplementations.SlidingWindowProblems;
/*Brute Force Approach*/
public class MaxSumOfSubArrayOfSizeK {
  public static void main(String[] args) {
       int[] arr = {3,2,5,4,1};
        //System.out.println(maxSum(arr,arr.length,3));
      System.out.println(maxSumOptimized(arr,arr.length,3));

    }
//
//    public static int maxSum(int[] arr, int size, int k){
//        if(size==0 || k==0 || k>size){
//            return -1;
//        }
//
//
//        int max_sum=0;
//        for (int i=0;i<=size-k;i++){
//            int sum =0;
//            for (int j=0;j<k;j++){
//                sum=sum+arr[j+i];
//                if(sum>max_sum)
//                {
//                    max_sum=sum;
//                }
//
//
//            }
//
//        }
//        return max_sum;
//    }
//}

/*optimized approach- Since there is overlap of indexes, we dont need to do recalculation*/

static int maxSumOptimized(int[] arr,int size,int k){

    if(size==0 || k>size || k==0){
        return -1;
    }
    int sum=0;
    int max_sum=sum;

    int start=0;
    for(int i=0;i<k;i++){
        sum+= arr[i];
    }
    for(int j=k;j<size;j++){
        sum+=arr[j]-arr[start++];
        max_sum=Math.max(max_sum,sum);

    }
    return max_sum;
}
}


