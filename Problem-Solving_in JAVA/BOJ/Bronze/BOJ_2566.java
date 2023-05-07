import java.io.*;
import java.util.*;

public class BOJ_2566 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int[][] A = new int [9][9];
		int maxVal = -1;
		int maxR = -1;
		int maxC = -1;
		
		for (int i = 0; i < 9; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 9; j++) {
				A[i][j] = Integer.parseInt(st.nextToken());
				if (maxVal < A[i][j]) {
					maxVal = A[i][j];
					maxR = i+1;
					maxC = j+1;
				}
			}
		}
		System.out.println(maxVal);
		System.out.println(maxR + " " + maxC);

	}

}
