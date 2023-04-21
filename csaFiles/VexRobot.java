import java.lang.Math;
public class VexRobot extends Robot {
  private int points;
  private int disksLoaded;
  private String name;
  private boolean hasAuton;

  public VexRobot() {
    super("4 Wheel Drive", false, 8, 18, "VRC", "Python");
    points = 0;
    name = "Gús";
    hasAuton = false;
    disksLoaded = 0;
  }
  public VexRobot(String name, String movement, boolean hasAuton, int disksLoaded, boolean sentient, int motors, int size, String language) {
    super(movement, sentient, motors, size, "VRC", language);
    this.points = 0;
    this.name = name;
    this.hasAuton = hasAuton;
    this.disksLoaded = disksLoaded;
  }

  public int getPoints() {return points;}
  public int getDisks() {return disksLoaded;}
  public String getName() {return name;}
  public boolean getAuton() {return hasAuton;}
  public void intakeDisk() {
    if (!isWorking()) {return;}
    useBattery(2);
    disksLoaded++;
    if (disksLoaded > 3) {
      setWorking(false);
      System.out.println("You cannot load more than 3 disks at once.");
    }
  }
  public void launchDisk() {
    if (!isWorking() || disksLoaded <= 0) {return;}
    useBattery(3);
    disksLoaded--;
    if (Math.random() >= 0.7) {
      points += 5;
      System.out.println("Nice Shot! " + disksLoaded + " disks loaded, " + points + " points");
    } else {
      points -= 1;
      System.out.println("Woops! Your aim sucks! " + disksLoaded + " disks loaded, " + points + " points");
    }
  }
  public void turnRoller() {
    if (!isWorking()) {return;}
    useBattery(2);
    points += 20;
  }

  public void runAuton() {
    if (!isWorking() || !hasAuton) {return;}
    launchDisk();
    launchDisk();
    move(20);
    turnRoller();
    move(20);
    intakeDisk();
    intakeDisk();
    intakeDisk();
    move(20);
    launchDisk();
    launchDisk();
    launchDisk();
  }
  public void move(int distance) {
    super.move(distance / 3);
  }

  public void launchEndgame() {
    int tilesCovered = (int)(Math.random() * 15);
    points += 3 * tilesCovered;
  }
  public String toString() {
    return "Gus (" + (hasAuton ? "has auton" : "no auton") + ", " + disksLoaded + " disks, " + points + " points)\n" + super.toString();
  }
}