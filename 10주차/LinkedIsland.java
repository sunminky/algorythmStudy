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
        int line_cnt = 0;
        int[][] newCosts = costs;
        boolean line_used[] = new boolean[newCosts.length];  //간선이 사용?
        boolean yn[] = new boolean[newCosts.length];         //yes no 저장
        boolean chained[] = new boolean[n];                 //연결이 된 노드
        LinkedList<Integer>[] nodelist = new LinkedList[n];           //연결된 노드 리스트

        for(int i = 0;i<nodelist.length;i++)
            nodelist[i] = new LinkedList<>();
        Arrays.sort(newCosts, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });
        yn[0] = true;
        for(int i = 0;i < newCosts.length;i++){
            if(chained[newCosts[i][0]] && chained[newCosts[i][1]])
                continue;
            if( yn[newCosts[i][0]] || yn[newCosts[i][1]])
                yn[newCosts[i][0]] = yn[newCosts[i][1]] = true;
            line_used[i] = chained[newCosts[i][0]] = chained[newCosts[i][1]] = true;
            answer += newCosts[i][2];
            line_cnt++;
        }
        while (line_cnt < n - 1){
            for(int i = 0;i < newCosts.length;i++){
                if(line_used[i])
                    continue;
                if(yn[newCosts[i][0]] == yn[newCosts[i][1]])
                    continue;
                line_used[i] = true;
                //연결된 정점 yes로 바꾸기
                answer += newCosts[i][2];
                line_cnt++;
            }
        }
        return answer;
    }
}
