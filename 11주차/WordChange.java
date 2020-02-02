package week11;

public class WordChange {
    public static void main(String[] args) {
        String[] words = {"hot", "dot", "dog", "lot", "log", "cog","sot","cok","pot"};
        int ret = new WordChange().solution("hit","cog",words);
        System.out.println(ret);
    }
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        int cnt = 1;
        boolean isLeft = true;
        int depth[] = new int[words.length];
        boolean[][] neighbor = new boolean[words.length][words.length];
        boolean[] beginNeighbor = new boolean[words.length];

        for(int i=0;i<depth.length;i++){    //depth 행렬 초기화
            depth[i] = Integer.MAX_VALUE;
        }
        for(int i=0;i<words.length;i++){    //인접여부 행렬 만들기
            for(int j=0;j<words.length;j++){
                neighbor[i][j] = cmpWord(words[i],words[j]);
            }
        }
        for(int i=0;i<words.length;i++){    //begin과 인접한 행렬 만들기
            beginNeighbor[i] = cmpWord(begin,words[i]);
        }
        for(int i=0;i<beginNeighbor.length;i++){    //begin과 한 글자 차이나는 애들은 거리 1로 설정
            if(beginNeighbor[i])
                depth[i] = 1;
        }
        while (isLeft){
            isLeft = false;
            for(int i=0;i<neighbor.length;i++){
                if(depth[i] == cnt){
                    for(int j=0;j<neighbor[i].length;j++){
                        if(neighbor[i][j]){
                            if(depth[j] > depth[i]+1)
                                depth[j] = depth[i]+1;
                        }
                    }
                    isLeft = true;
                }
            }
            cnt++;
        }
        for(int i=0;i<words.length;i++){    //target과 같은 문자열의 깊이 찾기
            if(target.equals(words[i])){
                answer = depth[i];
                break;
            }
        }
        /*for(int i=0;i<words.length;i++){
            System.out.println("**********" + words[i] + "*****************");
            for(int j=0;j<words.length;j++){
                System.out.print(neighbor[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println("**********" + begin + "*****************");
        for(int i=0;i<words.length;i++){
            System.out.print(beginNeighbor[i] + " ");
        }
        for(int i=0;i<depth.length;i++){
            System.out.println("["+i+"]"+" "+depth[i]);
        }*/
        return answer;
    }
    public boolean cmpWord(String word,String Target){    //단어가 한글자 빼고 같은지 체크
        boolean ret = true;
        for(int i=0;i<word.length();i++){
            ret = true;
            for(int j=0;j<word.length();j++){
                if(j == i)
                    continue;
                if(word.charAt(j) != Target.charAt(j)){
                    ret = false;
                    break;
                }
            }
            if(ret)
                break;
        }
        return ret;
    }
}
