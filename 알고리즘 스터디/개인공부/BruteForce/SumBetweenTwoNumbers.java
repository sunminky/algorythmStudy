/*https://programmers.co.kr/learn/courses/30/lessons/12912*/
package BruteForce;

public class SumBetweenTwoNumbers {
    public static void main(String[] args) {
        System.out.println(new SumBetweenTwoNumbers().solution(3,5));
    }
    public long solution(final int a, final int b) {
        int start = 0;
        int end = 0;
        long answer = 0;

        /** a 와 b의 대소관계를 정해준다 **/
        if(a >= b){
            start = b;
            end = a;
        }
        else{
            start = a;
            end = b;
        }
        /**********************************/

        answer = start; //일단 맨 처음꺼는 무조건 한번 더해져야함(두 수가 같은경우에도 맨 처음꺼는 한번은 나와야 하니까)

        for(int i=start+1;i<=end;i++){  //두 정수 사이의 있는 값을 다 더한다
            answer += i;
        }
        return answer;
    }
}
