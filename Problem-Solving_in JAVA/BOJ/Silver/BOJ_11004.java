import java.io.*;
import java.util.*;

public class BOJ_11004 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int[] A = new int [N];
		
		for (int n = 0; n < N; n++) {
			A[n] = Integer.parseInt(st.nextToken());
		}
		
		myQuickSort(A, 0, N-1, K-1);
		System.out.print(A[K-1]);
		
	}
	
	public static void myQuickSort(int[] A, int start, int end, int K) {
		if (start < end) {
			int pivot = myFunc(A, start, end);
			if (pivot == K) {
				return;
			}
			else if (K < pivot) {
				myQuickSort(A, start, pivot-1, K);
			}
			else {
				myQuickSort(A, pivot+1, end, K);
			}
			
		}
	}
	
	public static int myFunc(int[] A, int start, int end) {
		int mid = (start + end)/2;
		swap(A, start, mid);
		int pivot = A[start];
		
		int i = start;
		int j = end;
		
		while (i < j) {
			while (pivot < A[j]) {
				j--;
			}
			while (i < j && pivot >= A[i]) {
				i++;
			}
			swap(A, i, j);
		}
		A[start] = A[i];
		A[i] = pivot;
		return i;
	}
	
	public static void swap(int[] A, int i, int j) {
		int temp = A[i];
		A[i] = A[j];
		A[j] = temp;
	}
}
