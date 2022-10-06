public class Cat {
  private int age;
  private String name;
  private boolean longHair;
  private String color;
  private double weight;

  public Cat() {
    age = 5;
    name = "Fido";
    longHair = false;
    color = "Orange";
    weight = 12.75;
  }
  public Cat(int age, String name, boolean longHair, String color, double weight) {
    this.age = age;
    this.name = name;
    this.longHair = longHair;
    this.color = color;
    this.weight = weight;
  }

  public int getAge() {return age;}
  public String getName() {return name;}
  public boolean getLongHair() {return longHair;}
  public String getColor() {return color;}
  public double getWeight() {return weight;}

  public void setAge(int age) {this.age = age;}
  public void setName(String name) {this.name = name;}
  public void setLongHair(boolean longHair) {this.longHair = longHair;}
  public void setColor(String color) {this.color = color;}
  public void setWeight(double weight) {this.weight = weight;}

  public void getDirty() {this.color = "Brown";}
  public void meow() {System.out.println("Meow! " + this.name);}
  public boolean isHealthy() {return (this.age < 4 && this.weight < 15.0);}
  public String toString() {return String.format("age:%d, name:%s, longHair:%b, color:%s, weight:%f", age, name, longHair, color, weight);}
}