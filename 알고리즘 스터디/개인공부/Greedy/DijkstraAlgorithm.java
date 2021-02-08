/*https://level.goorm.io/exam/43211/%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-dijkstra-s-algorithm/quiz/1*/
package greedy;

import java.util.HashMap;
import java.util.Iterator;
import java.util.PriorityQueue;
import java.util.Scanner;

public class DijkstraAlgorithm {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int pointnum = scanner.nextInt();
        int line = scanner.nextInt();
        int[] distanceList = new int[pointnum];
        int depart = 0;
        Point[] points = new Point[pointnum];
        PriorityQueue<PointSet> priorityQueue = new PriorityQueue<>();

        /*** 정보입력 단계 ***/
        for (int i = 0; i < pointnum; i++) {  //정점,거리 초기화
            points[i] = new Point();
            distanceList[i] = Integer.MAX_VALUE;
        }

        for (int i = 0; i < line; i++)  //정점의 정보 저장
            points[scanner.nextInt()].inject(scanner.nextInt(),scanner.nextInt());
        
        depart = scanner.nextInt();  //출발점 입력받음
        distanceList[depart-1] = 0;
        /*** ********** ***/

        priorityQueue.offer(new PointSet(depart-1,distanceList[depart-1],depart-1));
        while(priorityQueue.isEmpty() == false){
            dijkstra(priorityQueue.poll());
        }

    }
    static void dijkstra(PointSet point){

    }
    static class Point{
        private HashMap<Integer,Integer> neighbor;

        public Point(){
            this.neighbor = new HashMap<>();
        }
        public void inject(int neighbor,int distance){
            if(this.neighbor.containsKey(neighbor) == false)    //없으면 넣어주기
                this.neighbor.put(neighbor,distance);
            else{
                if(this.neighbor.get(neighbor) > distance)      //새로 입력받은 값이 더 작으면 갱신
                    this.neighbor.put(neighbor,distance);
            }
        }
        public Integer show(Integer key){
            return neighbor.get(key);
        }
        public Iterator<Integer> showNeighbor(){
            return neighbor.keySet().iterator();
        }
    }
    static class PointSet implements Comparable<PointSet>{
        private int index;
        private int distance;
        private int previous;

        public PointSet(int index,int distance,int previous){
            this.index = index;
            this.distance = distance;
            this.previous = previous;
        }

        @Override
        public int compareTo(PointSet o) {
            return Integer.max(distance,o.distance);
        }
    }
}
