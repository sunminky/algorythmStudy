package ForCodingTest.stack;

import java.util.Stack;

public class Stack1 {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(89); //스택에 데이터 삽입
        System.out.println("가장 위에 있는 데이터 : "+stack.peek());
        stack.push(99);
        System.out.println("가장 위에 있는 데이터 : "+stack.peek());
        stack.push(4092);
        System.out.println("가장 위에 있는 데이터 : "+stack.peek());

        System.out.println("맨 처음에 넣은 데이터의 위치는? : "+stack.search(89));

        while (!stack.empty()){     //스택이 비어있지 않을때 까지
            System.out.println("가장 위에 있는 데이터 : "+stack.peek());
            stack.pop();//데이터 위에서부터 빼기
        }
    }
}
