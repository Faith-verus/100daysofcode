
import java.util.Random;

public class PasswordGenerator {
    
    public static void main(String[] args)
    {
        //Password length is 18 
        int length = 18; 
        //prints randomly generated password 
        System.out.println(generatePswd(length));
    }
    // method that generates radom password and returns it 
    static char[] generatePswd(int len)
    {
        System.out.println("Your Randomly Generated Password is:");
        String charsCaps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String chars = "abcdefghijklmnopqrstuvwxyz";
        String nums = "0123456789";
        String symbols = "!@#$%^&*_=+-/€.?<>)";

        String passSymbols = charsCaps + chars + nums + symbols;
        Random rnd = new Random();
        char[] password = new char[len];
        int counter = 0;

        
        for (int i = 0; i < len; i++) 
        {
            password[i] = passSymbols.charAt(rnd.nextInt(passSymbols.length()));
            
        }
        return password;
    }  


}
