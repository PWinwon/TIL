import java.io.*;
import java.util.*;


public class BOJ_2343 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		
		int[] A = new int[N];
		int start = -1;
		int end = 0;
		
		for (int i = 0; i < N ; i++) {
			A[i] = Integer.parseInt(st.nextToken());
			end += A[i];
			if (start < A[i]) {
				start = A[i];
			}
		}

		
		while (start <= end) {
			int mid = (start+end) / 2;
			int cnt = 0;
			int sum = 0;
			for (int i = 0 ; i < N; i++) {
				if (sum + A[i] > mid) {
					sum = 0;
					cnt++;
				}
				sum += A[i];
			}
			
			if (sum != 0) {
				cnt += 1;
			}
			
			if (cnt > M) {
				start = mid + 1;
			}
			else {
				end = mid - 1;
			}
		}
		
		System.out.println(start);
	}
}
