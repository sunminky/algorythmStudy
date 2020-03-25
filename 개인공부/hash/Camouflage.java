/*https://programmers.co.kr/learn/courses/30/lessons/42578?language=java*/
package pregrammers;

public class Camouflage {
    public static void main(String[] args) {
        String arr[][] = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        System.out.println(new Camouflage().solution(arr));
    }
    public int solution(final String[][] clothes) {
        int arr[] = new int[180];  //용량 30%이상 차면 해쉬충돌 확률 70%니까 3배 해줌
        int answer = 0;

        for(int i=0;i<clothes.length;i++){
            arr[makeHash(clothes[i][1],180)]++;
        }
        return NumOfCases(arr);
    }
    public int makeHash(final String source,final int size){    //해쉬만드는 중
        int ret = 0;
        int digit = 1;
        for(int i=0;i<source.length();i++){
            ret = ret + source.charAt(i) * digit + source.charAt(i);
            digit = digit * 2;
        }
        return ret%size;
    }
    public int NumOfCases(int arr[]){
        int ret = 1;
        for(int i=0;i<arr.length;i++){
            if(arr[i]>0){
                ret = ret * (arr[i]+1); //모든옷중 하나 고르는 개수 + 안고르는 경우의 수
            }
        }
        return ret-1;
    }
}
