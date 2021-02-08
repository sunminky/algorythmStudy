package ForCodingTest.Loop;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Score {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[][] arr = new int[8][2];
        int[] arr2 = new int[5];
        int sum = 0;

        for(int i=0;i<8;i++){
            arr[i][0] = i;
            arr[i][1] = scanner.nextInt();
        }
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o2[1],o1[1]);
            }
        });
        for(int i=0;i<5;i++){
            sum += arr[i][1];
            arr2[i] = arr[i][0]+1;
        }
        Arrays.sort(arr2);
        System.out.println(sum);
        for (int x:arr2)
            System.out.print(x+" ");
    }
}
