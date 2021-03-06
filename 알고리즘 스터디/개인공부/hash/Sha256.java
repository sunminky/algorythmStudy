package ForCodingTest.hash;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class Sha256 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println(new Sha256().makeSha512Hash(scan.next()));
    }
    public String makeSha512Hash(String source){
        MessageDigest messageDigest = null;
        StringBuilder retStr = new StringBuilder();
        try {
            messageDigest = MessageDigest.getInstance("sha-256");
            messageDigest.update(source.getBytes());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        for(byte b: messageDigest.digest())
            retStr.append(String.format("%02x",b));
        return retStr.toString();
    }
}
