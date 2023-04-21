import java.lang.Math;

public class Robot extends Machine {
  private int batteryLevel;
  private String movement;
  private boolean sentient;

  public Robot() {
    super(5, 12, "RC Car", "Assembly");
    batteryLevel = 100;
    movement = "4 Wheel drive";
    sentient = false;
  }
  public Robot(String movement, boolean sentient, int motors, int size, String use, String language) {
    super(motors, size, use, language);
    this.batteryLevel = 100;
    this.movement = movement;
    this.sentient = sentient;
  }

  public int getBatteryLevel() {return batteryLevel;}
  public String getMovement() {return movement;}
  public boolean getSentience() {return sentient;}

  public void setMovement(String movement) {this.movement = movement;}
  public void setSentience(boolean sentient) {
    if (this.sentient) {System.out.println("no fuck you im staying here");}
    else {this.sentient = sentient;}
  }
  public void useBattery(int amt) {batteryLevel -= amt;}

  public void move(int distance) {
    if (!isWorking()) {return;}
    this.run();
    if (sentient) {
      System.out.println("I move where I want to. fuck you");
      distance = (int)(50*Math.random());
    }
    if (batteryLevel >= distance) {
      batteryLevel -= distance;
    } else {
      distance = batteryLevel;
      batteryLevel = 0;
      setWorking(false);
    }
    if (!sentient) {System.out.println("You moved " + distance + " inches and your battery is " + ((batteryLevel > 0) ? ("at " + batteryLevel + " percent") : "fucking dead lmao"));}
    this.stop();
  }

  public void charge(int timeCharging) {
    batteryLevel += timeCharging;
    setWorking(true);
    if (batteryLevel > 100) {
      setWorking(false);
      System.out.println("you broke it. don't charge for that long");
    }
  }
  public void fix() {
    System.out.println(isWorking() ? "You broke it :(" : "It works now");
    setWorking(!isWorking());
  }

  public String toString() {
    return super.toString() + "\nBattery: " + batteryLevel + "%, Movement: " + movement + ", Sentient: " + sentient;
  }
}
