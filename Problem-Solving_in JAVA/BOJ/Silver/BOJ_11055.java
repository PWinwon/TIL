import java.io.*;
import java.util.*;


public class BOJ_11055 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] A = new int[N+1];
		int[] dp = new int[N+1];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 1; i < N+1; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		dp[1] = A[1];
		
		for (int i = 2; i < N+1; i++) {
			dp[i] = A[i];
			for (int j = 1; j < i; j++) {
				if (A[i] > A[j]) dp[i] = Math.max(dp[j] + A[i], dp[i]); 
			}
		}
		
		int answer = Integer.MIN_VALUE;
		
		for (int i = 1; i <= N; i++) {
			if (dp[i] > answer) answer = dp[i];
		}
		
		System.out.println(answer);

	}

}
