package week12;

import java.util.Arrays;
import java.util.Comparator;

public class SongJustPlayed {
    public static void main(String[] args) {
        String[] arr = {"12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"};
        String[] arr2 = {"03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"};
        String[] arr3 = {"12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"};
        String[] arr4 = {"12:00,12:30,HELLO1,ABCDEF", "12:00,12:30,HELLO2,ABCDEF","12:00,12:30,HELLO3,ABCDEF", "12:00,12:30,HELLO4,ABCDEF","12:00,12:20,HELLO5,ABCDEF"};

        System.out.println(new SongJustPlayed().solution("ABCDEFG",arr));
        System.out.println(new SongJustPlayed().solution("CC#BCC#BCC#BCC#B",arr2));
        System.out.println(new SongJustPlayed().solution("ABC",arr3));
        System.out.println(new SongJustPlayed().solution("ABC",arr4));
    }
    public String solution(String m, String[] musicinfos){  //#붙은 것들은 단일문자로 치환
        String replace_m = m.replace("C#","S");
        replace_m = replace_m.replace("D#","U");
        replace_m = replace_m.replace("F#","N");
        replace_m = replace_m.replace("G#","M");
        replace_m = replace_m.replace("A#","I");
        String[] musicinfos_m = new String[musicinfos.length * 4];  // ,로 구분된 문자열들을 분리해서 배열에 넣음

        for(int i=0;i<musicinfos.length;i++){
            musicinfos_m[i*4+0] = musicinfos[i].split(",")[0];
            musicinfos_m[i*4+1] = musicinfos[i].split(",")[1];
            musicinfos_m[i*4+2] = musicinfos[i].split(",")[2];
            musicinfos_m[i*4+3] = musicinfos[i].split(",")[3];
        }
        for(int i=0;i<musicinfos_m.length/4;i++){
            musicinfos_m[i * 4 + 3] = musicinfos_m[i * 4 + 3].replace("C#","S");
            musicinfos_m[i * 4 + 3] = musicinfos_m[i * 4 + 3].replace("D#","U");
            musicinfos_m[i * 4 + 3] = musicinfos_m[i * 4 + 3].replace("F#","N");
            musicinfos_m[i * 4 + 3] = musicinfos_m[i * 4 + 3].replace("G#","M");
            musicinfos_m[i * 4 + 3] = musicinfos_m[i * 4 + 3].replace("A#","I");
        }
        return solution2(replace_m,musicinfos_m);
    }
    public String solution2(String m, String[] musicinfos) {
        String answer = "(None)";
        int[][] playTimeArr = new int[musicinfos.length/4][2];  //재생시간과 info배열 인덱스 저장

        for(int i=0;i<playTimeArr.length;i++){
            playTimeArr[i][0] = playTime(musicinfos[i*4+0],musicinfos[i*4+1]);  //재생시간 저장
            playTimeArr[i][1] = i;      //info 배열의 몇번째로 나왔는지 기록
        }
        Arrays.sort(playTimeArr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return -(o1[0] - o2[0]);
            }
        }); //음악재생시간에 따라 내림차순정렬

        loop:
        for(int i=0;i<playTimeArr.length;i++){  //재생시간이 긴 곡부터 멜로디 비교
            if(makeString(musicinfos[ playTimeArr[i][1]*4 + 3],playTimeArr[i][0]).contains(m)){ //멜로디가 같은경우
                if(i < playTimeArr.length - 1){     //뒤에 다른 원소들이 남았는가??
                    if(playTimeArr[i+1][0] < playTimeArr[i][0]){    //뒤에 있는 원소보다 큰가??(같은 노래길이를 가진 원소는 없는가??)
                        answer = musicinfos[ playTimeArr[i][1]*4 + 2];
                        break;
                    }
                    if(playTimeArr[i+1][0] == playTimeArr[i][0]){   //뒤에 있는 원소와 크기가 같은가??(같은 노래길이를 가진 원소는 있는가??)
                        answer = musicinfos[ playTimeArr[i][1]*4 + 2];
                        for(int j=i+1;j<playTimeArr.length;j++){
                            if(playTimeArr[j][0] != playTimeArr[j-1][0]) {  //다른 노래길이를 가진 원소 등장
                                break loop;
                            }
                            if(playTimeArr[j-1][1] > playTimeArr[j][1]) {    //인덱스가 더 작음(info배열에서 더 앞에 있음)
                                answer = musicinfos[playTimeArr[j][1] + 2];
                            }
                        }
                    }
                }
                else{   //뒤에 다른 원소들이 없음(원소의 끝임)
                    answer = musicinfos[ playTimeArr[i][1]*4 + 2];
                    break;
                }
            }
        }
        return answer;
    }
    public int playTime(String start,String end){   //재생시간 구해주는 함수
        int startHour = Integer.parseInt(start.split(":")[0]);
        int startMinute = Integer.parseInt(start.split(":")[1]);
        int endHour = Integer.parseInt(end.split(":")[0]);
        int endMinute = Integer.parseInt(end.split(":")[1]);

        return (endHour - startHour) * 60 + (endMinute - startMinute);
    }
    public String makeString(String material,int time){ //재생시간만큼 곡을 만들어주는 함수
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<time/material.length();i++){
            sb.append(material);
        }
        sb.append(material.substring(0,time%material.length()));
        return sb.toString();
    }
}
