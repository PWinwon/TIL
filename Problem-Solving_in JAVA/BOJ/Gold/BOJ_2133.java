import java.io.*;
import java.util.*;


public class BOJ_2133 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		System.out.println(myFunc(N));

	}
	
	public static int myFunc(int n) {
		if (n % 2 == 1) return 0;
		
		int[] dp = new int[n+1];
		
		dp[0] = 1;
		
		for (int i = 2; i <= n; i += 2) {
			dp[i] = dp[i-2] * 3;
			
			for (int j = i-4; j >= 0; j -= 2) {
				dp[i] += dp[j] * 2;
			}
		}
		
		return dp[n];
	}

}
