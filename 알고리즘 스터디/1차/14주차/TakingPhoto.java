package week14;

public class TakingPhoto {
    char[] members = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};  //멤버들 저장
    boolean[] used = new boolean[8];    //멤버들중 이미 줄에 서있는  사람있다면 true로 체크 (줄세우기 할때 사용)
    int cnt = 0;    //조건을 만족하면서 줄을 설 수 있는 경우
    Condition[] conditionList = null;   //조건들을 저장

    public static void main(String[] args) {
        String[] ddd = {"R~T>2","N~F=0"};//,"M~C<2", "C~M>1"};
        new TakingPhoto().solution(2,ddd);
    }

    public int solution(int n, String[] data) {
        StringBuilder target = new StringBuilder();
        parseCondition(data);   //조건들을 분석해서 저장
        makeCase(target);       //줄 세울수 있는 모든 경우 만들기
        return cnt;
    }
    public void parseCondition(String[] data){  //조건을 분석해서 조건 리스트에 저장
        Condition[] conditionList = new Condition[data.length]; //조건 리스트

        for(int i=0;i<data.length;i++){
            conditionList[i] = new Condition(data[i].charAt(0),data[i].charAt(2),data[i].charAt(4)-48,data[i].charAt(3));
            //멤버1, 멤버2, 멤버간의 간격, (이상,이하,같음)
        }

        this.conditionList = conditionList;
    }
    public void makeCase(StringBuilder target){ //줄 세울수 있는 모든 경우 만듬
        if(target.length() == members.length) { //모두가 줄에 서 있는 경우(문자열의 길이가 멤버의 전체 수와 같음) 종료
            if(satisfyCondition(target))    //조건에 일치하면 카운트 증가
                cnt++;
            return;
        }

        for(int i = 0;i<members.length;i++){    //줄 세울 수 있는 경우 만듬
            if(used[i] == false){   //아직 줄에 안선 멤버 찾음
                used[i] = true;     //줄에 세우는 과정1
                target.append(members[i]);  //줄에 세우는 과정2
                makeCase(target);   //다음에 줄 세울 사람 찾아가기
                target.deleteCharAt(target.length()-1); //원래 있던 사람 대신 다른 사람을 줄에 세움1
                used[i] = false;    //원래 있던 사람 대신 다른 사람을 줄에 세움1
            }
        }
    }
    public boolean satisfyCondition(StringBuilder target){  //줄이 조건에 맞는지 확인
        boolean ret = false;

        loop:
        for(int i = 0;i < conditionList.length;i++){
            switch (conditionList[i].getOption()){
                case '>':
                    if(Math.abs(findchar(target,conditionList[i].getMem1()) - findchar(target,conditionList[i].getMem2()))-1 > conditionList[i].getInterval()) {
                        ret = true;
                    }
                    else {
                        ret = false;
                        break loop;
                    }
                    break;
                case '<' :
                    if(Math.abs(Math.abs(findchar(target,conditionList[i].getMem1()) - findchar(target,conditionList[i].getMem2())))-1 < conditionList[i].getInterval())
                        ret = true;
                    else {
                        ret = false;
                        break loop;
                    }
                    break;
                case '=' :
                    if(Math.abs(Math.abs(findchar(target,conditionList[i].getMem1()) - findchar(target,conditionList[i].getMem2())))-1 == conditionList[i].getInterval())
                        ret = true;

                    else {
                        ret = false;
                        break loop;
                    }
                    break;
            }
        }
        return ret;
    }
    public int findchar(StringBuilder raw,char target){ //멤버가 줄의 몇번째에 서있는지 알려줌
        for(int i=0;i<raw.length();i++){
            if(raw.charAt(i) == target)
                return i;
        }
        return -1;
    }
    class Condition{    //조건을 저장하는 객체
        private char mem1;
        private char mem2;
        private int interval;
        private int option;
        public Condition(char mem1,char mem2,int interval,int option){
            this.mem1 = mem1;
            this.mem2 = mem2;
            this.interval = interval;
            this.option = option;
        }

        public char getMem1() {
            return mem1;
        }

        public char getMem2() {
            return mem2;
        }

        public int getInterval() {
            return interval;
        }

        public int getOption() {
            return option;
        }
    }
}
