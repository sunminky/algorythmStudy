package week4;

import java.util.Arrays;

class Thief {
    public static void main(String[] args) {
        System.out.println(new Thief().solution(new int[]{1, 5, 10, 1, 7, 9}));
    }

    public int solution(int[] money) {
        int[] accumulated_value = new int[money.length];
        int[] answer = {0, 0};

        /*1 ~ money.length-1 개까지 중 최대값 구하기*/
        accumulated_value[0] = 0;   //맨 앞에 있는 집은 안털거임
        accumulated_value[1] = money[1];
        accumulated_value[2] = money[2];

        for(int i=3;i < money.length;i++){
            accumulated_value[i] = Integer.max(accumulated_value[i-3], accumulated_value[i-2]) + money[i];
        }

        answer[0] = Integer.max(accumulated_value[money.length-1], accumulated_value[money.length-2]);  //1 ~ money.length-1 개까지 중 최대값
        
        /*0 ~ money.length-2 개까지 중 최대값 구하기*/
        accumulated_value[0] = money[0];    //맨 앞에있는 집을 털거임
        accumulated_value[2] = money[0] + money[2]; //맨 앞에있는 집을 털어서 2번째 집에서 얻을 수 있는 최대값도 바뀜

        for(int i=3;i < money.length;i++){
            accumulated_value[i] = Integer.max(accumulated_value[i-3], accumulated_value[i-2]) + money[i];
        }

        answer[1] = Integer.max(accumulated_value[money.length-2], accumulated_value[money.length-3]);  //0 ~ money.length-2 개까지 중 최대값

        Arrays.sort(answer);
        return answer[1];   //제일 큰 애가 제일 뒤에 있음
    }
}
