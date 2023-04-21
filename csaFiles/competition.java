import java.util.*;

public class competition {
  public static void main(String[] args) {
    Machine m1 = new Machine();
    Machine m2 = new Robot();
    Robot m3 = new VexRobot();
    Robot m4 = new Robot();
    VexRobot m5 = new VexRobot();
    Machine m6 = m1;
    VexRobot m7 = new VexRobot();
    Machine m8 = new VexRobot();
    Robot m9 = m3;
    VexRobot sal = new VexRobot("Sal", "4 wheel drive", true, 2, false, 8, 18, "Python");
    sal.runAuton();
    System.out.println(sal);

    int[] data = new int[8];
    data[0] = 1;
    data[7] = -18;
    data[4] = 5;
    data[1] = data[0];

    int x = data[4];
    data[4] = 6;
    data[x] = data[0] * data[1];

    System.out.println(Arrays.toString(data));
  }
}
