package week8;

import java.util.Arrays;
import java.util.Scanner;

public class Lis {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int len = scan.nextInt();
        int arr[] = new int[len];
        int result = 0;

        for(int i = 0;i < len;i++)
            arr[i] = scan.nextInt();

        result = new Lis().solution(arr,len);
        System.out.println(result);
    }

    public int solution(int[] arr,int len){
        int[] result = new int[len];

        Arrays.fill(result,1);
        for(int i = 1;i<len;i++){   //https://www.youtube.com/watch?v=CE2b_-XfVDk 참고
            for(int j = 0;j<i;j++){
                /*
                i번째 요소가 j번째 요소보다 크면 arr[i] = arr[j] + 1
                 */
                if(arr[i] > arr[j])
                    if(result[i] < result[j] + 1)
                        result[i] = result[j] + 1;
            }
        }
       return maxValue(result);
    }

    public int maxValue(int[] arr){
        int max = 0;
        for(int i = 0;i < arr.length;i++)
            if(arr[i] > max)
                max = arr[i];
        return max;
    }
}
