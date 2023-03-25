import java.io.*;
import java.util.*;


public class BOJ_1377_2 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int N = Integer.parseInt(br.readLine());
		
		idxData[] A = new idxData[N];
		
		for (int n = 0; n < N; n++) {
			A[n] = new idxData(Integer.parseInt(br.readLine()), n);
		}
		Arrays.sort(A);
		
		int answer = -1;
		
		for (int i = 0; i < N; i++) {
			if (answer < A[i].idx - i) {
				answer = A[i].idx - i;
			}
		}
		System.out.print(answer + 1);
		
	}
	
	static class idxData implements Comparable<idxData> {
		int value;
		int idx;
		
		public idxData(int value, int idx) {
			super();
			this.value = value;
			this.idx = idx;
		}
		
		@Override
		public int compareTo(idxData o) {
			return this.value - o.value;
		}
	}

}



// 시간 초과. 다른 아이디어가 필요
// import java.io.*;
// import java.util.*;


// public class BOJ_1377 {

// 	public static void main(String[] args) throws Exception {
// 		// TODO Auto-generated method stub
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
// 		int N = Integer.parseInt(br.readLine());
		
// 		int[] A = new int [N+1];
		
// 		for (int n = 1; n <= N; n++) {
// 			A[n] = Integer.parseInt(br.readLine());
// 		}
		
// 		boolean flag = true;
// 		int temp = -1;
		
// 		for (int i = 1; i <= N; i++) {
// 			flag = true;
// 			for (int j = 1; j <= N - i - 1; j++) {
// 				if (A[j] > A[j+1]) {
// 					flag = false;
// 					temp = A[j];
// 					A[j] = A[j+1];
// 					A[j+1] = temp;
// 				}
// 			}
// 			if (flag) {
// 				System.out.print(i);
// 				break;
// 			}
// 		}

// 	}

// }
