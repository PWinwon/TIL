import java.io.*;
import java.util.*;


public class BOJ_9655 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[] dp = new int[Math.max(N+1, 3)];
		dp[0] = 0;
		dp[1] = 1;
		dp[2] = 2;
		
		for (int n = 3; n <= N; n++) {
			dp[n] = Math.min(dp[n-1], dp[n-3]) + 1;
		}
		
		if (dp[N] % 2 == 0) {
			System.out.println("CY");
		}
		else {
			System.out.println("SK");
		}

	}

}
