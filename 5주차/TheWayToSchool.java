package week4;

public class TheWayToSchool {
    public static void main(String[] args) {
        int arr[][] = {{2,2}};
        new TheWayToSchool().solution(4,3,arr);
    }

    public int solution(int m, int n, int[][] puddles) {
        int path[][] = new int[m][n];
        System.out.println("행 길이 : "+path.length+"열 길이 : "+path[0].length);

        for(int i = 0;i<puddles.length;i++)     //물에 젖은 부분 체크하기
           path[ puddles[i][0]-1 ][ puddles[i][1]-1 ] = 1;

        int answer = 0;
        answer += lookAt(path,1,0);   //가로 1칸
        answer += lookAt(path,0,1);   //세로 1칸
        System.out.println("경로수 : " + answer);
        return answer;
    }
    /*
    오른쪽 m반 아래로 n번 가면 성공
     */

    public int lookAt(int[][] path,int x,int y){
        System.out.printf("[%d][%d]\n",x,y);
        int cnt = 0;
        //물에 젖은 자리였던 경우
        if(path[x][y] == 1) {
            System.out.println("wet");
            return 0;
        }
        if(x < path.length-1)//가로로 움직이기
            cnt += lookAt(path,x+1,y);
        //세로로 움직이기
        if(y < path[0].length-1)
            cnt += lookAt(path,x,y+1);
        //도착지인 경우
        if(x == path.length-1 && y == path[0].length-1)
            System.out.println(cnt++);
        return cnt;
    }
}
