import java.io.*;
import java.util.*;


public class BOJ_2293 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int[] dp = new int[K+1];
		int[] coins = new int[N];
		
		for (int n = 0; n < N; n++) {
			coins[n] = Integer.parseInt(br.readLine());
		}
		
		for (int n = 0; n < N; n++) {
			if (coins[n] > K) continue;
			dp[coins[n]]++;
			for (int k = coins[n]+1; k <= K; k ++) {
				dp[k] = dp[k] + dp[k - coins[n]];
			}
		}
		
//		printDp(N, K, dp);
		
		System.out.println(dp[K]);

	}
	
	public static void printDp(int n, int k, int[] d) {
		for (int i = 0; i < k+1; i++) {
			System.out.print(d[i] + " ");
		}
		System.out.println();
	}

}
