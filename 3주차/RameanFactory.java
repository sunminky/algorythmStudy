package com.company;

import java.util.Collections;
import java.util.PriorityQueue;

public class RameanFactory {
    public static void main(String[] args) {
        int arr[] = {4,10,15};
        int arr2[] = {20,5,10};
        int x = new RameanFactory().solution(4,arr,arr2,30);
        System.out.print(x);
    }
    public int solution(int stock, int[] dates, int[] supplies, int k) {
        int answer = 0;
        int startIndex = 0;
        int latestIndex = 0;
        int curStock = stock;
        PriorityQueue <Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());
        /***일 시작***/
        while(curStock < k){  //k일까지 버틸만큼 수량 모으면 종료
            for(int i = startIndex ; i < dates.length;i++){
                if(dates[i] <= curStock){ //현재 날짜보다 이전이면 추가
                    priorityQueue.offer(supplies[i]);
                    System.out.println("supplies : "+supplies[i]);
                    latestIndex = i; //여태까지 추가한 인덱스
                }
                else
                    break;
            }
            startIndex = latestIndex+1;   //다음부터 추가할 인덱스

            while(priorityQueue.isEmpty() == false)
                curStock += priorityQueue.poll().intValue();

            System.out.println("value : "+curStock);
            answer++;
        }
        /**일 끝**/
        return answer;
    }
}
