import java.io.*;
import java.util.*;


public class BOJ_2240 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int T = Integer.parseInt(st.nextToken());
		int W = Integer.parseInt(st.nextToken());
		
		int[][] dp = new int[W+1][T+1];
		int[] origin = new int[T+1];
		
		dp[0][0] = 0;
		origin[0] = 0;
		
		for (int i = 1; i <= T; i++) {
			int a = Integer.parseInt(br.readLine());
			origin[i] = a - 1;
			dp[0][i] = dp[0][i-1];
			if (a == 1) dp[0][i] += 1;
		}
		
		for (int w = 1; w <= W; w++) {
			dp[w][0] = 0;
			for (int t = 1; t <= T; t++) {
				int dum = 0;
				// 현재 w 위치에 나무열매가 떨어지는 경우
				if (origin[t] == w % 2) {
					dum = 1;
				}
				dp[w][t] = Math.max(dp[w-1][t-1], dp[w][t-1]) + dum;
			}
		}
		
		int answer = -1;
		
		for (int i = 0; i <= W; i++) {
			if (answer < dp[i][T]) answer = dp[i][T];
		}
		
//		myDebug(T, W, dp);
		
		System.out.println(answer);

	}
	
	public static void myDebug(int t, int w, int[][] d) {
		for (int i = 0; i <= w; i++) {
			for (int j = 0; j <= t; j++) {
				System.out.print(d[i][j] + " ");
			}
			System.out.println();
		}
	}

}
