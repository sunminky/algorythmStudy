package week12;

public class Extract {
    public int solution(String s) {
        int answer = s.length();    //압축이 하나도 안됬을 경우가 초기값
        int result;                    //각 스텝마다 압축된 문자열의 길이 저장
        int cnt = 0;                //같은 단어가 몇번이나 반복되는지 세어봄
        char[] target = s.toCharArray();    //매개변수로 받은 String을 계산하기 좋게 char 배열로 바꿈

        for(int i=1;i<=s.length()/2;i++){   //몇글자씩 쪼개야 할지(1 ~ 전체문자열길이/2)
            char[] buf = new char[i];   //패턴을 저장하기위해 사용
            s.getChars(0,i,buf,0);  //buf를 맨처음 ~ i번째 까지의 문자열로 초기화
            cnt = 0;
            result = s.length();       //매 스텝마다 result는 최악의 경우(압축 하나도 안된경우)로 초기화
            for (int j=0;j<s.length()/i;j++){   //패턴 탐색
                for (int x=0;x<i;x++){  //패턴이 target과 완전히 같은지 확인
                    if(buf[x] != target[i * j + x]) {   //패턴과 다른 경우
                        if(cnt/i != 1){ //패턴이 자기자신과만 같은경우가 아니면
                            result = result - (cnt/i * i) + ((int)Math.log10(cnt/i) + 1 + i); //전제 길이에서 패턴이 반복된 횟수 * 패턴의 길이 만큼 빼고 반복된횟수의 자리수와 패턴 길이만큼 더해줌
                        }
                        s.getChars(i*j,i*(j+1),buf,0);      //이전의 문자열 새롭게 갱신
                        cnt = i;
                        break;
                    }
                    cnt++;
                }
            }
            if(cnt/i != 1){ //문자열의 끝까지 왔고 마지막 패턴이 자기자신과만 같은경우가 아니면
                result = result - (cnt/i * i) + ((int)Math.log10(cnt/i) + 1 + i);
            }
            answer = Math.min(answer,result);  //여태까지 나온 결과중 최소인것을 저장
        }
        return answer;
    }
}
