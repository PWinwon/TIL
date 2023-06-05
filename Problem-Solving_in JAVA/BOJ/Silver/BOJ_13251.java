import java.io.*;
import java.util.*;


public class BOJ_13251 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int M = Integer.parseInt(br.readLine());
		
		int[] D = new int[M];
		double[] pb = new double[M];
		int T = 0;
		
		st = new StringTokenizer(br.readLine());
		
		for (int m = 0; m < M; m++) {
			D[m] = Integer.parseInt(st.nextToken());
			T += D[m];
		}
		
		int K = Integer.parseInt(br.readLine());
		
		double answer = 0.0;
		
		for (int i = 0; i < M; i++) {
			if (D[i] >= K) {
				pb[i] = 1.0;
				for (int k = 0; k < K; k++) {
					pb[i] *= (double) (D[i] - k) / (T - k);
				}
				answer += pb[i];
			}
		}
		
		System.out.println(answer);
		
		
	}

}
