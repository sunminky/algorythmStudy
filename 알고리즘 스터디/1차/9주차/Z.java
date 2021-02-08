package week9;

import java.util.Scanner;

public class Z {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int r = scanner.nextInt();
        int c = scanner.nextInt();
        new Z().solution(n,r,c);
    }
    public void solution(final int n,final int r,final int c){
        int row = r;
        int colum = c;
        int r_location = 0; //행의 좌표가 어느 구간에 속하는지
        int c_location = 0; //열의 좌표가 어느 구간에 속하는지
        int phase= (int)Math.pow(2,n-1);
        int boundary = phase;
        int result = 0;

        for(int i = 0;i < n;i++){
            //구간확인
            if(row >= boundary) //좌표가 기준점보다 위쪽, 3,4사분면에 속함
                r_location = 1;
            else
                r_location = 0;
            if(colum >= boundary)   //좌표가 기준점보다 오른쪽, 1,4사분면에 속함
                c_location = 1;
            else
                c_location = 0;

            row = row - boundary * r_location;  //좌표 축소
            colum = colum - boundary * c_location;  //좌표 축소
            result = result + boundary * boundary * (r_location * 2 + c_location);
            boundary = boundary / 2;    //기준점 이동
        }
        System.out.println(result);
    }
}
