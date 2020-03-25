/*https://programmers.co.kr/learn/courses/30/lessons/42578?language=java*/
package pregrammers;

public class Camouflage {
    public static void main(String[] args) {
        String arr[][] = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
        System.out.println(new Camouflage().solution(arr));
    }
    public int solution(final String[][] clothes) {
        int arr[] = new int[180];  //용량 30%이상 차면 해쉬충돌 확률 70%니까 3배 해줌

        for(int i=0;i<clothes.length;i++){
            arr[makeHash(clothes[i][1],180)]++;     //같은 의상종류였다면 의상개수 증가
        }
        return NumOfCases(arr);
    }
    public int makeHash(final String source,final int size){    //해쉬만드는 중
        int ret = 0;
        int digit = 1;
        for(int i=0;i<source.length();i++){     //라빈카프 알고리즘 읽어보삼
            ret = ret + source.charAt(i) * digit + source.charAt(i);    //문자열에 대한 해쉬값  계산
            digit = digit * 2;
        }
        return ret%size;    //배열의 크기만큼 나눠서 배열에 들어가게 만듬
    }
    public int NumOfCases(int arr[]){   //옷을 조합할 수 있는 경우의 수를 구함
        int ret = 1;
        for(int i=0;i<arr.length;i++){
            if(arr[i]>0){
                ret = ret * (arr[i]+1); //모든옷중 하나 고르는 개수 + 안고르는 경우의 수
            }
        }
        return ret-1;   //옷을 하나도 안입는 경우는 제외
    }
}
