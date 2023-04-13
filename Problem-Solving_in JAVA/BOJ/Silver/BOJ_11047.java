import java.io.*;
import java.util.*;

public class BOJ_11047 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		int[] A = new int [N];
		
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(br.readLine());
		}
		
		
		int answer = 0;
		for (int i = N-1; i >= 0; i--) {
			if (K == 0) {
				break;
			}
			answer += K / A[i];
			K = K % A[i];
		}
		System.out.println(answer);
	}

}
