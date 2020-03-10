package ForCodingTest.Loop;

import java.util.Scanner;

public class ProhibitStudyingAbroad {
    public static void main(String[] args) {
        char[] target = {'C','A','M','B','R','I','D','G','E'};
        Scanner scanner = new Scanner(System.in);
        String victim = scanner.nextLine();

        for(int i=0;i<target.length;i++){
            victim = victim.replace(target[i],'!');
        }
        victim = victim.replace("!","");
        System.out.println(victim.toUpperCase());
    }
}
