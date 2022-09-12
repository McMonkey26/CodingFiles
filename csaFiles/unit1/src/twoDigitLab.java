import java.util.Scanner;
import java.lang.Math;

public class twoDigitLab {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); //creates a new instance of the Scanner class to take input from the terminal
    System.out.println("How many numbers would you like?"); //prompts the user for how many numbers they want
    int n = sc.nextInt(); //gets the amount of numbers from the user
    boolean rolled13 = false; //initializes a variable to store whether or not the user rolled a 13
    for (int i = 0; i < n; i++) { //sets a loop to repeat as many times as the user entered
      int next = (int)(Math.random()*10)+10; //generates a random number
      System.out.println("next = "+next); //displays it to the user
      if (next == 13) rolled13 = true; //checks if the random number was a 13, and if so, updates the boolean
    }
    if (rolled13) System.out.println("Found a 13!"); //prints to the user whether or not they found a 13
    else System.out.println("no 13 :("); //prints to the user whether or not they found a 13
    sc.close(); //closes the scanner for memory stuff
  }
}