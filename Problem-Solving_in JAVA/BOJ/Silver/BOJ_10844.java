import java.io.*;
import java.util.*;


public class BOJ_10844 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		
		int[][] dp = new int[n][12];
		
		for (int i = 1; i < 11; i++) {
			dp[0][i] = 1;
		}
		
		for (int nIdx = 1; nIdx < n; nIdx++) {
			for (int i = 1; i < 11; i++) {
				dp[nIdx][i] = (dp[nIdx-1][i-1] + dp[nIdx-1][i+1]) % 1000000000;
			}
		}
		
		int answer = 0;
		
		for (int i = 2; i < 11; i++) {
			answer += dp[n-1][i];
			answer %= 1000000000;
		}
		
		System.out.println(answer);

	}

}
