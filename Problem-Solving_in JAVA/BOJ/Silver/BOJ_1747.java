import java.io.*;
import java.util.*;


public class BOJ_1747 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		boolean[] isPrime = new boolean[10000001];
		isPrime[0] = true;
		isPrime[1] = true;
		
		for (int i = 2; i < Math.sqrt(isPrime.length); i++) {
			if (isPrime[i]) {
				continue;
			}
			// N 이상이면서 소수라면 바로 검증
			for (int j = i+i; j < isPrime.length; j += i) {
				isPrime[j] = true;
			}
		}
		
		while (true) {
			if (!isPrime[N] & isPD(N)) {
				System.out.println(N);
				break;
			}
			N++;
		}
		
	}
	
	public static boolean isPD(int num) {
		char[] c = String.valueOf(num).toCharArray();
		int start = 0;
		int end = c.length-1;
		
		while (start < end) {
			if (c[start] != c[end]) {
				return false;
			}
			start++;
			end--;
		}		
		return true;
	}

}
