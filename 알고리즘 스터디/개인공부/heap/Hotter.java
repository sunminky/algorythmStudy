import java.util.*;

public class Hotter {
    class Food {
        public int scoville;

        public Food(int scoville) {
            this.scoville = scoville;
        }
    }

    class FoodComparator implements Comparator<Food> {
        @Override
        public int compare(Food o1, Food o2) {
            return o1.scoville - o2.scoville;
        }
    }

    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Food> pq = new PriorityQueue<>(new FoodComparator());

        for (int tmp : scoville) {
            pq.offer(new Food(tmp));
        }

        while (pq.peek().scoville < K && pq.size() >= 2) {
            pq.offer(new Food(pq.poll().scoville + (pq.poll().scoville * 2)));
            answer++;
        }

        return pq.peek().scoville >= K ? answer : -1;
    }

    public static void main(String[] args) {
        System.out.println(new Hotter().solution(new int[]{1, 2, 3, 9, 10, 12}, 7));   // 2
    }
}
