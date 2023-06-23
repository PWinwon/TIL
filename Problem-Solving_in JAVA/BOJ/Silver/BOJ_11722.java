import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class BOJ_11722 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int[] A = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		System.out.println(myFunc(N, A));
		

	}
	
	public static int myFunc(int n, int[] cost) {
		int answer = Integer.MIN_VALUE;

		int[] dp = new int[n];

		dp[0] = 1;

		for (int i = 1; i < n; i++) {
			dp[i] = 1;
			for (int j = 0; j < i; j++) {
				if (cost[i] < cost[j]) dp[i] = Math.max(dp[j] + 1, dp[i]);
			}
		}

		for (int i = 0; i < n; i++) {
			if (answer < dp[i]) answer = dp[i];
		}

		return answer;
	}


}
