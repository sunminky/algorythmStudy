//https://www.acmicpc.net/problem/2230
package TwoPointer;

import java.util.Arrays;
import java.util.Scanner;

public class NumberSelection {
    public static void main(String[] args) {
        new NumberSelection().solution();
    }
    private void solution(){
        Scanner scanner = new Scanner(System.in);
        final int N = scanner.nextInt();    //입력받을 배열개수
        final int M = scanner.nextInt();    //두 수의 차의 최소값
        int[] arr = new int[N];
        int startIdx = 0;
        int minimun = Integer.MAX_VALUE;

        //배열 초기화
        for(int i=0;i<N;i++)
            arr[i] = scanner.nextInt();

        Arrays.sort(arr);   //오름차순으로 정렬

        loop:
        for(int endIdx = 1;endIdx < arr.length;endIdx++){
            for (;startIdx<endIdx;startIdx++){
                if(arr[endIdx] - arr[startIdx] >= M){   //두 수의 차가 M보다 큼
                    if(arr[endIdx] - arr[startIdx] < minimun){  //두 수의 차가 최소값임
                        minimun = arr[endIdx] - arr[startIdx];
                        if (minimun == M)   //최소값이 M임, 더이상 계산할 필요가 없다..!!
                            break loop;
                    }
                }
                else    //arr[endIdx] - arr[startIdx]가 M보다 크지않으면 endIdx++증가시키러 감
                    break;
            }
        }

        System.out.println(minimun);
    }
}
