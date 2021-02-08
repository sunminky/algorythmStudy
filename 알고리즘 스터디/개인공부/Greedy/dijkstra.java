package greedy;

import java.util.Random;
import java.util.Scanner;

public class dijkstra {
    public static void main(String[] argv){
        int nodenum,strtnode,endnode,pathnum;
        Scanner sc = new Scanner(System.in);
        System.out.print("노드개수를 입력하시오");
        nodenum = sc.nextInt();
        System.out.print("시작노드를 입력하시오");
        strtnode = sc.nextInt();
        System.out.print("종료노드를 입력하시오");
        endnode = sc.nextInt();
        System.out.print("경로개수를 입력하시오");
        pathnum = sc.nextInt();

        Graph graph = new Graph(nodenum,pathnum);
        graph.dijkstra(1);
    }
}

class Graph{
    private int n;           //노드들의 수
    private int p;             //경로의 수
    private int maps[][];    //노드들간의 가중치 저장할 변수
    Random rd = new Random();

    public Graph(int n,int pnum){    //노드의 개수 , 경로의 수
        this.n = n;
        this.p = pnum;
        maps = new int[n+1][n+1];
        input(p);

    }
    private void input(int pathnum){
        int temp1,temp2;
        for(int i=0;i<pathnum-1;i++){
            if(maps[rd.nextInt(n)+1][rd.nextInt(n)+1] != 0){    //이미 할당 되있으면
                Loop1 :
                for(int j=1;j<n+1;j++){   //빈자리 나오는 대로 대입
                    for(int k=1;k<n+1;k++){
                        if(j != k && maps[j][k] == 0) {   //j,k다르고 빈자리면
                            maps[j][k] = rd.nextInt(10) + 1;
                            maps[k][j] = maps[j][k];
                            break Loop1;
                        }
                    }
                }
            }
            maps[temp1 = rd.nextInt(n) + 1][temp2  = rd.nextInt(n) + 1] = rd.nextInt(10) + 1;
            maps[temp2][temp1] = maps[temp1][temp2];
        }
        if(maps[1][n] == 0){
            maps[1][n] = maps[n][1] = 10000;
        }
    }

    public void dijkstra(int v){                //v는 맨처음 노드 v = 1
        int distance[] = new int[n+1];          //최단 거리를 저장할 변수
        boolean[] check = new boolean[n+1];     //해당 노드를 방문했는지 체크할 변수
        int prevnode[] = new int[n+1];

        //distance값 초기화.
        for(int i=1;i<n+1;i++){
            distance[i] = Integer.MAX_VALUE;
        }

        //시작노드값 초기화.
        distance[v] =0;
        check[v] =true;

        //연결노드 distance갱신
        for(int i=1;i<n+1;i++){ //맨처음 노드랑 붙은애들 거리 갱식
            if(!check[i] && maps[v][i] !=0){
                distance[i] = maps[v][i];
                prevnode[i] = v;
            }
        }
        //맨처음노드와 붇은애들은 거리값 설정 완료
        //체크는 아직 안됨

        for(int a=0;a<n-1;a++){
            //원래는 모든 노드가 true될때까지 인데
            //노드가 n개 있을 때 다익스트라를 위해서 반복수는 n-1번이면 된다.
            //원하지 않으면 각각의 노드가 모두 true인지 확인하는 식으로 구현해도 된다.
            int min=Integer.MAX_VALUE;
            int min_index=-1;

            //최소값 찾기
            for(int i=1;i<n+1;i++){
                if(!check[i] && distance[i]!=Integer.MAX_VALUE){    //i가 체크안되고 거리값이 대입된것
                    if(distance[i]<min ){       //가장 가까운애 찾음
                        min=distance[i];
                        min_index = i;
                    }
                }
            }

            check[min_index] = true;    //가장가까운 노드 방문(체크)
            for(int i=1;i<n+1;i++){
                if(!check[i] && maps[min_index][i]!=0){ //체크 안되고 나와 붙어있는 노드
                    if(distance[i]>distance[min_index]+maps[min_index][i]){ //더 가까운 경로가 있다면 갱신
                        distance[i] = distance[min_index]+maps[min_index][i];
                        prevnode[i] = min_index;
                    }
                }
            }

        }

        System.out.println("최소경로 : "+distance[n]);
        System.out.print(n+"->");
        int temp = prevnode[n];
        while(true){    //최소경로 표시
            System.out.print(temp+"->");
            if(temp == 1)
                break;
            temp = prevnode[temp];
        }
    }
}
