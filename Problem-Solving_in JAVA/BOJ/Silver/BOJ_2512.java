import java.io.*;
import java.util.*;


public class BOJ_2512 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[] arr = new int[N];
		
		int left = 0;
		int right = -1;
		
		st = new StringTokenizer(br.readLine());
		for (int n = 0; n < N; n++) {
			arr[n] = Integer.parseInt(st.nextToken());
			right = Math.max(right, arr[n]);
		}
		
		int M = Integer.parseInt(br.readLine());
		
		while (left <= right) {
			int mid = (left + right) / 2;
			long budget = 0;
			for (int i = 0; i < N; i++) {
				if (arr[i] > mid) budget += mid;
				else budget += arr[i];
			}
			
			if(budget <= M) {
				left = mid + 1;
			} else {
				right = mid - 1;
			}
		}
		
		System.out.println(right);

	}

}
