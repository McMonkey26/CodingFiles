import java.util.Scanner;

public class lab6 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); //creates a scanner to take input from the terminal
    System.out.print("Do you want to convert from or to celsius? "); //prompts the user for which direction theyre going
    boolean toCels = sc.next().equals("to"); //gets the string the user put in, then checks if the user wrote "to"
    System.out.print("What number do you want to convert: "); //prompts the user for their initial temperature
    int initTemp = sc.nextInt(); //gets the temperature the user put in
    int finalTemp = toCels ? ((initTemp-32)*5/9) : (initTemp*9/5+32); //converts the initial temperature to the other unit based on the boolean
    System.out.println(String.format("%d%s is %d%s", initTemp, toCels?"F":"C", finalTemp, toCels?"C":"F")); //prints the user's final temperature
    sc.close(); //closes the scanner for memory purposes
  }
}
