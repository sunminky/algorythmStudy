package dp;

class Solution {
    public int solution(int[] money) {
        int maxanswer = 0;
        int[] answer = {money[0],money[1]};

        for(int i = 2;i < money.length;i++){
            answer[i%2] += money[i];
            maxanswer = answer[i%2]= getMax(answer[i%2],answer[(i-1)%2]);
        }

        return maxanswer;
    }

    private int getMax(int x,int y){
        if(x > y)
            return x;
        return y;
    }
}