package stack;

public class Top {
    public int[] solution(int[] heights) {
        int[] answer = new int[heights.length];

        answer[0] = 0;
        for(int i = 1;i<heights.length;i++){    //전체 탑에 대해서 수신가능 탑 조사
            for(int j=i-1;j >= 0;j--){  //왼쪽에서 오른쪽으로 이동
                if(heights[i] < heights[j]) {   //제일 먼저 발견하는 수신 탑
                    answer[i] = j + 1;
                    break;
                }
            }
        }
        return answer;
    }
}
