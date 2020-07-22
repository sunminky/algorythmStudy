package goorm;

import java.util.Scanner;

public class FastAdd {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int upper = scanner.nextInt();  //1부터 upper 까지 입력받을 값
        System.out.println(addRecusively(upper));   //1~upper까지 더함
    }
    private static int addRecusively(int limit) {
        if(limit == 1)  //더하는 숫자들이 1~1 이면 종료
            return 1;

        int prev = addRecusively(limit/2);  //이전에 값을 계산
        int late = prev + limit/2 * Math.round((float)limit/2); //예를 들어 1~6까지 합 = (1+2+3) + (3+1 + 3+2 + 3+3)
        int result = late + prev;
        boolean isOdd = limit%2 == 1;   //만약 더해져야 할 숫자가 홀수개라면

        if(isOdd)
            result += Math.round((float)limit/2);   //정 가운데 수를 더해줌

        return result;
    }
}
