package ForCodingTest.recursive;

import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        new Factorial().recursive(scanner.nextInt(),1);
    }
    public void recursive(final int n,final int result){  //꼬리재귀로 간다
        if(n <= 1)
            System.out.println(result);
        else
            recursive(n-1,result*n);
    }
}
