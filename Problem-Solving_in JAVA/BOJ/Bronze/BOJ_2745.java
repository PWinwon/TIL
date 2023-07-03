import java.io.*;
import java.util.*;


public class BOJ_2745 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		char[] c = st.nextToken().toCharArray();
		int order = Integer.parseInt(st.nextToken());
		
		int answer = 0;
		
		for (int i = 0; i < c.length; i++) {
			answer *= order;
			answer += myFunc(c[i]);
			
		}
		
		System.out.println(answer);

	}
	
	public static int myFunc(char n) {		
		if (n - '0' < 10) return n - '0';
				
		return n - 'A' + 10;
	}

}
