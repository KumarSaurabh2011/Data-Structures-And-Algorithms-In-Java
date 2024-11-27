package DSAImplementations.Recursion;
/*Revise this code again plz*/
import java.util.*;
public class BubbleSort {
    public static void main(String[] args) {
        int[] arr = {4, 3, 2, 1};
        sorting(arr, arr.length-1, 0);
        System.out.println(Arrays.toString(arr));

    }

    public static void sorting(int[] arr, int length, int c) {

        if (length == 0) {
            return;
        }
        if (c < length) {
            if (arr[c] > arr[c + 1]) {
                int temp = arr[c];
                arr[c] = arr[c + 1];
                arr[c + 1] = temp;
            }
            sorting(arr,length,c+1);
        }
        sorting(arr,length-1,c);
    }
}
