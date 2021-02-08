package week5;

public class IntegerTriangle {
    public static void main(String[] args) {
        int[][] parm = {{7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5}};
        int answer = new IntegerTriangle().solution(parm);
        System.out.println(answer);
    }

    public int solution(int[][] triangle) {
        int max[][] = new int[triangle.length][triangle[triangle.length-1].length];    //삼각형 맨 밑줄의 원소 개수와 같게
        int answer = 0;

        max[0][0] = triangle[0][0];
        for(int i = 0;i < triangle.length - 1;i++){
            for(int j = 0;j < triangle[i].length;j++){
                if(max[i][j] + triangle[i+1][j] > max[i+1][j])
                    max[i+1][j] = max[i][j] + triangle[i+1][j];
                if(max[i][j] + triangle[i+1][j+1] > max[i+1][j+1])
                    max[i+1][j+1] = max[i][j] + triangle[i+1][j+1];
            }
            //show(max[i]);
        }
        //show(max[triangle.length-1]);
        answer = findMax(max[triangle.length - 1]);
        return answer;
    }
    public int findMax(int[] elements){
        int max = 0;

        for(int i = 0;i < elements.length;i++){
            if(max < elements[i])
                max = elements[i];
        }
        return max;
    }
    public void show(int[] parm){
        for(int i = 0;i < parm.length;i++)
            System.out.print(parm[i] + " ");
        System.out.println();
    }
}
