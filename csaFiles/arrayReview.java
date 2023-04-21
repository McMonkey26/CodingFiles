import java.util.Scanner;
import java.util.Arrays;

public class arrayReview {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("How many purchases did you make?");
    int numPurchases = sc.nextInt();
    double[] purchases = new double[numPurchases];
    for (int i = 0; i < numPurchases; i++) {
      System.out.println(String.format("How much did item %d cost", i+1));
      purchases[i] = sc.nextDouble();
    }
    sc.close();
    System.out.println(Arrays.toString(purchases));
  }

  public static double median(double[] arr) {
    Arrays.sort(arr);
    if (arr.length % 2 == 1) {
      return arr[arr.length / 2];
    }
    else {
      return (arr[arr.length / 2] + arr[(arr.length - 1) / 2] / 2);
    }
  }

  public static int aboveMed(double[] arr) {
    int retVal = 0;
    double med = median(arr);
    for (double i : arr) {
      if (i > med) {
        retVal++;
      }
    }
    return retVal;
  }

  public static double average(double[] arr) {
    double sum = 0;
    for (double i : arr) {
      sum += i;
    }
    return sum / arr.length;
  }

  public static int aboveAvg(double[] arr) {
    int retVal = 0;
    double avg = average(arr);
    for (double i : arr) {
      if (i > avg) {
        retVal++;
      }
    }
    return retVal;
  }
}