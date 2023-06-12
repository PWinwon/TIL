import java.io.*;
import java.util.*;


public class BOJ_1256 {
	static int N, M, K;
	static int[][] dp;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		M = sc.nextInt();
		K = sc.nextInt();
		
		dp = new int[202][202];
		
		for (int i = 0; i <= 200; i++) {
			for (int j = 0; j <= i; j++) {
				if (j == 0 || j == i) dp[i][j] = 1;
				else {
					dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
					if (dp[i][j] > 1000000000) dp[i][j] = 1000000001;
				}
			}
		}
		
		if (dp[N+M][M] < K) System.out.println(-1);
		else {
			while (!(N == 0 && M == 0)) {
				if (dp[N-1+M][M] >= K) {
					System.out.print("a");
					N--;
				}
				else {
					System.out.print("z");
					K = K - dp[N-1+M][M];
					M--;
				}
			}
		}

	}

}
