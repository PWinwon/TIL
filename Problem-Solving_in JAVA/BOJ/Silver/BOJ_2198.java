import java.io.*;
import java.util.*;


public class BOJ_2198 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		long[] dp = new long[N+1];
		dp[1] = 1;
		
		for (int i = 2; i < N+1; i++) {
			dp[i] = dp[i-1] + dp[i-2];
		}
		
		System.out.println(dp[N]);

	}

}
