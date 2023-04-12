import java.io.*;
import java.util.*;


public class BOJ_1300 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		int K = Integer.parseInt(br.readLine());
		
		int start = 1;
		int end = K;
		int answer = -1;
		while (start <= end) {
			int mid = (start + end) / 2;
			int cnt = 0;
			for (int i = 1 ; i <= N; i++) {
				cnt += Math.min(mid / i, N);
			}
			
			if (cnt < K) {
				start = mid + 1;
			}
			else {
				end = mid - 1;
				answer = mid;
			}
		}
		System.out.println(answer);

	}

}
