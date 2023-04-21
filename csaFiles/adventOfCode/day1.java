package adventOfCode;

public class day1 {
  public static void main(String[] args) {
    String[] words = new String[]{"ten", "fading", "post", "card", "thunder", "hinge", "trailing", "batting"};
    for (String str : words)  {
      if (str.substring(str.length()-3).equals("ing")) {
        System.out.println(str);
      }
    }
  }
}