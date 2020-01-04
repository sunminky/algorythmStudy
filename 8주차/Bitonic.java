package week8;

import java.util.Arrays;
import java.util.Scanner;

public class Bitonic {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int len = scan.nextInt();
        int arr[] = new int[len];
        int result = 0;

        for(int i = 0;i < len;i++)
            arr[i] = scan.nextInt();

        result = new Bitonic().solution(arr,len);
        System.out.println(result);
    }
    public int solution(int[] arr,int len){
        int maxResult = 0;
        int result[][] = new int[2][];

        result[0] = lis(arr,len);
        result[1] = lds(arr,len);

        /*for(int x : result[0])
            System.out.print(x + " ");
        System.out.println();

        for(int x : result[1])
            System.out.print(x + " ");
        System.out.println();

        for(int i = 0;i < result[0].length && i < result[1].length;i++)
            System.out.print(result[0][i] + result[1][i] + " ");
        System.out.println();*/

        for(int i = 0;i < result[0].length && i < result[1].length;i++)     //lds와 lis의 합이 가장 큰 부분 찾기
            if(result[0][i] + result[1][i] > maxResult)
                maxResult = result[0][i] + result[1][i];

        return maxResult - 1;
    }
    public int[] lis(int[] arr,int len){
        int[] result = new int[len];

        Arrays.fill(result,1);
        for(int i = 1;i<len;i++){
            for(int j = 0;j<i;j++){
                /*
                i번째 요소가 j번째 요소보다 크면 arr[i] = arr[j] + 1
                 */
                if(arr[i] > arr[j])
                    if(result[i] < result[j] + 1)
                        result[i] = result[j] + 1;
            }
        }
        return result;
    }
    public int[] lds(int[] arr,int len){
        int[] result = new int[len];

        Arrays.fill(result,1);
        for(int i = len - 2;i>=0;i--){  //뒤에서 부터 탑색하는 lis랑 같음
            for(int j = len-1;j>i;j--){
                /*
                i번째 요소가 j번째 요소보다 작으면 arr[i] = arr[j] + 1
                 */
                if(arr[i] > arr[j])
                    if(result[i] < result[j] + 1)
                        result[i] = result[j] + 1;
            }
        }
        return result;
    }
}
