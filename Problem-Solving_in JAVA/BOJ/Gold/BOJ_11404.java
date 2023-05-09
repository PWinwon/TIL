import java.io.*;
import java.util.*;

public class BOJ_11404 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int M = Integer.parseInt(br.readLine());
		
		int[][] Map = new int[N][N];
		
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (r == c) Map[r][c] = 0;
				else Map[r][c] = 100001;
			}
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken()) - 1;
			int e = Integer.parseInt(st.nextToken()) - 1;
			int c = Integer.parseInt(st.nextToken());
			
			Map[s][e] = Math.min(Map[s][e], c);
		}
//		
//		for (int i = 0; i < N; i++) {
//			for (int j = 0; j < N; j++) {
//				System.out.print(Map[i][j] + " ");
//			}
//			System.out.println("");
//		}
//		
//		System.out.println("--------------------");
//		
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					Map[i][j] = Math.min(Map[i][j], Map[i][k] + Map[k][j]);
				}
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (Map[i][j] == Integer.MAX_VALUE) System.out.print("0 ");
				else System.out.print(Map[i][j] + " ");
			}
			System.out.println("");
		}

	}

}
