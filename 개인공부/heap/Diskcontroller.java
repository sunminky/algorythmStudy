package heap;

import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Diskcontroller {
    public int solution(int[][] jobs) {
        int present = 0;
        int answer = 0;
        int past = 0;
        int used = 0;
        PriorityQueue<node> priorityQueue = new PriorityQueue<>();
        Arrays.sort(jobs, new Comparator<int[]>() { //배열을 도착시간에 대해 오름차순으로 정렬
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0],o2[0]);
            }
        });

        while(used < jobs.length){  //모든 작업들을 다 실행할때 까지 반복
            for(int i=past;i<jobs.length;i++){  //현재 시간보다 이전에 온것들 추가
                if(jobs[i][0] <= present) {
                    priorityQueue.offer(new node(jobs[i][0], jobs[i][1]));
                    past++;
                }
            }
            if(priorityQueue.isEmpty()){    //할 수 있는 작업이 없음(아직 작업이 도착하지 않은 상태)
                present++;  //시간이 흐르게 함
            }
            else{
                node tmp = priorityQueue.poll();    //현재 큐에 있는 작업들중 가장 작업시간이 짧은 것 꺼냄
                present += tmp.spend;   //현재 시간을 작업이 끝난 시점으로 바꿈
                answer += present - tmp.arrive; //이 작업이 대기한 시간을 더해줌
                used++;     //완료된 작업 카운트
            }
        }
        return answer/jobs.length;  //대기시간의 평균을 구함
    }
    class node implements Comparable<node>{
        int arrive; //도착시간
        int spend;  //작업에 걸리는 시간
        public node(int arrive,int spend){
            this.arrive = arrive;
            this.spend = spend;
        }
        @Override
        public int compareTo(node o) {  //작업시간이 짧을 수록 우선순위가 높게 함
            if(this.spend > o.spend)
                return 1;
            return -1;
        }
    }
}
