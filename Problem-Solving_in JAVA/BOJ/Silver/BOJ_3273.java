import java.io.*;
import java.util.*;


public class BOJ_3273 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		
		int[] A = new int [N];
		
		st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		int X = Integer.parseInt(br.readLine());
		
		Arrays.sort(A);
		
		int s = 0;
		int e = N-1;
		int answer = 0;
		
		while (s < e) {
			int mySum = A[s] + A[e];
			if (mySum == X) {
				answer++;
				s++;
			}
			else if (mySum < X) {
				s++;
			}
			else {
				e--;
			}
		}
		
		System.out.println(answer);

	}

}
