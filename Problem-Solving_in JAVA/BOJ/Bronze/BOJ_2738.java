import java.io.*;
import java.util.*;


public class BOJ_2738 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int R = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(st.nextToken());
		
		int[][] A = new int[R][C];
//		int[][] B = new int[R][C];
		
		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < C; c++) {
				A[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < C; c++) {
				A[r][c] += Integer.parseInt(st.nextToken());
			}
		}
		
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				System.out.print(A[r][c] + " ");
			}
			System.out.println("");
		}

	}

}
