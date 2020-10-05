package FenwickTree;

import java.util.Scanner;

public class PortionAdd {
    public static void main(String[] args) {
        new PortionAdd().solution();
    }
    private void solution(){
        Scanner scanner = new Scanner(System.in);
        int indice = scanner.nextInt();
        int tries = scanner.nextInt() + scanner.nextInt();
        int[] tree =new int[indice+1];

        for(int i=0;i<indice;i++){
            tree[i+1] = scanner.nextInt();
            System.out.print(tree[i+1] + " ");
        }
        System.out.println();

        for(int i=0;i<tries;i++){
            int action = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();

            System.out.println(action + ", " + b + ", " + c);
        }
    }
}
