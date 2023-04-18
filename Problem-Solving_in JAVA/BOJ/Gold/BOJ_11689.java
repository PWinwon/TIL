import java.io.*;
import java.util.*;


public class BOJ_11689 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		long N = sc.nextLong();
		
//		int[] A = new int[N+1];
//		
//		for (int i = 0; i <= N; i++) {
//			A[i] = i;
//		}
		
		long answer = N;
		
		for (int i = 2; i <= Math.sqrt(N); i++) {
			if (N % i == 0) {
				answer -= answer / i;
				while (N % i == 0) {
					N /= i;
				}
			}
		}
		
		if (N > 1) {
			answer -= answer / N;
		}
		System.out.println(answer);
	}

}
