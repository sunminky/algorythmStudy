package dp;

class Solution {
    public int solution(int[] money) {
        int maxanswer = 0;
        int[] answer = {0,0};

        for(int i = 0;i < money.length;i++){
            answer[i%2] += money[i];
            if(answer[i%2] > answer[(i+1)%2])
                maxanswer = answer[i%2];
        }

        return maxanswer;
    }
}