import java.util.Scanner;

public class labFactors {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); //creates a scanner to take in input from the terminal
    int factors = 0; //initializes a variable to store the number of factors of your input
    int check = 1; //initializes a variable to check if your input is divisible by every number
    System.out.println("insert a number"); //prompts the user for input
    int num = sc.nextInt(); //gets the user's input number
    while (check <= num) { //loops until the factor check exceeds the input number
      if (num % check == 0) { //checks if the input number is divisible by the factor check
        factors++; //increments the number of factors
      }
      check++; //increments the factor check
    }
    System.out.println(num+" has "+factors+" factors"); //prints out the number of factors
    sc.close(); //closes the scanner for memory leak purposes
  }
}
