package PersonnelStudy.week7;

public class MakeBiggest {
    public String solution(String number, int k) {
        int targetLen = number.length() - k;
        StringBuilder answer = new StringBuilder(number.substring(0,targetLen));
        int count = k;

        for(int i=targetLen;i<number.length();i++){
            for(int j=0;j<targetLen-1;j++){
                if(answer.charAt(j) < answer.charAt(j+1)){
                    answer.deleteCharAt(j);
                    answer.append(number.charAt(i));
                    count--;
                    if(count == 0)
                        return answer.toString();
                    break;
                }
            }
            if(answer.charAt(answer.length()-1) < number.charAt(i))
                answer.setCharAt(answer.length()-1, number.charAt(i));
        }

        return answer.toString();
    }

    public static void main(String[] args) {
        String result = new MakeBiggest().solution("1924", 2);
        System.out.println(result);

        result = new MakeBiggest().solution("4177252841", 4);
        System.out.println(result);
    }
}
