/*https://www.acmicpc.net/problem/9205*/
/*
2   //테스트 케이스 개수
2   //편의점 개수
0 0 //집주소
1000 0  //편의점1
1000 1000   //편의점2
2000 1000   //페스티발 장소
2   //편의점 개수
0 0 //집주소
1000 0  //편의점1
2000 1000   //편의점2
2000 2000   //페스티발 장소
 */
package BeakJoon;

import java.util.Scanner;

public class DrinkingBeerWhileWalking {
    public static void main(String[] args) {
        boolean result = false;
        Scanner scanner = new Scanner(System.in);
        int testTimes = scanner.nextInt();
        boolean[] resultArr = new boolean[testTimes];
        int storeNum = 0;
        int[] storeAddr = new int[2];
        int previousLocation[] = new int[2];
        int[] festivalAddr = new int[2];

        for(int i=0;i<testTimes;i++){
            result = true;
            storeNum = scanner.nextInt();
            previousLocation[0] = scanner.nextInt();
            previousLocation[1] = scanner.nextInt();

            for(int j=0;j<storeNum;j++) {
                storeAddr[0] = scanner.nextInt();
                storeAddr[1] = scanner.nextInt();
                if(Math.abs(storeAddr[0] - previousLocation[0]) + Math.abs(storeAddr[1] - previousLocation[1]) > 1000)
                    result = false;
                previousLocation[0] = storeAddr[0];
                previousLocation[1] = storeAddr[1];
            }

            festivalAddr[0] = scanner.nextInt();
            festivalAddr[1] = scanner.nextInt();

            if(Math.abs(festivalAddr[0] - previousLocation[0]) + Math.abs(festivalAddr[1] - storeAddr[1]) > 1000)
                result = false;

            resultArr[i] = result;
        }
        for(int i=0;i<resultArr.length;i++) {
            if(resultArr[i])
                System.out.println("happy");
            else
                System.out.println("sad");
        }
    }
}
