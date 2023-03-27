import java.io.*;
import java.util.*;


public class BOJ_2023 {
	
	static boolean[] primeNums;
	static int N;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		
//		int lenN = (int) Math.pow(10, N);
//		primeNums = new boolean[lenN];
//		
//		primeCheck(primeNums, lenN);
		
		amazingPrime(2, 1);
		amazingPrime(3, 1);
		amazingPrime(5, 1);
		amazingPrime(7, 1);
	}
	
//	public static void primeCheck(boolean[] primeNums, int lenN) {
//		primeNums[0] = true;
//		primeNums[1] = true;
//		
//		int idx = 2;
//		int dIdx = 0;
//		
//		while (idx <= Math.sqrt(lenN)) {
//			dIdx = idx;
//			for (int i = idx * 2; i < lenN; i += dIdx) {
//				primeNums[i] = true;
//			}
//			idx++;
//		}
//	}
	
	public static boolean primeCheck(int num) {
		for (int i = 2; i <= Math.sqrt(num); i++) {
			if (num % i == 0) {
				return true;
			}
		}		
		return false;
	}
	
	public static void amazingPrime(int num, int lenN) {
		if (primeCheck(num)) {
			return;
		}
		if (lenN == N) {
			System.out.println(num);
			return;
		}		
		for (int i = 1; i < 10; i += 2) {
			amazingPrime(num * 10 + i, lenN+1);
		}
		
	}

}
