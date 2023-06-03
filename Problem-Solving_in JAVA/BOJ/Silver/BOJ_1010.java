import java.io.*;
import java.util.*;

public class BOJ_1010 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int[][] dp = new int[31][31];
		
		for (int i = 0; i <= 30; i++) {
			dp[i][i] = 1;
			dp[i][0] = 1;
			dp[i][1] = i;
		}
		
		for (int i = 2; i <= 30; i++) {
			for (int j = 1; j < i; j++) {
				dp[i][j] = dp[i-1][j] + dp[i-1][j-1];
			}
		}
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < T; tc++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			
			System.out.println(dp[m][n]);
		}

	}

}
