import java.io.*;
import java.util.*;


public class BOJ_1253 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int A[] = new int [N];
		
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(A);
		int answer = 0;
		int leftIdx = 0;
		int rightIdx = N-1;
		
		for (int k = 0; k < N; k++) {
			leftIdx = 0;
			rightIdx = N-1;
			while (leftIdx < rightIdx) {
				if (leftIdx == k) {
					leftIdx++;
					continue;
				}
				else if (rightIdx == k) {
					rightIdx--;
					continue;
				}
				
				if (A[leftIdx] + A[rightIdx] == A[k]) {
					answer++;
					break;
				}
				else if (A[leftIdx] + A[rightIdx] > A[k]) {
					rightIdx--;
				}
				else {
					leftIdx++;
				}
			}
		}
		System.out.print(answer);
	}
}
