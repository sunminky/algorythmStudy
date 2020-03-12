import java.io.*;
import java.util.Scanner;


class Main {
	public static void main(String[] args) throws Exception {
		Scanner scan = new Scanner(System.in);
		int len = scan.nextInt();	//남은 글자 수
		int k = scan.nextInt();
		int idx = 0;
		int answer = 0;
		int arr[] = new int[len];
		for(int i=0;i < len;i++){
			arr[i] = scan.nextInt();
		}
		for(int i=0;i < len;){
			for(int j=0;j < k-1;j++){
				if(i+j >= len)
					break;
				if(arr[i+j] == 1){
					i++;
				}
			}
			i+=(k-1);
			answer++;
		}
		System.out.println(answer);
	}
}