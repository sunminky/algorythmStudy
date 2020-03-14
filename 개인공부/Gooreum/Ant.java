package Gooreum;

import java.util.Arrays;
import java.util.Scanner;

public class Ant {
    public static void main(String[] args) throws Exception {
        Scanner scan = new Scanner(System.in);
        int N = scan.nextInt(); //전체 개미수
        int d = scan.nextInt(); //줄이고 싶은 반지름 수
        int ant[] = new int[N];     //개미들 위치 저장
        int min = Integer.MAX_VALUE;    //최소로 죽여야 하는 개미

        for(int i=0;i<N;i++){
            ant[i] = scan.nextInt();    //개미 입력 받음
        }
        Arrays.sort(ant);
        for(int i=0;i<N;i++){   //왼쪽에 있는 게미부터 죽이기
            if(i>=min) {
                break;
            }
            for(int j = 0;j<N-i;j++){   //오른쪽에 있는 개미부터 죽이기
                if(ant[N-1-j] - ant[i] <= d){
                    if(i+j<min) {
                        min = i + j;
                    }
                    break;
                }
            }
        }
        System.out.println(min);
    }
}
