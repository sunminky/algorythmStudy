package week11;

public class MockExam {
    public static void main(String[] args) {
        int[] data = {1,3,2,4,2};
        new MockExam().solution(data);
    }
    public int[] solution(int[] answers) {
        int[] answer = {};
        int highest = 0;        //최고 점수
        int topStudentNum = 1;  //최고득점자 수
        int student[][] = {{1,2,3,4,5},{2,1,2,3,2,4,2,5},{3,3,1,1,2,2,4,4,5,5}};    //학생들이 찍는 방식
        int accuracy[] = new int[3];    //학생별로 맞춘 문제 개수

        for(int i=0;i<answers.length;i++){  //첫번째 학생
            if(answers[i] == student[0][i%5])
                accuracy[0]++;
        }
        for(int i=0;i<answers.length;i++){  //두번째 학생
            if(answers[i] == student[1][i%8])
                accuracy[1]++;
        }
        for(int i=0;i<answers.length;i++){  //세번째 학생
            if(answers[i] == student[2][i%10])
                accuracy[2]++;
        }
        for(int i=0;i<accuracy.length;i++){ //최고 점수 맞은 사람 개수 세어보자
            if (accuracy[i] > highest) {    //최고 점수 갱신
                highest = accuracy[i];
                topStudentNum = 1;          //최고득점자 인원수 갱신
            }
            else if(accuracy[i] == highest){    //최고득점자랑 같은 점수 맞은 사람 몇명인지 세보자
                topStudentNum++;
            }
        }
        answer = new int[topStudentNum];
        topStudentNum = topStudentNum - 1;
        for(int i=accuracy.length-1;i>=0;i--){
            if(accuracy[i] == highest){
                answer[topStudentNum--] = i+1;
            }
        }
        /*for(int i=0;i<answer.length;i++){
            System.out.println(answer[i]);
        }*/
        return answer;
    }
}
