package ForCodingTest.BruteForce;

public class Odd4letters {
    public static void main(String[] args) {
        int tmp = 0;
        for(int i=2992;i<10000;i++){
            tmp = cal(Integer.toHexString(i));
            if(tmp == cal(Integer.toString(i)) && tmp == cal(toDozenNotation(i)))
                System.out.println(i);
        }
    }
    public static String toDozenNotation(int source){
        StringBuilder stringBuilder = new StringBuilder();
        int tmp = 0;
        while(source != 0){
            tmp = source % 12;
            if(tmp == 10)
                stringBuilder.append('a');
            else if(tmp == 11)
                stringBuilder.append('b');
            else
                stringBuilder.append(tmp);
            source = source / 12;
        }
        return stringBuilder.toString();
    }
    public static int cal(String source){
        int sum = 0;
        for(int i=0;i<source.length();i++){
            switch (source.charAt(i)-48){
                case 0:
                    case 1:
                case 2:
                case 3:
                case 4:
                case 5:
                case 6:
                case 7:
                case 8:
                case 9:
                    sum += source.charAt(i)-48;
                    break;
                case 'a'-48:
                    sum += 10;
                    break;
                case 'b'-48:
                    sum += 11;
                    break;
                case 'c'-48:
                    sum += 12;
                    break;
                case 'd'-48:
                    sum += 13;
                    break;
                case 'e'-48:
                    sum+= 14;
                    break;
                case 'f'-48:
                    sum += 15;
                    break;
            }
        }
        return sum;
    }
}
