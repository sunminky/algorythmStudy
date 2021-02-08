package Gooreum;

import java.util.Scanner;

public class DistinguishPrime {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int prime = scanner.nextInt();

        if(prime %2 == 0) {
            System.out.println("False");
            return;
        }

        int root = (int) Math.sqrt(prime);
        for(int i=3;i <= root;i+=2){
            if(prime % i ==0){
                System.out.println("False");
                return;
            }
        }
        System.out.println("True");
    }
}
