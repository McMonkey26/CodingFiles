import java.util.Scanner;

public class timesTableLab {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int num = sc.nextInt();
    for (int i = 1; i <= num; i++) {
      for (int j = 1; j <= 10; j++) {
        System.out.print("" + j * i + "\t");
      }
      System.out.println();
    }
    sc.close();
  }
}
