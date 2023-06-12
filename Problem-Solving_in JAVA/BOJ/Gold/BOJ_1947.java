import java.io.*;
import java.util.*;


public class BOJ_1947 {
	static int N;
	static long[] dp;
	
	static long myMod = 1000000000;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		
		dp = new long[N+1];
		
		dp[0] = 0;
		dp[1] = 1;
		
		for (int i = 2; i <= N; i++) {
			dp[i] = i * (dp[i-1] + dp[i-2]) % myMod;
		}
		
		System.out.println(dp[N-1]);

	}

}
