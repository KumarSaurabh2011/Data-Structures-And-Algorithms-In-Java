package DSAImplementations.SlidingWindowProblems;
import java.util.*;
public class CountOfAnagrams {

    public static void main(String[] args) {
        String s="forxxorfxdofr";
        String t="for";
        System.out.println(count(s,t));
    }

    static boolean anagram(String s, String t){

        char[] ch1=s.toCharArray();
        char[] ch2=t.toCharArray();
        Arrays.sort(ch1);
        Arrays.sort(ch2);
        if(Arrays.equals(ch1,ch2)){
            return true;
        }
        return false;
    }
    static int count(String s, String t){
        int count=0;
        int N=s.length();
        int n=t.length();

        for(int i=0;i<=N-n;i++){

            String ans=s.substring(i,i+n);
            if(anagram(t,ans)){
                count++;
            }
        }
        return count;


    }
}
