import java.io.*;
import java.util.*;


public class BOJ_11052 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] cards = new int[N+1];
		int[] dp = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 1; i <= N; i++) {
			cards[i] = Integer.parseInt(st.nextToken());
		}
		
		
		for (int i = 1; i <= N; i++) {
			int card = cards[i];
			for (int j = i; j <= N; j++) {
				dp[j] = Math.max(dp[j-i] + card, dp[j]); 
			}
		}
		
		System.out.println(dp[N]);

	}

}
