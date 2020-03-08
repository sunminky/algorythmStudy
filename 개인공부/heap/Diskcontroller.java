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
        Arrays.sort(jobs, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0],o2[0]);
            }
        });

        while(used < jobs.length){
            for(int i=past;i<jobs.length;i++){  //현재 시간보다 이전에 온것들 추가
                if(jobs[i][0] <= present) {
                    priorityQueue.offer(new node(jobs[i][0], jobs[i][1]));
                    past++;
                }
            }
            if(priorityQueue.isEmpty()){    //할 수 있는 작업이 하나도 없음
                present++;
            }
            else{
                node tmp = priorityQueue.poll();
                present += tmp.spend;
                answer += present - tmp.arrive;
                used++;
            }
        }
        return answer/jobs.length;
    }
    class node implements Comparable<node>{
        int arrive;
        int spend;
        public node(int arrive,int spend){
            this.arrive = arrive;
            this.spend = spend;
        }
        @Override
        public int compareTo(node o) {
            if(this.spend > o.spend)
                return 1;
            return -1;
        }
    }
}
