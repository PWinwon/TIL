import java.io.*;
import java.util.*;


public class BOJ_1915 {
//	//				  상 좌상 좌
//	static int[] dr = {-1, -1, 0};
//	static int[] dc = {0, -1, -1};

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		long[][] dp = new long[R][C];
		long answer = 0;
		
		for (int r = 0; r < R; r++) {
			char[] temp = br.readLine().toCharArray();
			for (int c = 0; c < C; c++) {
				dp[r][c] = Long.parseLong(String.valueOf(temp[c]));
				if (dp[r][c] == 1 && r > 0 && c > 0) {
					dp[r][c] = Math.min(dp[r-1][c-1], Math.min(dp[r-1][c], dp[r][c-1])) + dp[r][c];
				}
				if (answer < dp[r][c]) answer = dp[r][c];
			}
		}
		
//		
//		for (int r = 1; r < R; r++) {
//			for (int c = 1; c < C; c++) {
//				if (dp[r][c] == 1) {
//					int cnt = Integer.MAX_VALUE;
//					for (int i = 0; i < 3; i++) {
//						cnt = Math.min(dp[r+dr[i]][c+dc[i]], cnt);
//					}
//					dp[r][c] += cnt;
//				}
//				
//				if (answer < dp[r][c]) answer = dp[r][c];
//			}
//		}
		
		System.out.println(answer * answer);

	}

}
