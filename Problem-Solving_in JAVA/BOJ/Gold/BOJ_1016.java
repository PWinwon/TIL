import java.io.*;
import java.util.*;


public class BOJ_1016 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		long start = sc.nextLong();
		long end = sc.nextLong();
		
		
		boolean[] isSquare = new boolean[(int) (end - start + 1)];
		
		for (long i = 2; i * i < end+1; i++) {
			long pow = i * i;
			long startIdx = start / pow;
			if (start % pow != 0) {
				startIdx++;
			}
			
			for (long j = startIdx; j * pow < end+1; j++) {
				isSquare[(int) ((j * pow) - start)] = true;
			}
		}
		
		
		int answer = 0;
		
		for (int i = 0; i < end-start+1; i++) {
			if (isSquare[i]) {
				continue;
			}
			answer++;
		}

		System.out.println(answer);
	}

}
