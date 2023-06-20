import java.io.*;
import java.util.*;


public class BOJ_11726 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		int[] dp = new int [N+1];
		
		dp[0] = 1;
		dp[1] = 2;
		
		for (int i = 2; i < N; i++) {
			dp[i] = (dp[i-1] + dp[i-2]) % 10007;
		}
		
		System.out.println(dp[N-1]);

	}

}
