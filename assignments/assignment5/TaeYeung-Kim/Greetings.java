import java.util.*;

public class Greetings {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String userName = console.nextLine();
        System.out.println("Hello, " + userName + "! Nice to meet you :)");
        console.close(); 
    }
}
