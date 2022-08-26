import java.util.Scanner; //lets you access the Scanner class


public class lab3 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); //Creates a scanner to take in input from the terminal
    System.out.println("give me a 3 digit number"); //prompts the user for a number
    int num = sc.nextInt(); //gets the number from the user
    while (num <= 99 || num >= 1000) { //makes sure the number is 3 digits
      System.out.println("no, a 3 digit number"); //prompts the user for a new number
      num = sc.nextInt(); //gets the new number from the user
    }
    int hundreds, tens, ones; //initializes the variables for each digit
    hundreds = num / 100; //gets the hundreds place of your number
    tens = (num / 10) % 10; //gets the tens place of your number
    ones = num % 10; //gets the ones place of your number
    System.out.println(String.format("%d is in the hundreds, %d is in the tens, and %d is in the ones place", hundreds, tens, ones)); // prints out the places of your number
    sc.close(); //closes the scanner to prevent a memory leak
  }
}
