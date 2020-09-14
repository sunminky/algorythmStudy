/*https://programmers.co.kr/learn/courses/30/lessons/1829#*/
package Studt.week10;


public class ColoringBook {
    long[][] map = null;

    public static void main(String[] args) {
        int[][] arr = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
        int[] result = new ColoringBook().solution(6,4, arr);
        System.out.println(result[0] + " / " + result[1]);

        int[][] arr2 = {{0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0}, {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}, {0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0}, {0, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0}, {0, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 0}, {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0}, {0, 1, 3, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 3, 1, 0}, {0, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 0}, {0, 0, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0}, {0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}, {0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0}};
        result = new ColoringBook().solution(13,16, arr2);
        System.out.println(result[0] + " / " + result[1]);
    }

    private int relationTracing(int x, int y, long color){  //영역의 넓이 반환
        int curArea = 0;

        /*
        통과조건 :
        0 <= x < n이고 0<= y < m 이고 color == map[y][x] 이고 color != 0
         */
        if (x < 0 || x >= map[0].length || y < 0 || y >= map.length || color != map[y][x] || color == 0)
            return curArea; //0반환

        ++curArea;
        map[y][x] = 0;  //이미 탐색한 지역은 0으로 세팅

        //오른쪽, 위쪽, 아래쪽, 왼쪽 탐색
        curArea += relationTracing(x+1, y, color);
        curArea += relationTracing(x, y+1, color);
        curArea += relationTracing(x, y-1, color);
        curArea += relationTracing(x-1, y, color);

        return curArea;
    }

    public int[] solution(int m, int n, final int[][] picture) {
        map = new long[m][n];
        int diversity = 0;  //영역의 개수
        int maxArea = 0;    //영역의 최대넓이

        //그림을 int형 -> long형으로 변환
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++)
                map[i][j] = picture[i][j];
        }

        for(int i=0;i<map.length;i++){
            for(int j=0;j<map[i].length;j++){
                //0이 아니면 같은 색깔의 영역 탐색
                if(map[i][j] != 0){
                    diversity++;
                    //영역 탐색
                    maxArea = Integer.max(maxArea, relationTracing(j, i, map[i][j]));
                }
            }
        }

        return new int[]{diversity, maxArea};
    }
}
