import java.util.Random;

public class lab2 {
  public static void main(String[] args) {
    Random rand = new Random();
    int age = 16;
    int minutes = rand.nextInt(301, 999);
    System.out.println(String.format("Age:%d", age));
    System.out.println(String.format("%d minutes is equal\nto %d hours %d minutes", minutes, minutes/60, minutes%60));
    System.out.println((41 % 7 * 3 / 5 + 5 / 2 * 2.5));
  }
}
