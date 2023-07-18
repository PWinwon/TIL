import java.io.*;
import java.util.*;


public class BOJ_1934 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		StringBuffer sb = new StringBuffer();
		
		int N = Integer.parseInt(br.readLine());
		
		for (int n = 0; n < N; n++) {
			st = new StringTokenizer(br.readLine());
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			sb.append(a * b / myGcd(a, b)).append("\n");
		}
		
		System.out.println(sb);

	}
	
	public static int myGcd(int a, int b) {
		
		while (b != 0) {
			int r = a % b;
			
			a = b;
			b = r;
		}
		
		return a;
	}

}
