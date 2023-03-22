import java.io.*;
import java.util.*;


public class boj_2018 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		
		int numArray[] = new int [N+1];
		
		for (int i = 1; i < N; i++) {
			numArray[i] = i;
		}
		
		int leftIdx = 1;
		int rightIdx = 1;
		
		int subSum = 0;
		int answer = 1;
		
		while ((leftIdx <= rightIdx) && (rightIdx <= N)) {
			if (subSum == N) {
				answer++;
				subSum -= numArray[leftIdx];
				leftIdx++;

			}
			else if (subSum > N) {
				subSum -= numArray[leftIdx];
				leftIdx++;
			}
			else {
				subSum += numArray[rightIdx];
				rightIdx++;
			}
		}
		
		System.out.print(answer);

	}

}
