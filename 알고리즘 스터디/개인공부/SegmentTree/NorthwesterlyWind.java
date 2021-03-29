// https://www.acmicpc.net/problem/5419
// 스위핑, 세그먼트 트리, 좌표압축


import java.io.*;
import java.util.*;

public class Main {
    static class Point {
        int x, y;
        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int[] tree;

    static long query(int node, int start, int end, int left, int right) {
        if (right < start || left > end) { return 0; }
        if (left <= start && end <= right) {
            return tree[node];
        }
        int m = (start + end) >> 1;
        return query(node << 1, start, m, left, right) + query(node << 1 | 1, m + 1, end, left, right);
    }

    static int update(int node, int start, int end, int idx) {
        if (idx < start || idx > end) { return tree[node]; }
        if (start == end) {
            return tree[node] += 1;
        }
        int m = (start + end) >> 1;
        return tree[node] = update(node << 1, start, m, idx) + update(node << 1 | 1, m + 1, end, idx);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        List<Point> list = new ArrayList<>();
        for (int tc = 1; tc <= T; tc++) {
            int n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                list.add(new Point(x, y));
            }

            // 북쪽에 있는 y좌표부터 낮은 수를 부여함(좌표 압축)
            list.sort((o1, o2) -> Integer.compare(o2.y, o1.y));
            int size = 0;
            int prev = Integer.MIN_VALUE;
            for (int i = 0; i < list.size(); i++) {
                Point p = list.get(i);
                if (prev == p.y) {
                    list.set(i, new Point(p.x, size));
                    continue;
                }
                prev = p.y;
                p.y = ++size;
                list.set(i, p);
            }

            list.sort((o1, o2) -> {
                if (o1.x == o2.x) { return Integer.compare(o1.y, o2.y); }
                return Integer.compare(o1.x, o2.x);
            }); // x좌표 순으로 정렬(쿼리용), x좌표가 같으면 북쪽에 있는 섬먼저.

            int h = (int) Math.ceil(Math.log(size) / Math.log(2));
            tree = new int[1 << h + 1];
            long answer = 0;
            for (int i = 0; i < list.size(); i++) {
                System.out.println(list.get(i).x + " " + list.get(i).y);
                int val = list.get(i).y;
                answer += query(1, 1, size, 1, val);
                update(1, 1, size, val);
            }
            sb.append(answer).append('\n');
            list.clear();
        }
        System.out.print(sb);
    }
}

