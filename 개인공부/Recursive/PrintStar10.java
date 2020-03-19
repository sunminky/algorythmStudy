/*https://www.acmicpc.net/problem/2447*//*재귀로 푸는 문제*/
package BeakJoon;

import java.util.Scanner;

public class PrintStar10 {
    public static char arr[][];
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        arr = new char[n][n];   //' '로 다 초기화 ㄱㄱ
        PrintStar10 temp = new PrintStar10();
        temp.init(n);
        temp.printArr();
    }
    public void init(int n){
        //char 배열 초기화하기
        for(int i=0;i<arr.length;i++){  //세로 출력
            for(int j=0;j<arr[i].length;j++){   //가로 출력
                arr[i][j] = 32;
            }
        }

        if(n == 3)
            recursive(3,0,0);
        else{
            for(int i=0;i<3;i++){   //세로 3번 반복
                for(int j=0;j<3;j++){   //가로 3번 반복
                    if((i == 1) && (j == 1))     //가운데 아니면 탐색계속
                        continue;
                    recursive(n/3,j*n/3,i*n/3);
                }
            }
        }
    }
    public void recursive(int n,int x,int y){   //3 x 3 행렬로 보기
        if(n == 3){
            //행렬 초기화
            for(int i=0;i<3;i++){   //세로 3번 반복
                for(int j=0;j<3;j++){   //가로 3번 반복
                    if((i == 1) && (j == 1))     //가운데 아니면 탐색계속
                        continue;
                    arr[x+j][y+i] = '*';
                }
            }
        }
        else {
            for(int i=0;i<3;i++){   //가로 3번 반복
                for(int j=0;j<3;j++){   //세로 3번 반복
                    if((i == 1) && (j == 1))     //가운데 아니면 탐색계속
                        continue;
                    recursive(n/3,x+j*n/3,y+i*n/3);
                }
            }
        }
    }
    public void printArr(){
        StringBuilder stringBuilder = new StringBuilder();
        for(int i=0;i<arr.length;i++){  //세로 출력
            for(int j=0;j<arr[i].length;j++){   //가로 출력
                stringBuilder.append(arr[i][j]);
            }
            stringBuilder.append('\n');
        }
        System.out.println(stringBuilder);
    }
}
