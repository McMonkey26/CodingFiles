import java.util.Scanner;

public class timesTableLab {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); //creates a new scanner object to take input
    int num = sc.nextInt(); //gets a number from the user
    for (int i = 1; i <= num; i++) { //iterates up to the number
      for (int j = 1; j <= 10; j++) { //iterates up to ten
        System.out.print("" + j * i + "\t"); //prints out the current number multiplied by the value to ten, separated by tabs
      }
      System.out.println(); //goes to a new line
    }
    sc.close(); //closes the scanner object for memory purposes
  }
}
