public class inheritanceLab {
  public static void main(String[] args) {
    class Parrot {
      private String name;
      private int age;
      private String sound;
      public Parrot() {
        this("polly", 24, "wanna cracker");
      }
      public Parrot(String name, int age, String sound) {
        this.name = name;
        this.age = age;
        this.sound = sound;
      }
      public int getAge() {return age;}
      public void train(String phrase) {
        this.sound = phrase;
      }
      public void speak() {System.out.println(name + sound);}
    }

    class PirateParrot extends Parrot {
      private int legs;
      private String attitude;
      public PirateParrot() {
        super("peter", 24, "I am filled with the rage of a thousand suns");
        this.legs = 6;
        this.attitude = "snarky";
      }
      public PirateParrot(int legs, String attitude, String name, int age, String sound) {
        super(name, age, sound);
        this.legs = legs;
        this.attitude = attitude;
      }
      public void speak() {
        System.out.println("Ah hoy!");
        super.speak();}
    }

    PirateParrot Peter = new PirateParrot();
    Parrot polly = new Parrot();
    Peter.speak();
    polly.speak();
  }
}