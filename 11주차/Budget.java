package week11;

import java.util.Arrays;

public class Budget {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println(new Budget().solution(arr,30));
    }
    public int solution(int[] budgets, final int M) {
        int sum = M;
        int indicator = 0;
        int denominator = budgets.length;
        int quota = sum / denominator;    //몫
        int rest = sum % denominator;     //나머지
        Arrays.sort(budgets);

        if(budgets[0]>quota)   //예산이 쪼들림
            return quota;

        while (true){
            for (int i=indicator;i<budgets.length;i++){
                indicator = i;  //현재 몫으로 어디까지 만족시키는지
                if(budgets[i] <= quota)
                    rest = rest + quota - budgets[i];   //요구하는 예산이 몫보다 작으면 나머지에 더해줌
                else{
                    denominator = budgets.length - i;   //요구하는 예산이 몫보다 더 큰 사람들
                    break;
                }
            }
            if(indicator == budgets.length-1)   //예산이 충분함
                return budgets[budgets.length-1];
            if(rest / denominator == 0)     //더 이상 몫을 올릴수 없음
                break;
            quota += rest / denominator;    //요구하는 예산이 몫보다 작은 사람들 것을 나눠먹는다
            rest = rest % denominator;
        }
        return quota;
    }
}
