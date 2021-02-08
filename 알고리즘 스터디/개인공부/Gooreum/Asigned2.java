package Gooreum;

import java.util.Scanner;

public class Asigned2 {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int n, x, y;
        boolean chk;
        n = scanner.nextInt();
        int arr[][];

        for (int i = 0; i < n; i++) {
            y = scanner.nextInt();
            x = scanner.nextInt();
            chk = true;
            arr = new int[y][x];
            for (int a = 0; a < y; a++) {
                for (int b = 0; b < x; b++) {
                    arr[a][b] = scanner.nextInt();
                }
            }

            for (int a = 1; a < y; a++) {
                for (int b = 1; b < x; b++) {
                    if ((arr[a - 1][b - 1] != 0)) {
                        if(arr[a][b - 1] != 0) {
                            if (arr[a - 1][b] != 0) {
                                if (arr[a][b] != 0) {
                                    arr[a - 1][b - 1] = 7;
                                    arr[a - 1][b] = 7;
                                    arr[a][b - 1] = 7;
                                    arr[a][b] = 7;
                                }
                            }
                        }
                    }
                }
            }
            for (int a = 0; a < y; a++) {
                for (int b = 0; b < x; b++) {
                    if (arr[a][b] == 1){
                        chk = false;
                    }
                }
            }
            if (chk) {
                System.out.println("YES");
            } else
                System.out.println("NO");
        }
    }
}

