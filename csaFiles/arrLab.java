import java.util.*;

public class arrLab {
  public static void main(String[] args) {
    int[] testArr = {-5, 96, 98, 56, 77};
    System.out.println(average(testArr));
    System.out.println(countAboveAvg(testArr));
    System.out.println(largest(testArr));
    System.out.println(indexOfSmallest(testArr));
    System.out.println(Arrays.toString(testArr));
  }

  public static double average(int[] arr) {
    double sum = 0;
    for (int el : arr) {
      sum += el;
    }
    return (arr.length > 0) ? sum / arr.length : 0.0;
  }

  public static int countAboveAvg(int[] arr) {
    int count = 0;
    for (int el : arr) {
      if (el > average(arr)) {
        count++;
      }
    }
    return count;
  }

  public static int largest(int[] arr) {
    int largest = arr[0];
    for (int el : arr) {
      if (el > largest) {
        largest = el;
      }
    }
    return largest;
  }

  public static int indexOfSmallest(int[] arr) {
    int smallIndex = 0;
    for (int i = 0; i < arr.length; i++) {
      if (arr[i] < arr[smallIndex]) {
        smallIndex = i;
      }
    }
    return smallIndex;
  }
}
