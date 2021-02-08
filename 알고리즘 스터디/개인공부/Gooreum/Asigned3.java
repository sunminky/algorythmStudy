package Gooreum;
import java.util.Arrays;
import java.util.Scanner;

public class Asigned3 {
        public static void main(String[] args) throws Exception {
            Scanner sc= new Scanner(System.in);
            int inputNum = sc.nextInt();
            int K = sc.nextInt();
            int arr[] = new int[inputNum];

            for (int i=0;i<inputNum;i++) {
                arr[i] = sc.nextInt();
            }
            Arrays.sort(arr);
            System.out.println(arr[inputNum-K]-arr[0]);
        }

}
