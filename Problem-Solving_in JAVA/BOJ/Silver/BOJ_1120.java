import java.io.*;
import java.util.*;


public class BOJ_1120 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		char[] a = st.nextToken().toCharArray();
		char[] b = st.nextToken().toCharArray();

		int answer = Integer.MAX_VALUE;
		
		for (int i = 0; i <= b.length - a.length; i++) {
			int cnt = 0;
			
			for (int j = 0; j < a.length; j++) {
				if (a[j] != b[i+j]) cnt++;
			}
			
			if (cnt < answer) answer = cnt;
		}
		
		System.out.println(answer);
	}

}
