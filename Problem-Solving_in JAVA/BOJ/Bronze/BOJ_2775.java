import java.io.*;
import java.util.*;


public class BOJ_2755 {
	static int T;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int[][] dp = new int[15][15];
		
		for (int i = 0; i < 15; i++) {
			dp[i][1] = 1;
			dp[0][i] = i;
		}
		
		for (int i = 1; i < 15; i++) {
			for (int j = 1; j < 15; j++) {
				dp[i][j] = dp[i][j-1] + dp[i-1][j];
			}
		}
		
		T = sc.nextInt();
		
		for (int tc = 0; tc < T; tc++) {
			int k = sc.nextInt();
			int n = sc.nextInt();
			System.out.println(dp[k][n]);
		}

	}

}
