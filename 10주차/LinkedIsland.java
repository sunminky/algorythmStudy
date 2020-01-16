package week10;

import java.util.Arrays;
import java.util.Comparator;
import java.util.LinkedList;

public class LinkedIsland {
    public static void main(String[] args) {
        int arr[][] = {{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}};
        new LinkedIsland().solution(4,arr);
    }
    public int solution(final int n, final int[][] costs) {
        int answer = 0;
        int[][] newCosts = costs;
        int[] parent = new int[n];

        Arrays.sort(newCosts, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });

        for(int i = 0;i < newCosts.length;i++){
            //사이클이 생기면(=속해있는 부모가 같으면) 무시

        }
        return answer;
    }
}
