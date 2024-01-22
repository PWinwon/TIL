import java.io.*;
import java.util.*;


public class BOJ_19637 {
	static int N, M;
	static int[] nums;
	static String[] strs;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		nums = new int[N];
		strs = new String[N];
		
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			strs[i] = st.nextToken();
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		StringBuilder sb = new StringBuilder();
		
		for (int m = 0; m < M; m++) {
			int num = Integer.parseInt(br.readLine());
			String s = BSearch(num);
			sb.append(s + "\n");
		}
		
		System.out.println(sb.toString());

	}

	private static String BSearch(int num) {
		// TODO Auto-generated method stub
		int l = 0;
		int r = N-1;
		while (l <= r) {
			int mid = (l+r) / 2;
			if(nums[mid] < num) {
				l = mid + 1;
			} else {
				r = mid - 1;
			}
		}
		
		return strs[r+1];
	}

}
