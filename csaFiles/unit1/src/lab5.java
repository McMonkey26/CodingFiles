import java.util.Scanner;

public class lab5 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); //Creates a scanner to take in input from the terminal
    System.out.println("Input your full name, separated by spaces:"); //prompts the user for their name
    String fullName = sc.nextLine(); //takes the user's name as a string
    String firstName, midName, lastName; //initializes variables to store the user's name
    firstName = fullName.substring(0, fullName.indexOf(" ")+1); //gets a substring from the start of the full name to the first space
    fullName = fullName.substring(fullName.indexOf(" ")+1); //cuts off the first space and everything before it from the full name variable
    midName = fullName.substring(0, fullName.indexOf(" ")+1); //gets a substring from the start of the modified full name to the only remaining space
    lastName = fullName.substring(fullName.indexOf(" ")+1); //gets a substring from the space to the end of the string
    System.out.println(String.format("Your name is F:%s M:%s L:%s", firstName, midName, lastName)); //prints out the user's separated names
    sc.close(); //closes the scanner for memory
  }
}