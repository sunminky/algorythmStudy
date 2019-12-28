package week5;

public class TileDecoration {
    public long solution(int N) {
        long answer = 0;
        answer = getSuround(N);
        return answer;
    }
    public int getSuround(int N) {
        int tmp = 0;
        int[] prev = {1,1};
        int area = 6;

        if(N == 1)
            return 4;
        if(N == 2)
            return 6;

        for(int i = 2;i < N;i++){
            tmp = prev[0] + prev[1];
            area =  area + tmp * 2;
            prev[0] = prev[1];
            prev[1] = tmp;
        }

        return area;
    }
}
