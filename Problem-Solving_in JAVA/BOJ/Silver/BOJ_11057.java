import java.io.*;
import java.util.*;


public class BOJ_11057 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		int[][] dp = new int[N][10];
		
		for (int i = 0; i < 10; i++) {
			dp[0][i] = 1;
		}
		
		for (int n = 1; n < N; n++) {
			dp[n][0] = 1;
			for (int i = 1; i < 10; i++) {
				dp[n][i] = (dp[n][i-1] + dp[n-1][i]) % 10007;
			}
		}

		int answer = 0;
		
		for (int i = 0; i < 10; i++) {
			answer += dp[N-1][i];
			answer %= 10007;
		}
		
		System.out.println(answer);
	}

}
