import java.io.*;
import java.util.*;


public class BOJ_15486 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[][] arr = new int[N+2][2];
		int[] dp = new int[N+2];
		
		for(int i = 1; i < N+1; i++) {
			st = new StringTokenizer(br.readLine());
			
			int t = Integer.parseInt(st.nextToken());
			int p = Integer.parseInt(st.nextToken());
			arr[i][0] = t;
			arr[i][1] = p;
		}
		
		int maxVal = -1;
		
		for (int i = 1 ; i <= N+1; i++) {
			if (maxVal < dp[i]) maxVal = dp[i];
			
			int nxt = i + arr[i][0];
			if(nxt < N+2) dp[nxt] = Math.max(dp[nxt], maxVal+arr[i][1]);
		}
		
		System.out.println(dp[N+1]);
		
//		for (int i = 0; i < N+2; i++) {
//			System.out.print(dp[i] + " ");
//		}
			
	}

}
