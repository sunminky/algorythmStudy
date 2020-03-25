/*https://programmers.co.kr/learn/courses/30/lessons/42578?language=java*/
package pregrammers;

import java.util.Enumeration;
import java.util.Hashtable;

public class Camouflage2 {
    public static void main(String[] args) {
        String arr[][] = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        System.out.println(new Camouflage().solution(arr));
    }
    public int solution(final String[][] clothes) {
        Hashtable<String,Integer> hashtable = new Hashtable<>();    //의상의 종류와 수량을 저장할 해쉬맵 생성

        for(int i=0;i<clothes.length;i++){
            if(hashtable.get(clothes[i][1]) == null)    //해쉬테이블에 의상 종류가 없는 경우
                hashtable.put(clothes[i][1],1);
            else
                hashtable.put(clothes[i][1], hashtable.get(clothes[i][1])+1);   //이전에 해쉬테이블에 같은 의상종류가 있는 경우
        }
        return NumOfCases(hashtable);
    }
    public int NumOfCases(final Hashtable hashtable) {  //옷 조합 가지수 구하기
        int ret = 1;
        Enumeration en = hashtable.keys();

        while(en.hasMoreElements()){
            ret = ret * ((Integer) hashtable.get(en.nextElement().toString()) + 1); //입을수 있는 옷의 가지수 + 안입는 경우
        }
        return ret-1;   //하나도 안 입는 경우는 제외
    }
}

