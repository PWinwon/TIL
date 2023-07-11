import java.io.*;
import java.util.*;


public class BOJ_10431 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuffer sb = new StringBuffer();
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			int[] a = new int[20];
			st = new StringTokenizer(br.readLine());
			
			sb.append(st.nextToken()).append(" ");
			
			for (int i = 0; i < 20; i++) {
				a[i] = Integer.parseInt(st.nextToken());
			}
			
			int cnt = 0;
			
			for (int i = 0; i < 20; i++) {
				for (int j = 0; j < i; j++) {
					if (a[j] > a[i]) cnt++;
				}
			}
			
			sb.append(cnt).append("\n");
		}
		
		System.out.println(sb);

	}

}
