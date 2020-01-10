package week9;

import java.util.Scanner;

public class TowerOfHanoi {
    public static void main(String[] args) {
        int towerHeight = new Scanner(System.in).nextInt();
        TowerOfHanoi towerOfHanoi = new TowerOfHanoi();
        towerOfHanoi.moveCount(towerHeight);
        towerOfHanoi.move(1,3,towerHeight);
    }
    public void move(int start,int end,int phase){
        if(phase == 1) {  //1 하나만 옮기면 되는 상황
            System.out.println(start + " " + end);
        }
        else{
            int 선택안된친구 = notSelected(start,end);
            move(start,선택안된친구,phase-1);
            move(start,end,1);
            move(선택안된친구,end,phase-1);
        }
    }
    public int notSelected(int p1,int p2){  //1,2,3 중 p1,p2가 아닌 것은?
        boolean[] lst = new boolean[3];
        int result = -1;

        lst[p1-1] = true;
        lst[p2-1] = true;
        for(int i = 0;i < lst.length;i++)
            if(lst[i] == false){
                result = i+1;
                break;
            }
        return result;
    }
    public void moveCount(int height){
        int result = (int)Math.pow(2,height) - 1;
        System.out.println(result);
    }
}
