package week14;

public class DartGame {
    public static void main(String[] args) {
        new DartGame().solution("1S2D*3T");
        new DartGame().solution("1D2S#10S");
        new DartGame().solution("1D2S0T");
        new DartGame().solution("1S*2T*3S");
        new DartGame().solution("1D#2S*3S");
        new DartGame().solution("1T2D3D#");
        new DartGame().solution("1D2S3T*");
    }
    public int solution(String dartResult) {
        int result = 0;
        AnswerPack answer = new AnswerPack(dartResult);

        for(int i = 0;i<3;i++){ //다트를 총 세번 던지니까 3개의 점수표현이 존재
            cutScore(answer,i); //몇점을 맞췄는지 알아내기
            bonus(answer,i);    //싱글, 더블, 트리플인지 구분
            option(answer,i);   //#, * 아니면 없는지 구분
        }
        for(int i = 0;i<3;i++)  //전체 점수를 구하는 과정
            result = result + answer.getDivision(i);
        return result;
    }
    public void cutScore(AnswerPack answerPack,int seq){
        char[] source = answerPack.getDartResult();
        int index = answerPack.getIndex();

        if(source[index] == '1') {  //1로 시작하는 숫자인 경우
            if (source[index+1] == '0'){  //10점 맞췄을 경우
                answerPack.setDivision(seq,10);
                index = index + 2;  //10은 두글자니까 두 글자 읽었다고 표시해야함
            }
            else{   //1점인 경우
                answerPack.setDivision(seq,source[index] - 48);
                index = index + 1;  //일반적인 경우에는 한글자 문자니까 한글자만 읽었다고 표시
            }
        }
        else{   //1로 시작하는 숫자가 아닌 경우
            answerPack.setDivision(seq,source[index] - 48);
            index = index + 1;  //일반적인 경우에는 한글자 문자니까 한글자만 읽었다고 표시
        }
        answerPack.setIndex(index); //인덱스 최신화
    }
    public void bonus(AnswerPack answerPack,int seq){
        char[] source = answerPack.getDartResult();
        int index = answerPack.getIndex();

        switch (source[index]){
            case 's':
            case 'S':
                //1제곱은 하나마나니까 아무것도 안할거임
                break;
            case 'd':
            case 'D':
                answerPack.setDivision(seq,answerPack.getDivision(seq)*answerPack.getDivision(seq));
                break;
            case 't':
            case 'T':
                answerPack.setDivision(seq,answerPack.getDivision(seq)*answerPack.getDivision(seq)*answerPack.getDivision(seq));
                break;
        }
        index = index + 1;
        answerPack.setIndex(index); //인덱스 최신화
    }
    public void option(AnswerPack answerPack,int seq){
        char[] source = answerPack.getDartResult();
        int index = answerPack.getIndex();

        if(source.length == index)  //3번째 다트점수에서 옵션이 없는 경우
            return;
        if(source[index] == '*'){
            if(seq != 0)
                answerPack.setDivision(seq - 1,answerPack.getDivision(seq - 1) * 2);    //이전꺼 2배
            answerPack.setDivision(seq,answerPack.getDivision(seq) * 2);    //현재꺼 2배
            index = index + 1;
            answerPack.setIndex(index); //인덱스 최신화
        }
        else if(source[index] == '#'){
            answerPack.setDivision(seq,answerPack.getDivision(seq) * -1);   //현재꺼 음수화
            index = index + 1;
            answerPack.setIndex(index); //인덱스 최신화
        }
    }
    class AnswerPack{
        private int division[]; //n번째 다트로 얻은 점수는 몇점인가
        private int index;      //문자열의 어디까지 읽었는가
        private char[] dartResult;  //String을 char로 저장

        public AnswerPack(String dartResult){
            this.division = new int[3];
            this.index = 0;
            this.dartResult = dartResult.toCharArray();
        }

        public int getDivision(int index) {
            return division[index];
        }

        public void setDivision(int index,int value) {
            this.division[index] = value;
        }

        public int getIndex() {
            return index;
        }

        public void setIndex(int index) {
            this.index = index;
        }

        public char[] getDartResult() {
            return dartResult;
        }
    }
}
