package week10;

import java.util.Arrays;

public class Lifeboat {
    public static void main(String[] args) {
        int[] arr = {70,50,80,50};
        new Lifeboat().solution(arr,100);
    }
    public int solution(final int[] people, final int limit) {
        int answer = 0;
        int idx = 0;    //정렬 했을때 앞에 있는 사람 어디까지 태웟나 표시
        int[] newPeople = people;
        Arrays.sort(newPeople);

        for(int i = newPeople.length - 1;i >= idx;i--){
            if(newPeople[i] + newPeople[idx] <= limit)
                idx++;
            answer++;
        }
        System.out.println(answer);
        return answer;
    }
}
