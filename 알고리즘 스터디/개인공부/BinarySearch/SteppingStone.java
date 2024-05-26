/* https://school.programmers.co.kr/learn/courses/30/lessons/43236 */

import java.util.Arrays;

public class SteppingStone {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        int start = 1;
        int end = 1000000000;
        Arrays.sort(rocks);

        while (start < end) {
            int middle = (start + end) / 2;
            int prev = 0;
            int remain = n;

            for(int i = 0;i < rocks.length; i++){
                if(rocks[i] - prev < middle){
                    remain--;
                    continue;
                }

                prev = rocks[i];
            }

            // 제일 마지막 돌
            if(distance - prev < middle)
                remain--;   // 제일 마지막 돌 바로 앞에 있는 돌 제거

            if(remain >= 0) {
                start = middle + 1;
                answer = middle > answer?middle:answer;
            }
            else
                end = middle;

        }

        return answer;
    }

    public static void main(String[] args) {
        new SteppingStone().solution(25, new int[]{2, 14, 11, 21, 17}, 2);   // 4
    }
}
