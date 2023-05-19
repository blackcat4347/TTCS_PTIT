import java.math.BigInteger;
import java.security.SecureRandom;
import java.util.Scanner;

public class RSA {
    private BigInteger p, q, n, e, d;

    public RSA() {
        int bits = 1024;
        // tao 2 so nguyen to
        p = BigInteger.probablePrime(bits / 2, new SecureRandom());
        q = BigInteger.probablePrime(bits / 2, new SecureRandom());  
        // tinh n va phiN
        n = p.multiply(q);
        BigInteger phi = p.subtract(BigInteger.ONE).multiply(q.subtract((BigInteger.ONE)));
        // tìm e
        while(true){
            e = BigInteger.probablePrime(bits / 2, new SecureRandom());
            if(e.compareTo((phi)) < 0 && e.gcd(phi).compareTo(BigInteger.ONE) == 0)
                break;
        }
        d = e.modInverse(phi);//tìm d sao cho d*e=1(mod m)
    }
    
    public String encrypt(String message) {
        BigInteger m = new BigInteger( message.getBytes());
        BigInteger c = m.modPow(e, n);
        return c.toString();
    }
    
    public String decrypt(String message) {
        BigInteger c = new BigInteger(message);
        BigInteger m = c.modPow(d, n);
        return new String(m.toByteArray());
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Plaintext: ");
        RSA rsa = new RSA();
        String message = sc.nextLine();
        String encryptedMessage = rsa.encrypt(message);
        String decryptedMessage = rsa.decrypt(encryptedMessage);
        System.out.println("Encrypted message: " + encryptedMessage);
        System.out.println("Decrypted message: " + decryptedMessage);
    }
}