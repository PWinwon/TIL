import java.util.Scanner;

public class test {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[] dp = new int[N+1];
		dp[0] = 1;
		dp[1] = 1;
//		dp[2] = 2;
		
		for (int i = 2; i <= N; i++) {
			dp[i] = (dp[i-1] + dp[i-2]) % 15746;
		}
		
		System.out.println(dp[N]);
	}

}