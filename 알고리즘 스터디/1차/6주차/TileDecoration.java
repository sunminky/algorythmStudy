package week5;

public class TileDecoration {
    public long solution(int N) {
        long fibo[] = new long[80];
        fibo[0] = fibo[1] = 1;

        for(int i=2;i<=N;i++){
            fibo[i] = fibo[i-1] + fibo[i-2];
        }
        return (fibo[N-1]+fibo[N])*2;
    }
}
