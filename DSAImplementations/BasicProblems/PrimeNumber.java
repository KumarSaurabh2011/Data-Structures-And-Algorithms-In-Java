package DSAImplementations.BasicProblems;

import java.util.Scanner;

public class PrimeNumber {

 // Function to check if a number is prime
 public static boolean isPrime(int num) {
  // Corner cases
  if (num <= 1) {
   return false;
  }
  if (num == 2 || num == 3) {
   return true;
  }
  if (num % 2 == 0 || num % 3 == 0) {
   return false;
  }

  // Check from 5 to the square root of the number
  for (int i = 5; i * i <= num; i += 6) {
   if (num % i == 0 || num % (i + 2) == 0) {
    return false;
   }
  }

  return true;
 }

 public static void main(String[] args) {
  Scanner scanner = new Scanner(System.in);

  // Prompt the user to enter a number
  System.out.print("Enter a number: ");
  int number = scanner.nextInt();

  // Check if the number is prime and print the result
  if (isPrime(number)) {
   System.out.println(number + " is a prime number.");
  } else {
   System.out.println(number + " is not a prime number.");
  }

  scanner.close();
 }
}

