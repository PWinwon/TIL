import java.io.*;
import java.util.*;


public class BOJ_1515 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String num = br.readLine();
		
		int N = 1;
		String n = "0";
		int nIdx = 0;
		int idx = 0;
		
		while (idx < num.length()) {
			int a = num.charAt(idx) - '0';
			
			if (n.equals("0")) {
				n = String.valueOf(N);
				nIdx = 0;
				N++;
			}
			
			while (nIdx < n.length()) {
				if (a == n.charAt(nIdx) - '0') {
					idx++;
					nIdx++;
					break;
				}
				nIdx++;
			}
			
			if (nIdx >= n.length()) {
				n = "0";
			}
		}
		
		System.out.println(N-1);
		
//		int[] nCnt = new int[10];
//		int[] numCnt = new int[10];
//		
//		for (int i = 0; i < num.length(); i++) {
//			int a = num.charAt(i) - '0';
//			numCnt[a]++;
//		}
//		
//		int N = 1;
//		
//		while (true) {
//			int n = N;
//			while (n > 0) {
//				nCnt[n % 10]++;
//				n /= 10;
//			}
//			
//			if (possibleCnt(numCnt, nCnt)) break;
//			N++;
//		}
//		
//		System.out.println(N);

	}
	
//	public static boolean possibleCnt(int[] origin, int[] n) {
//		for (int i = 0; i < 10; i++) {
//			if (origin[i] > n[i]) return false;
//		}
//		return true;
//	}
//	
//	public static void printCnt(int[] a) {
//		for (int i = 0; i < 10; i++) {
//			System.out.print(a[i] + " ");
//		}
//	}

}
