package week4;

public class TheWayToSchool {
    boolean path[][];
    int count[][];

    public static void main(String[] args) {
        int arr[][] = {{2,2}};
        System.out.println(new TheWayToSchool().solution(4,3,arr));
    }

    public int solution(int m, int n, int[][] puddles) {
        path = new boolean[n+1][m+1];
        count = new int[n+1][m+1];

        for(int i=0;i<puddles.length;i++)
            path[puddles[i][1]][puddles[i][0]] = true;

        for(int i=1;i<=n;i++){  //세로 채우기
            if(path[i][1])  //물에 젖었으면 패스
                break;
            count[i][1] = 1;
        }

        for(int i=1;i<=m;i++){  //가로 채우기
            if(path[1][i])  //물에 젖었으면 패스
                break;
            count[1][i] = 1;
        }

        for(int i=2;i<=n;i++){
            for(int j=2;j<=m;j++){
                if(path[i][j])  //물에 젖었으면 패스
                    continue;
                count[i][j] = readPath(i,j);
            }
        }

        return count[n][m] % 1000000007;
    }
    /*
    오른쪽 m번 아래로 n번 가면 성공
     */
    public int readPath(int x,int y){
        return count[x-1][y] % 1000000007 + count[x][y-1] % 1000000007;
    }
}
