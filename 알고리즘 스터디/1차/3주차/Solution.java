package com.company;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Solution {
    boolean[] node;

    public static void main(String[] args) {
        //int[][] arr = {{1,1,0},{1,1,0},{0,0,1}};
        int[][] arr = {{1,1,0},{1,1,1},{0,1,1}};
        int a = new Solution().solution(3,arr);
        System.out.print(a);
    }

    public int solution(int n, int[][] computers) {
        int answer = makeList(n,computers);
        return answer;
    }
    public int makeList(int n,int [][]computers){
        int cnt= 0;
        node = new boolean[n];
        for(int i = 0;i<n;i++){
            if(node[i] == false){
                //네트워크 구하는 로직
                //이웃 노드 찾기
                findNeigh(computers,i);
                cnt++;
            }
        }
        return cnt;
    }
    public void findNeigh(int [][]computers,int turn){
        for(int i = 0;i < computers[turn].length;i++){
            if(computers[turn][i] == 1 && node[i] == false){
                if(i == turn)
                    node[i] = true;
                else
                    findNeigh(computers,i);
            }
        }
    }
}
