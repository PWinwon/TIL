import java.io.*;
import java.util.*;


public class BOJ_1427 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		String N = br.readLine();
		
		int[] A = new int[N.length()];
		
		for (int i = 0; i < N.length(); i++) {
			A[i] = Integer.parseInt(N.substring(i, i+1));
		}
		
		int maxValue = 0;
		int temp = 0;
		
		for (int i = 0; i < N.length(); i++) {
			maxValue = i;
			for (int j = i+1; j < N.length(); j++) {
				if (A[maxValue] < A[j]) {
					maxValue = j;
				}
			}
			if (A[i] < A[maxValue]) {
				temp = A[i];
				A[i] = A[maxValue];
				A[maxValue] = temp;
			}
		}
		
//		for (int i = 0; i < N.length(); i++) {
//			System.out.print(A[i]);
//		}
		
		for (int i = 0; i < N.length(); i++) {
			sb.append(A[i]);
		}
		System.out.print(sb);
	}

}
