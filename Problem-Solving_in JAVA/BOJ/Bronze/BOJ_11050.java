import java.io.*;
import java.util.*;


public class BOJ_11050 {
	static int[][] dp;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		dp = new int [N+1][N+1];
		
		for (int i = 0; i <= N; i++) {
			dp[i][1] = i;
			dp[i][i] = 1;
			dp[i][0] = 1;
		}
		
		for (int i = 2; i <= N; i++) {
			for (int j = 1; j < i; j++) {
				dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
			}
		}
		
		System.out.println(dp[N][K]);
	}

}
