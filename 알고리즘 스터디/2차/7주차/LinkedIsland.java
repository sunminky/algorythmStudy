package week10;

import java.util.Arrays;
import java.util.Comparator;

public class LinkedIsland {
    public static void main(String[] args) {
        int arr[][] = {{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}};
        new LinkedIsland().solution(4,arr);
    }
    public int solution(final int n, final int[][] costs) {
        int answer = 0;
        int cnt = 0;
        int[][] newCosts = costs;
        int[] parent = new int[n];

        for(int i = 0;i < parent.length;i++)    //부모노드 자기자신으로 초기화
            parent[i] = i;

        Arrays.sort(newCosts, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[2] - o2[2];
            }
        });
        for(int i = 0;i < newCosts.length && cnt < n-1;i++){
            //사이클이 생기면(=속해있는 부모가 같으면) 무시
            if(compareParent(newCosts[i][0],newCosts[i][1],parent))
                continue;
            unionParent(newCosts[i][0],newCosts[i][1],parent);
            answer += newCosts[i][2];
            cnt++;
        }
        return answer;
    }
    public int getRootNode(final int node,final int[] parent){
        if(parent[node] == node)
            return node;
        else
            return parent[node] = getRootNode(parent[node],parent);
    }
    public boolean compareParent(int node1,int node2,int[] parent){
        if(getRootNode(node1,parent) == getRootNode(node2,parent))
            return true;
        return false;
    }
    public void  unionParent(int node1,int node2,int[] parent){
        int node1Root = getRootNode(node1,parent);
        int node2Root = getRootNode(node2,parent);

        if(node1Root > node2Root)
            parent[node1Root] = node2Root;
        else
            parent[node2Root] = node1Root;
    }
}
