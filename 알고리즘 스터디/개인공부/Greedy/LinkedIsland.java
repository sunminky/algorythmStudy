/* https://school.programmers.co.kr/learn/courses/30/lessons/42861 */

import java.util.Arrays;
import java.util.Comparator;

public class LinkedIsland {
    class Island {
        int cost, island1, island2;

        public Island(int island1, int island2, int cost) {
            this.cost = cost;
            this.island1 = island1;
            this.island2 = island2;
        }
    }

    public int solution(final int n, final int[][] costs) {
        int answer = 0;
        PriorityQueue<Island> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
        Map<Integer, LinkedList<Island>> path = new HashMap<>(n);
        boolean[] visited = new boolean[n];

        for (int[] cost : costs) {
            int[] _cost = cost;

            if (!path.containsKey(_cost[0]))
                path.put(new Integer(_cost[0]), new LinkedList<>());

            if (!path.containsKey(_cost[1]))
                path.put(new Integer(_cost[1]), new LinkedList<>());

            path.get(new Integer(_cost[0])).add(new Island(_cost[0], _cost[1], _cost[2]));
            path.get(new Integer(_cost[1])).add(new Island(_cost[1], _cost[0], _cost[2]));
        }

        pq.offer(new Island(0, 0, 0));

        Arrays.fill(visited, false);

        while (!pq.isEmpty()) {
            Island cur_i = pq.poll();

            if (visited[cur_i.island2])
                continue;

            visited[cur_i.island2] = true;
            answer += cur_i.cost;

            for (Island i : path.get(cur_i.island2)) {
                if (visited[i.island2])
                    continue;

                pq.offer(i);
            }
        }

        return answer;
    }

}
