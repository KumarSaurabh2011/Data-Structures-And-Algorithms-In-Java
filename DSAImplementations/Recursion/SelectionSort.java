package DSAImplementations.Recursion;
/*Revise this code again*/

import java.util.Arrays;

public class SelectionSort {
    public static void main(String[] args) {
        int[] arr = {4, 3, 2, 1};
        sorting(arr, arr.length, 0,0);
        System.out.println(Arrays.toString(arr));

    }
    static void sorting(int[] arr, int length,int c,int max){
        if(length==0){
            return;
        }
        if(c<length){
            if(arr[c]>arr[max]){
                sorting(arr,length,c+1,c);

            }else {
                sorting(arr,length,c+1,max);
            }

        }else{
            int temp=arr[max];
            arr[max]=arr[length-1];
            arr[length-1]=temp;
            sorting(arr,length-1,0,0);
        }
    }
}
