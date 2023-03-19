import java.io.*;
import java.util.*;


public class BOJ_11660 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		
		long MAP[][] = new long[N+1][N+1];
		
		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j <= N; j++) {
				MAP[i][j] = MAP[i-1][j] + MAP[i][j-1] - MAP[i-1][j-1] + Integer.parseInt(st.nextToken());
			}
		}
		
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine());
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			bw.write((MAP[x2][y2] - MAP[x2][y1-1] - MAP[x1-1][y2] + MAP[x1-1][y1-1]) + "\n");
		}
		bw.close();

	}

}
