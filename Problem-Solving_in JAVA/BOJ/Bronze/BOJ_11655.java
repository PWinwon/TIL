import java.io.*;
import java.util.*;

public class BOJ_11655 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] c = br.readLine().toCharArray();
		
		for (int i = 0; i < c.length; i++) {
			// 소문자 일 경우
			if (0 <= c[i] - 'a' && c[i] - 'a' < 26) {
				c[i] = (char) ((c[i] - 'a' + 13) % 26 + 'a');
			}
			
			else if (0 <= c[i] - 'A' && c[i] - 'A' < 26) {
				c[i] = (char) ((c[i] - 'A' + 13) % 26 + 'A');
			}
			
			System.out.print(c[i]);
		}
		
//		System.out.print

	}

}
