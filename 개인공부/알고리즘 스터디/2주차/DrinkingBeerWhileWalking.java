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
package ForCodingTest.FloydWarshall;

import java.util.Scanner;

public class DrinkingBeerWhileWalking {
    int storeNum = 0;   //편의점 개수저장
    int[][] interval = null;    //집,편의점,페스티발 간 거리저장
    int[][] storeAddr = null;   //집,편의점,페스티발 위치 저장
    boolean[] visited = null;   //방문여부 저장

    public static void main(String[] args) {
        new DrinkingBeerWhileWalking().solution();
    }

    public boolean searching(final int location){   //loc에서 1000이내이고 방문한적이 없는 편의점 탐색
        boolean result = false;
        visited[location] = true;   //방문도장 찍기
        if(location == storeNum + 1)    //페스티발에 도착함
            return true;
        //loc에서 갈수 있는 위치가 어디인지 찾음
        for (int i = 0; i < interval[location].length; i++) {
            if(interval[location][i] <= 1000 && visited[i] != true && interval[location][i] != 0)
                result = searching(i);
            if(result)  //락페스티발에 도착한 경우
                break;  //탐색 종료
        }
        return result;
    }

    public void solution(){
        Scanner scanner = new Scanner(System.in);
        int testTimes = scanner.nextInt();  //테스트케이스 개수 저장
        boolean[] resultArr = new boolean[testTimes];   //각 테스트케이스별 결과 저장(happy 인지 sad 인지)

        for(int i=0;i<testTimes;i++){
            storeNum = scanner.nextInt();
            visited = new boolean[storeNum+2];  //storeNum + 2 == len(집+편의점들+페스티발)
            storeAddr = new int[storeNum+2][2]; //storeNum + 2 == len(집+편의점들+페스티발)
            interval = new int[storeNum+2][storeNum+2]; //storeNum + 2 == len(집+편의점들+페스티발)

            /**********좌표입력받음**********/
            for(int j=0;j<storeNum+2;j++) {
                storeAddr[j][0] = scanner.nextInt();
                storeAddr[j][1] = scanner.nextInt();
            }
            /**********좌표입력 끝**********/
            /************좌표간 거리 계산************/
            for (int j = 0; j < interval.length; j++) {
                for (int k = 0; k < interval[j].length; k++)
                    interval[j][k] = Math.abs(storeAddr[j][0] - storeAddr[k][0]) + Math.abs(storeAddr[j][1] - storeAddr[k][1]);
            }
            /**********좌표간 거리 계산 끝**********/
            /************경로 탐색************/
            resultArr[i] = searching(0);
            /**********경토 탐색 끝**********/
        }
        for(int i=0;i<resultArr.length;i++) {
            if(resultArr[i])
                System.out.println("happy");
            else
                System.out.println("sad");
        }
    }
}
