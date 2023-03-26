import java.io.*;
import java.util.*;


public class BOJ_2751 {
	
	public static int[] A, tmp;
	public static long result;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		
		A = new int[N+1];
		tmp = new int[N+1];
		
		for (int i = 1; i <= N; i++) {
			A[i] = Integer.parseInt(br.readLine());
		}
		myMergeSort(1, N);
		
		for (int i = 1; i <= N; i++) {
			bw.write(A[i] + "\n");
		}
		bw.flush();
		bw.close();
		
	}
	
	public static void myMergeSort(int s, int e) {
		if (e - s < 1) {
			return;
		}
		int m = s + (e - s) / 2;
		
		myMergeSort(s, m);
		myMergeSort(m+1, e);
		
		for (int i = s; i <= e; i++) {
			tmp[i] = A[i];
		}
		
		int k = s;
		int idx1 = s;
		int idx2 = m+1;
		
		while (idx1 <= m && idx2 <= e) {
			if (tmp[idx1] > tmp[idx2]) {
				A[k] = tmp[idx2];
				k++;
				idx2++;
			}
			else {
				A[k] = tmp[idx1];
				k++;
				idx1++;
			}
		}
		while (idx1 <= m) {
			A[k] = tmp[idx1];
			k++;
			idx1++;
		}
		
		while (idx2 <= e) {
			A[k] = tmp[idx2];
			k++;
			idx2++;
		}
		
	}

}
