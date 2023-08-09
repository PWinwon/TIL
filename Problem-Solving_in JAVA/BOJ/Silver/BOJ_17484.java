import java.io.*;
import java.util.*;


public class BOJ_17484 {
	static int R, C, answer;
	
	static int[] dr = {1, 1, 1};
	static int[] dc = {-1, 0, 1};
	
	static int[][] myMap;

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		
		myMap = new int[R][C];
		
		for (int r = 0; r < R; r++) {
			st = new StringTokenizer(br.readLine());
			for (int c = 0; c < C; c++) {
				myMap[r][c] = Integer.parseInt(st.nextToken());
			}
		}
		
		answer = Integer.MAX_VALUE;
		
		for (int i = 0; i < C; i++) {
			myFunc(myMap[0][i], 0, i, -1);
		}
		
		System.out.println(answer);

	}
	
	public static void myFunc(int total, int y, int x, int d) {
		if (y == R-1) {
			if (total < answer) answer = total;
			return;
		}
		
		for (int i = 0; i < 3; i++) {
			if (d == i) continue;
			int yr = y + dr[i];
			int xr = x + dc[i];
			
			if (yr < 0 || yr >= R || xr < 0 || xr >= C) continue;
			
			myFunc(total + myMap[yr][xr], yr, xr, i);
		}
	}

}
