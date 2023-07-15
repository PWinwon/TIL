import java.io.*;
import java.util.*;


public class BOJ_1159 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		int[] alpha = new int[26];
		
		for (int n = 0; n < N; n++) {
			char c = br.readLine().charAt(0);
			alpha[c - 'a'] += 1;
		}
		
		StringBuffer sb = new StringBuffer();
		
		for (int i = 0; i < 26; i++) {
			if (alpha[i] > 4) sb.append((char)('a' + i));
		}
		
		if (sb.length() == 0) System.out.println("PREDAJA");
		else System.out.println(sb.toString());

	}

}
