import java.io.*;
import java.util.*;


public class BOJ_11403 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		int[][] Map = new int[N][N];
		
		for (int n = 0; n < N; n++) {
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				Map[n][i] = Integer.parseInt(st.nextToken());
			}
		}
		
		for (int k = 0; k < N; k++) {
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (Map[i][k] == 1 && Map[k][j] == 1) Map[i][j] = 1;
				}
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				System.out.print(Map[i][j] + " ");
			}
			System.out.println();
		}

	}

}
