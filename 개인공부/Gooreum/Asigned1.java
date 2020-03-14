package Gooreum;

import java.util.Scanner;

public class Asigned1 {
    static int arr[][] = {{1,2},{4,4},{7,3},{9,6}};
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int inputNum = scan.nextInt();
        int sum[][] = new int[4][2];
        int answer = 0;
        int tmp = 0;

        for(int i=0;i<arr.length;i++){
            if(inputNum >= arr[i][1]) {
                tmp = recur(new StringBuilder().append(arr[i][0]), inputNum - arr[i][1]);
                if(tmp > answer)
                    answer =tmp;
            }
        }

        System.out.println(answer);
    }
    public static int recur(StringBuilder sum,int rest){
        int max = 0;
        int tmp;
        if(rest < 2) {
            //System.out.println(sum);
            return Integer.parseInt(sum.toString());
        }
        for(int i=0;i<arr.length;i++){
            if(rest >= arr[i][1]) {
                StringBuilder tstr = new StringBuilder(sum);
                tmp = recur(tstr.append(arr[i][0]), rest - arr[i][1]);
                if(tmp > max)
                    max =tmp;
            }

        }
        return max;
    }
}
