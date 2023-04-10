import java.io.*;
import java.util.*;


public class BOJ_1920 {
	static int A[];
	static boolean flag;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		A = new int[N];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for (int i = 0; i < N; i++) {
			A[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(A);
		
//		for (int i = 0; i < N; i++) {
//			System.out.println(A[i]);
//		}
		
		int M = Integer.parseInt(br.readLine());
		
		st = new StringTokenizer(br.readLine());
		
		for (int j = 0 ; j < M ; j++) {
			flag = false;
			int f = Integer.parseInt(st.nextToken());
			bSearch(0, N-1, f);
			if (flag) {
				System.out.println(1);
			}
			else {
				System.out.println(0);
			}
		}
	}
	
	public static void bSearch(int start, int end, int findNum) {
		if (flag | start > end) {
			return ;
		}
		int mid = (start + end) / 2;
		if (A[mid] == findNum) {
			flag = true;
			return ;
		}
		
		else if (A[mid] > findNum) {
			bSearch(start, mid-1, findNum);
		}
		
		else {
			bSearch(mid+1, end, findNum);
		}
		return ;
	}

}
