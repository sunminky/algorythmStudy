/*https://www.acmicpc.net/problem/3033*/
package hash;

import java.util.Scanner;

public class LongestString {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        new LongestString().longest(Integer.parseInt(scanner.nextLine()),scanner.nextLine());
    }
    public int longest(int len,String source){
        int ret = 0;
        int dp[][] = new int[2][len];

        if(len == 1)
            return ret;

        for(int i=0;i<len;i++){     //첫째줄 초기화
            if(source.charAt(0) == source.charAt(i)) {
                dp[0][i] = 1;
                ret = 1;
            }
        }

        for(int i=1;i<len/2;i++){   //둘째줄부터 계산
            for(int j=i+1;j<len;j++){
                if(source.charAt(i) == source.charAt(j)) {
                    dp[i%2][j] = dp[(i-1)%2][j-1] + 1;
                    if(dp[i%2][j] > ret)   //최대값 구하기
                        ret = dp[i % 2][j];
                }
                else
                    dp[i%2][j] = 0;
            }
        }

        System.out.println(ret);
        return ret;
    }
}
