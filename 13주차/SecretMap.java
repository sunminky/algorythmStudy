package week13;

public class SecretMap {
    public static void main(String[] args) {
        int[] arr1 = {9, 20, 28, 18, 11};
        int[] arr2 = {30, 1, 21, 17, 28};
        String[] ret = new SecretMap().solution(5,arr1,arr2);
        for(int i = 0;i < ret.length;i++)
            System.out.println(ret[i]);
    }
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = {};
        int map1[][] = flatten(arr1,n);
        int map2[][] = flatten(arr2,n);

        answer = drawWall(map1,map2,n);
        return answer;
    }
    public int[][] flatten(int[] map,int size){
        int ret[][] = new int[size][size];

        for(int i = 0;i < size;i++){
            String bin = Integer.toBinaryString(map[i]);
            for(int j = 0;j < bin.length();j++){
                ret[i][size-bin.length()+j] = bin.charAt(j)-48;
            }
        }
        return ret;
    }
    public String maptoString(int[] map){
        StringBuilder ret = new StringBuilder();
        for(int i = 0;i < map.length;i++){
            if(map[i] == 0)
                ret.append(" ");
            else
                ret.append("#");
        }
        return ret.toString();
    }
    public String[] drawWall(int[][] map1,int[][] map2,int size){
        int combination[][] = new int[size][size];
        String[] ret = new String[size];

        for(int i = 0;i < size;i++){
            for(int j = 0;j < size;j++){
                combination[i][j] = map1[i][j] | map2[i][j];
            }
            ret[i] = maptoString(combination[i]);
        }
        return ret;
    }
}
