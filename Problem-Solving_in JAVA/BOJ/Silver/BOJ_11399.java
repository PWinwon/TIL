import java.io.*;
import java.util.*;


public class BOJ_11399 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int[] A = new int [N+1];
		
		for (int i = 1; i <= N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(A);
		
		int answer = 0;
		
		for (int i = 1; i <= N; i++) {
			A[i] += A[i-1];
			answer += A[i];
		}
		System.out.print(answer);
	}

}
