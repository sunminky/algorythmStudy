/*https://www.acmicpc.net/problem/2042*/
package HomeWork;

import java.util.Scanner;

public class PortionAdd {
    long[] tree = null;

    public static void main(String[] args) {
        new PortionAdd().solution();
    }

    private void solution(){
        Scanner scanner = new Scanner(System.in);
        int indice = scanner.nextInt(); //원소들의 개수
        int tries = scanner.nextInt() + scanner.nextInt();  //조회횟수 + 수정횟수
        long[] elements = new long[indice+1];   //원소들 저장
        tree =new long[indice+1];   //펜윅트리

        /*트리 초기화*/
        for(int i=0;i<indice;i++){
            long newValue = scanner.nextLong(); 
            update(i+1, newValue);
            elements[i+1] = newValue;
        }

        for(int i=0;i<tries;i++) {
            int action = scanner.nextInt();
            int b = scanner.nextInt();
            long c = scanner.nextLong();

            switch (action) {
                case 1: //숫자 바꾸기
                    long margin = c - elements[b];  //원래 값과 새 값의 차이
                    elements[b] = c;
                    update(b, margin);
                    break;
                case 2: //부분 합 구하기
                    System.out.println(sum((int)c) - sum(b-1));
                    break;
            }

        }
    }

    private void update(int idx, long newValue){
        int grpBit = idx;
        while (grpBit < tree.length - 1){
            tree[grpBit] += newValue;
            grpBit += grpBit & (-grpBit);
        }
        //전체 합에 대해서 업데이트
        tree[tree.length - 1] += newValue;
    }

    private long sum(int idx){
        int grpBit = idx;
        long ret = 0;

        if(idx == tree.length-1)    //조회하려는 범위가 전체합인 경우
            return tree[tree.length-1];

        while (grpBit > 0){
            ret += tree[grpBit];
            grpBit -= grpBit & (-grpBit);
        }
        return ret;
    }
}
