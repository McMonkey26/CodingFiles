public class Machine {
  private int motorCount;
  private int size;
  private String use;
  private String language;
  private boolean running;
  private boolean working;

  public Machine() {
    motorCount = 2;
    size = 84;
    use = "Sliding Door";
    language = "Python";
    running = false;
    working = true;
  }
  public Machine(int motorCount, int size, String use, String language) {
    this.motorCount = motorCount;
    this.size = size;
    this.use = use;
    this.language = language;
    this.running = false;
    this.working = true;
  }
  public int getMotorCount() {return motorCount;}
  public int getSize() {return size;}
  public String getUse() {return use;}
  public String getLanguage() {return language;}
  public boolean isRunning() {return running;}
  public boolean isWorking() {return working;}

  public void setMotorCount(int motorCount) {this.motorCount = motorCount;}
  public void setSize(int size) {this.size = size;}
  public void setUse(String use) {this.use = use;}
  public void setLanguage(String language) {this.language = language;}
  public void setWorking(boolean working) {this.working = working;}

  public void run() {
    if (!this.working) return;
    if (!this.running) {
      this.running = true;
    } else {
      System.out.println("you broke it");
      this.working = false;
      this.running = false;
    }
  }
  public void stop() {
    this.running = false;
  }
  public void fix() {
    if (this.working) {
      System.out.println("You can't fix what ain't broke");
    }
    else {
      System.out.println("Fixed it");
      this.working = true;
    }
  }

  public String toString() {
    return "Use Case: " + use + ", Size: " + size + " inches, Motors: " + motorCount + ", Language: " + language + ", Running: " + running + ", Working: " + working;
  }
  public boolean equals(Object compare) {
    Machine thing = (Machine)compare;
    return (this.use == thing.use && this.size == thing.size && this.motorCount == thing.motorCount && this.language == thing.language && this.running == thing.running && this.working == thing.working);
  }
}