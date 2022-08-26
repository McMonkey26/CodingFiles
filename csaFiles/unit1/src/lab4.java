import java.util.Scanner;

public class lab4 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); //Creates a scanner to take in input from the terminal
    System.out.print("Input a word:"); //prompts the user for a word
    String str = sc.next(); //takes in the user's word
    System.out.println("\nYour word had an 'a' at index "+str.indexOf("a")); //prints an output statement, and gets the index of the first a, and adds it to the output statement
    sc.close(); //close the scanner for memory issues
  }
}
