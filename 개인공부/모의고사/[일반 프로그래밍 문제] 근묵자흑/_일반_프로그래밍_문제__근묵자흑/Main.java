import java.io.*;
import java.util.Scanner;


class Main {
	public static void main(String[] args) throws Exception {
		Scanner scan = new Scanner(System.in);
		int len = scan.nextInt();	//남은 글자 수
		int k = scan.nextInt();		//몇개씩 따로 빼놓을 것인지
		int answer = 0;
		int arr[] = new int[len];
		for(int i=0;i < len;i++){
			arr[i] = scan.nextInt();
		}
		for(int i=0;i < len;){	//전체 배열에 대해서 조사
			for(int j=0;j < k-1;j++){
				if(i+j >= len)	//배열 인덱스 초과 방지
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