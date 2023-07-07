import java.io.*;
import java.util.*;


public class BOJ_7576 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		char[] c = br.readLine().toCharArray();
		
		int answer = 10;
		
		for (int i = 1; i < c.length; i++) {
			if (c[i-1] == c[i]) answer += 5;
			else answer += 10;
		}
		
		System.out.println(answer);

	}

}
