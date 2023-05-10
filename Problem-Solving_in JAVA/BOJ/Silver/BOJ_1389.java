import java.io.*;
import java.util.*;


public class BOJ_1389 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		int[][] Map = new int[N][N];
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				Map[i][j] = 100001;
			}
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int s = Integer.parseInt(st.nextToken()) - 1;
			int e = Integer.parseInt(st.nextToken()) - 1;
			Map[s][e] = 1;
			Map[e][s] = 1;
		}
		
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					Map[i][j] = Math.min(Map[i][j], Map[i][k] + Map[k][j]);
				}
			}
		}
		
		int answer = 0;
		int minVal = Integer.MAX_VALUE;
		
		for (int i = 0; i < N; i++) {
			int temp = 0;
			for (int j = 0; j < N; j++) {
//				System.out.print(Map[i][j] + " ");
				temp += Map[i][j];
			}
			if (temp < minVal) {
				minVal = temp;
				answer = i+1;
			}
		}
		System.out.println(answer);

	}

}
