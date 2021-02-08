/*https://level.goorm.io/exam/49060/%EA%B0%9C%EB%AF%B8-%EC%A7%91%ED%95%A9%EC%9D%98-%EC%A7%80%EB%A6%84/quiz/1*/
package goorm;

import java.util.Arrays;
import java.util.Scanner;

public class Ant {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt(); //전체 개미수
        int d = scan.nextInt(); //줄이고 싶은 반지름 수
        int ant[] = new int[N];     //개미들 위치 저장
        int min = Integer.MAX_VALUE;    //최소로 죽여야 하는 개미
        int killIndicator = 0;      //개미를 앞에서 부터 어디까지 죽였는가 표시

        for(int i=0;i<N;i++){
            ant[i] = scan.nextInt();    //개미 입력 받음
        }
        Arrays.sort(ant);   //오름차순 정렬
        if(ant[N-1] - ant[0] <= d){ //이미 조건을 만족(현재 d보다 작음)하면 종료
            System.out.println(0);
            return;
        }

        for(int i=killIndicator;i<N;i++){
            for(int j=i;j<N;j++){
                if(ant[j] - ant[i] <= d){   //현재 개미와 죽은 개미를 제외하고 제일 앞에 있는 개미와 거리 비교
                    if(N-j-1 + i < min) {   //뒤에서 부터 죽인 개미 + 앞에서 부터 죽인 개미 < 최소값
                        //System.out.println(min + " -> " + (N - j-1 + i) );
                        min = N - j-1 + i;  //최소값 갱신
                    }
                }
                else {  //이 개미 뒤에있는 개미들은 조건을 만족하지 못함(d보다 큼)
                    for(int k = killIndicator;k <= j;k++){  //앞에서 개미를 얼마나 죽여야 d를 만족 할수 있는지 확인
                        if(ant[j] - ant[k] <= d) {
                            killIndicator = k;
                            break;
                        }
                    }
                    if(N - j-1 + killIndicator > min)   //오히려 죽어야 되는 개미의 수가 전보다 늘었다?? -> 최악효율 구간이군!
                        killIndicator = j;  //최악의 효율구간은 빼야지
                    break;
                }
            }
        }
        System.out.println(min);
    }
}
