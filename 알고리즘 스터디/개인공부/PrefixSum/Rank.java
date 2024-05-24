/* https://school.programmers.co.kr/learn/courses/30/lessons/72412 */

import java.util.*;

public class Rank {
    public int[] solution(String[] info, String[] query) {
        List<Integer> answer = new ArrayList<>();
        int[][][][][] applicant = new int[4][3][3][3][100001];
        HashMap<String, int[]> lanMap = new HashMap<>(4);
        HashMap<String, int[]> posMap = new HashMap<>(3);
        HashMap<String, int[]> carMap = new HashMap<>(3);
        HashMap<String, int[]> fooMap = new HashMap<>(3);

        lanMap.put("cpp", new int[]{0});
        lanMap.put("java", new int[]{1});
        lanMap.put("python", new int[]{2});
        lanMap.put("-", new int[]{0, 1, 2});

        posMap.put("backend", new int[]{0});
        posMap.put("frontend", new int[]{1});
        posMap.put("-", new int[]{0, 1});

        carMap.put("junior", new int[]{0});
        carMap.put("senior", new int[]{1});
        carMap.put("-", new int[]{0, 1});

        fooMap.put("chicken", new int[]{0});
        fooMap.put("pizza", new int[]{1});
        fooMap.put("-", new int[]{0, 1});

        for (int i1 = 0; i1 < applicant.length; i1++)
            for (int i2 = 0; i2 < applicant[i1].length; i2++)
                for (int i3 = 0; i3 < applicant[i1][i2].length; i3++)
                    for (int i4 = 0; i4 < applicant[i1][i2][i3].length; i4++)
                        Arrays.fill(applicant[i1][i2][i3][i4], 0);

        for (String str : info) {
            String[] tmp = str.split(" ");

            for (int i1 : lanMap.get(tmp[0]))
                for (int i2 : posMap.get(tmp[1]))
                    for (int i3 : carMap.get(tmp[2]))
                        for (int i4 : fooMap.get(tmp[3]))
                            applicant[i1][i2][i3][i4][Integer.parseInt(tmp[4])]++;

        }

        for (int i1 = 0; i1 < applicant.length; i1++)
            for (int i2 = 0; i2 < applicant[i1].length; i2++)
                for (int i3 = 0; i3 < applicant[i1][i2].length; i3++)
                    for (int i4 = 0; i4 < applicant[i1][i2][i3].length; i4++)
                        for (int i5 = applicant[i1][i2][i3][i4].length - 2; i5 >= 0; i5--)
                            applicant[i1][i2][i3][i4][i5] += applicant[i1][i2][i3][i4][i5 + 1];

        for (String str : query) {
            String[] tmp = str.split(" ");
            int result = 0;

            for (int i1 : lanMap.get(tmp[0]))
                for (int i2 : posMap.get(tmp[2]))
                    for (int i3 : carMap.get(tmp[4]))
                        for (int i4 : fooMap.get(tmp[6]))
                            result += applicant[i1][i2][i3][i4][Integer.parseInt(tmp[7])];

            answer.add(result);
        }

        return answer.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        new Rank().solution(new String[]{"java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"},
                new String[]{"java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"});
        // [1,1,1,1,2,4]
    }
}
