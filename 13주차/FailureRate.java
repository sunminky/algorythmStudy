package week13;

import java.util.Arrays;
import java.util.Comparator;

public class FailureRate {
    public static void main(String[] args) {
        int[] arr = {4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,6,6,7};
        new FailureRate().solution(10,arr);
        //int[] arr2 = {2, 1, 2, 6, 2, 4, 3, 3};
        //new FailureRate().solution(5,arr2);
    }
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        double[][] rateArr = new double[N][2];
        int match = 0;
        int participant = stages.length;

        for(int i = 0;i<rateArr.length;i++){
            rateArr[i][0] = i+1;
        }
        for(int i = 1;i<=N;i++){
            match = 0;
            for(int j = 0;j < stages.length;j++){
                if(stages[j] == i) {  //현재 스테이지 못깬사람 찾기
                    match++;
                }
            }
            rateArr[i-1][1] = (double)match/participant;
            participant = participant - match;
            if(participant < 1)
                break;
        }
        Arrays.sort(rateArr, new Comparator<double[]>() {
            @Override
            public int compare(double[] o1, double[] o2) {
                if(o1[1] == o2[1])
                    return Integer.compare((int)o1[0],(int)o2[0]);
                return -Double.compare(o1[1],o2[1]);
            }
        });

        for(int i = 0;i<answer.length;i++){
            answer[i] = (int)rateArr[i][0];
        }
        return answer;
    }
}
