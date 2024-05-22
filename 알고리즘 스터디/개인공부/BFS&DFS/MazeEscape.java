import java.util.*;

public class MazeEscape {
    public int find(int[] start, int[] end, String[] maps) {
        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[maps.length][];
        final int[][] movement = {{0, 1}, {-1, 0}, {1, 0}, {0, -1}};

        for (int i = 0; i < maps.length; i++) {
            visited[i] = new boolean[maps[i].length()];
            Arrays.fill(visited[i], false);
        }

        queue.offer(new int[]{start[0], start[1], 0});
        visited[start[1]][start[0]] = true;

        while (!queue.isEmpty()) {
            int[] cur_loc = queue.poll();

            if (cur_loc[0] == end[0]) {
                if (cur_loc[1] == end[1]) {
                    return cur_loc[2];
                }
            }

            for (int i = 0; i < movement.length; i++) {
                int new_x = cur_loc[0] + movement[i][0];
                int new_y = cur_loc[1] + movement[i][1];

                // 바운더리 체크
                if (0 > new_y || maps.length <= new_y)
                    continue;

                if (0 > new_x || maps[new_y].length() <= new_x)
                    continue;

                // 방문여부 체크
                if (visited[new_y][new_x])
                    continue;

                // 벽인지 길인지 체크
                if (maps[new_y].charAt(new_x) == 'X')
                    continue;

                visited[new_y][new_x] = true;
                queue.offer(new int[]{new_x, new_y, cur_loc[2] + 1});
            }
        }

        return -1;
    }

    public int[][] getPosition(String[] maps) {
        int[][] result = new int[3][2];

        for (int row = 0; row < maps.length; row++) {
            for (int col = 0; col < maps[row].length(); col++) {
                if (maps[row].charAt(col) == 'S')
                    result[0] = new int[]{col, row};

                if (maps[row].charAt(col) == 'L')
                    result[1] = new int[]{col, row};

                if (maps[row].charAt(col) == 'E')
                    result[2] = new int[]{col, row};
            }
        }

        return result;
    }

    public int solution(String[] maps) {
        int answer = 0, result = 0;
        int[][] position = getPosition(maps); // S, L, E

        System.out.printf("[%d %d] [%d %d] [%d %d]\n", position[0][0], position[0][1], position[1][0], position[1][1], position[2][0], position[2][1]);

        // s -> l
        result = find(position[0], position[1], maps);

        if (result == -1)
            return -1;

        answer += result;

        // l -> e
        result = find(position[1], position[2], maps);

        if (result == -1)
            return -1;

        answer += result;

        return answer;
    }

    public static void main(String[] args) {
        System.out.println(new MazeEscape().solution(new String[]{"SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"}));
        System.out.println(new MazeEscape().solution(new String[]{"LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"}));
    }
}
