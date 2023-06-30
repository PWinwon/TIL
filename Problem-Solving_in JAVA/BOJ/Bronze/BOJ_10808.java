import java.io.*;
import java.util.*;

public class BOJ_10808 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		char[] c = sc.next().toCharArray();
		
		int[] alpha = new int[26];
		
		for (int i = 0; i < c.length; i++) {
			alpha[c[i] - 'a'] += 1;
		}
		
		for (int i = 0; i < 26; i++) {
			System.out.print(alpha[i] + " ");
		}

	}

}
