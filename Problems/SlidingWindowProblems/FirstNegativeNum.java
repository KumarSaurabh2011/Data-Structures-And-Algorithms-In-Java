package DSAImplementations.SlidingWindowProblems;
/*Brute Force*/
import java.util.*;
public class FirstNegativeNum {
    public static void main(String[] args) {
        int arr[] = {12, -1, -7, 8, -15, 30, 16, 28};
        int n = arr.length;
        int k = 3;
        firstNegNum(arr, n, k);
    }

//    static void firstNegNum(int[] arr, int n, int k) {
//
//        boolean flag;
//
//        for (int i = 0; i < (n -k+1); i++) {
//            flag = false;
//
//            for (int j = 0; j < k; j++) {
//                if (arr[i + j] < 0) {
//                    System.out.print((arr[i + j]) + " ");
//                    flag = true;
//                    break;
//                }
//            }
//
//
//            if (!flag)
//
//                System.out.print("0" + " ");
//        }
//    }
//}

    /*Optimized Approach using Linked List*/
    static void firstNegNum(int arr[], int n, int k) {

        LinkedList<Integer> dq= new LinkedList<Integer>();

        for(int i=0;i<k;i++){
            if(arr[i]<0){
                dq.add(i);
            }

        }
        for(int i=k;i<n;i++){

            if(!dq.isEmpty()){
                System.out.println(arr[dq.peek()]);
            }
            else{
                System.out.println("0"+ " ");
            }
            while(!dq.isEmpty()&& dq.peek()<=(i-k)){
                dq.remove();
            }
            if(arr[i]<0){
                dq.add(i);
            }
        }
        if(!dq.isEmpty()){
            System.out.println(arr[dq.peek()]);
        }
        else{
            System.out.println("0" + " ");
        }

    }
}


