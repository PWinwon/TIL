import java.io.*;
import java.util.*;


public class BOJ_10988 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		char[] str = sc.next().toCharArray();
		
		int leftIdx = 0;
		int rightIdx = str.length - 1;
		
		int answer = 1;
		
		while (leftIdx < rightIdx) {
			if (str[leftIdx] != str[rightIdx]) {
				answer = 0;
				break;
			}
			leftIdx++;
			rightIdx--;
		}
		
		System.out.println(answer);

	}

}
