package week11;

import java.util.Arrays;

public class Budget {
    public static void main(String[] args) {
        int[] arr = {120,150,140,110,130,125,122,129};
        Arrays.sort(arr);
        System.out.println(arr[new Budget().binSearch(arr,0,110)]);
    }
    public int solution(int[] budgets, final int M) {
        int answer = 0;
        int satisfied = 0;
        Arrays.sort(budgets);
        return answer;
    }
    public int binSearch(int[] budgets,int satisfied,int data){
        int len = budgets.length - 1;
        int index = (len + satisfied) / 2;
        while (true){
            if(budgets[index] <= data && budgets[index+1] > data)
                break;
            //오른쪽 == 왼쪽
            if(index == satisfied)  //더 작은 숫자 없음
                return -1;
            if(budgets[index] > data) { //더 작아
                len = index;
                index = (satisfied + index) / 2;
            }
            else {  //더 커
                satisfied = index + 1;
                index = index + (len - satisfied) / 2;
            }
            if(index == len - 1)    //더 큰 숫자 없음
                return -2;

        }
        return index;
    }
}
