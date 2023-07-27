import java.io.*;
import java.util.*;


public class BOJ_2294 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		int[] dp = new int[K+1];
		
		for (int i = 0; i <= K; i++) {
			dp[i] = 10001;
		}
		
		for (int i = 0; i < N; i++) {
			int coin = Integer.parseInt(br.readLine());
			
			if (coin > K) continue;
			
			dp[coin] = 1;			
			
			for (int j = coin; j <= K; j++) {
				dp[j] = Math.min(dp[j - coin] + 1, dp[j]);
			}
		}
		
		if (dp[K] == 10001) System.out.println(-1);
		else System.out.println(dp[K]);

	}
	

}
