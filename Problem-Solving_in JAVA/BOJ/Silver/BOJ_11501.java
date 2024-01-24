import java.io.*;
import java.util.*;


public class BOJ_11501 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int T = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for (int tc = 0; tc < T; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[] nums = new int[N];
			st = new StringTokenizer(br.readLine());
			for (int n = 0; n < N; n++) {
				nums[n] = Integer.parseInt(st.nextToken());
			}
			
			int maxValue = -1;
			long sum = 0;
			
			for (int n = N-1; n >= 0; n--) {
				// 현재 최고가 갱신 o
				if (nums[n] > maxValue) {
					maxValue = nums[n];
				}
				// 				x
				
				sum += maxValue - nums[n];
			}
			
			sb.append(sum + "\n");
			
			
		}
		
		System.out.println(sb.toString());	

	}

}
