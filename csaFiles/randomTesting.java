import java.util.Scanner;

public class randomTesting {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("started");
    char[] inp = sc.nextLine().toCharArray();
    String out = "";
    for (char elem : inp) {
      out = elem + out;
    }
    sc.close();
    System.out.println(out);
  }
}